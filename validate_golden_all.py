# validate_golden_all.py — pure-stdlib validator (Windows-friendly)
# Usage (from CMD):
#   py -3 validate_golden_all.py ^
#     --golden "C:\Users\ASUS\Desktop\Ephemeris\Final Test\golden_all_v2_1.csv" ^
#     --manifests "C:\Users\ASUS\Desktop\Ephemeris\JTK_v2_0_RUN1\JTK_v2_0_RUN3\manifests_calc_flat" ^
#     --tol 1e-5
#
# Checks:
#  • Angle match to <= tol (after wrap180) and exact rasi match for every golden row
#  • Rahu/Ketu identity: Ketu = wrap360(Rahu + 180) within 1e-6°
# Exit codes: 0=PASS, 1=FAIL, 2=IO/format error

import sys, os, csv, json, math
from datetime import date

def emod(x, m): return ((x % m) + m) % m
def wrap360(x): return x - 360.0 * math.floor(x / 360.0)
def wrap180(x): return emod(x + 180.0, 360.0) - 180.0

def rasi_from_deg(L):
    Lw = wrap360(L)
    k = round(Lw / 30.0)
    if abs(Lw - 30.0 * k) <= 5e-12:  # tie → higher rasi (12→0)
        return int(k % 12)
    return int(math.floor(emod(Lw, 360.0) / 30.0))

def days_since(date_iso, t0_iso):
    y, m, d = map(int, date_iso.split("-"))
    y0, m0, d0 = map(int, t0_iso.split("-"))
    return (date(y, m, d) - date(y0, m0, d0)).days

def eval_angle_from_parts(a0, n, t0, terms, date_iso):
    t = days_since(date_iso, t0)
    y = a0 + n * t
    for (w, c, d) in terms:
        y += c * math.sin(w * t) + d * math.cos(w * t)
    return wrap360(y)

def load_manifest_shape(path):
    with open(path, "r", encoding="utf-8") as f:
        man = json.load(f)
    # Extract minimal runtime parts; accept several shapes (calc-flat, named, terms[])
    # a0
    a0 = None
    if isinstance(man.get("beta"), dict):
        a0 = man["beta"].get("a0_deg", man["beta"].get("a0"))
    if a0 is None:
        a0 = man.get("a0_deg", 0.0)
    a0 = float(a0)

    # n (order: beta.b1, n_deg_per_day, 360/P_sid_days)
    b = man.get("beta") or {}
    if "b1_deg_per_day" in b:
        n = float(b["b1_deg_per_day"])
    elif "n_deg_per_day" in man:
        n = float(man["n_deg_per_day"])
    else:
        P_sid = man.get("P_sid_days")
        if P_sid:
            n = 360.0 / float(P_sid)
        else:
            raise ValueError("Cannot determine n_deg_per_day in %s" % path)

    # t0
    if "t0" in man:
        t0 = man["t0"]
    else:
        t0_iso = man.get("t0_ISO")
        if not t0_iso:
            raise ValueError("Missing t0/t0_ISO in %s" % path)
        t0 = t0_iso.split("T")[0]

    # terms: prefer explicit terms[], else omegas+beta pairs, else harmonics[]
    terms = []
    if isinstance(man.get("terms"), list) and man["terms"]:
        for term in man["terms"]:
            terms.append( (float(term["w_rad_per_day"]), float(term["c_sin"]), float(term["d_cos"])) )
    elif isinstance(man.get("omegas"), dict) and man["omegas"]:
        omg = man["omegas"]; bet = man.get("beta", {})
        for suf, wkey in [("1","w1"),("2","w2"),("3","w3"),("S","wS"),("E","nE"),("A","wA"),("D","wD")]:
            if (wkey in omg) and (("c"+suf) in bet) and (("d"+suf) in bet):
                terms.append( (float(omg[wkey]), float(bet["c"+suf]), float(bet["d"+suf])) )
    elif isinstance(man.get("harmonics"), list) and man["harmonics"]:
        for term in man["harmonics"]:
            w = float(term.get("w_rad_per_day", 0.0))
            c = float(term.get("c_sin", 0.0))
            d = float(term.get("d_cos", 0.0))
            terms.append((w,c,d))

    return {
        "planet": (man.get("planet") or "").strip(),
        "t0": t0,
        "a0": float(a0),
        "n": float(n),
        "terms": terms,
        "raw": man,
        "path": path
    }

def peek_manifest_planet(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            man = json.load(f)
        p = man.get("planet")
        return p.strip() if isinstance(p, str) else None
    except Exception:
        return None

def choose_manifest_for(planet, manifest_dir):
    # Prefer exact planet match by content (not filename). If not found for Ketu, allow fallback to Rahu.
    best = None
    for fn in os.listdir(manifest_dir):
        if not fn.lower().endswith(".json"): 
            continue
        path = os.path.join(manifest_dir, fn)
        p = peek_manifest_planet(path)
        if p and p.lower() == planet.lower():
            best = path if (best is None) else best
    if (best is None) and (planet.lower() == "ketu"):
        # fallback: use Rahu manifest and add +180 at eval time
        for fn in os.listdir(manifest_dir):
            if not fn.lower().endswith(".json"):
                continue
            path = os.path.join(manifest_dir, fn)
            p = peek_manifest_planet(path)
            if p and p.lower() == "rahu":
                return (path, True)  # fallback flag
    return (best, False)

def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--golden", required=True)
    ap.add_argument("--manifests", required=True)
    ap.add_argument("--tol", type=float, default=1e-5)
    args = ap.parse_args()

    if not os.path.isfile(args.golden):
        print("ERROR: golden CSV not found:", args.golden); sys.exit(2)
    if not os.path.isdir(args.manifests):
        print("ERROR: manifests folder not found:", args.manifests); sys.exit(2)

    # Load golden rows
    rows = []
    with open(args.golden, "r", encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        needed = {"planet","date","L_hat_deg","rasi"}
        missing = [k for k in needed if k not in r.fieldnames]
        if missing:
            print("ERROR: golden missing columns:", ", ".join(missing))
            print("Headers:", r.fieldnames); sys.exit(2)
        for row in r:
            rows.append({
                "planet": row["planet"].strip(),
                "date": row["date"].strip(),
                "L_csv": float(row["L_hat_deg"]),
                "rasi_csv": int(row["rasi"])
            })

    # Group by planet
    byP = {}
    for rr in rows:
        byP.setdefault(rr["planet"], []).append(rr)

    overall_fail = False
    rahu_eval = {}
    ketu_eval = {}

    print("Golden   :", args.golden)
    print("Manifests:", args.manifests)
    print("Tol(deg) :", args.tol)
    print("-"*72)

    for planet in sorted(byP.keys()):
        mpath, ketu_fallback = choose_manifest_for(planet, args.manifests)
        if mpath is None:
            print(f"{planet:8s} | FAIL — manifest not found")
            overall_fail = True
            continue

        try:
            man = load_manifest_shape(mpath)
        except Exception as e:
            print(f"{planet:8s} | FAIL — load error: {e}")
            overall_fail = True
            continue

        mism, nrows, max_abs = 0, 0, 0.0
        for r in byP[planet]:
            nrows += 1
            L_eval = eval_angle_from_parts(man["a0"], man["n"], man["t0"], man["terms"], r["date"])
            if ketu_fallback:
                L_eval = wrap360(L_eval + 180.0)
            diff = abs(wrap180(L_eval - r["L_csv"]))
            if diff > max_abs: max_abs = diff
            if (diff > args.tol) or (rasi_from_deg(L_eval) != r["rasi_csv"]):
                mism += 1

            if planet.lower() == "rahu":
                rahu_eval[r["date"]] = L_eval
            elif planet.lower() == "ketu":
                ketu_eval[r["date"]] = L_eval

        status = "PASS" if mism == 0 else "FAIL"
        if status == "FAIL": overall_fail = True
        note = " (fallback=Rahu+180)" if ketu_fallback else ""
        print(f"{planet:8s} | rows={nrows:3d} | max_abs_err={max_abs:.8f} deg | mismatches={mism:3d} | {status}")
        print(f"          | manifest: {os.path.basename(mpath)}{note}")

    # Node identity (shared dates)
    shared = sorted(set(rahu_eval.keys()) & set(ketu_eval.keys()))
    if shared:
        max_dev, bad = 0.0, 0
        for d in shared:
            dev = abs(wrap360(ketu_eval[d] - rahu_eval[d]) - 180.0)
            if dev > max_dev: max_dev = dev
            if dev > 1e-6: bad += 1
        print("-"*72)
        print(f"Nodes     | shared_dates={len(shared)} | max|Δ-180|={max_dev:.9f} deg | {'PASS' if bad==0 else 'FAIL'}")
        if bad: overall_fail = True

    print("-"*72)
    print("RESULT:", "PASS" if not overall_fail else "FAIL")
    sys.exit(0 if not overall_fail else 1)

if __name__ == "__main__":
    main()
