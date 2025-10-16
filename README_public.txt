SSM-JTK v2.1 — Public Verification Bundle (minimal+)

Intro (brief)
SSM-JTK v2.1 is a tiny, ephemeris-independent transit kernel: 
one JSON-style manifest per body plus a one-line evaluator that emits daily Lahiri sidereal longitudes and the derived rāśi, fully offline and deterministic. 
Evaluator (ASCII): L_hat_deg := wrap360(a0 + n_deg_per_day*t + SUM_k( c_k*sin(omega_k*t) + d_k*cos(omega_k*t) )), 
with t := days_since(D, t0) (evaluated at 05:30 IST). Utilities: wrap360(x) := x - 360*floor(x/360) and wrap180(x) := ((x + 180) % 360) - 180. 
Rāśi rule: rasi := floor((L_hat_deg % 360)/30). Node identity: Ketu(t) := wrap360(Rahu(t) + 180).

What ships in this public research release
This bundle provides the golden day-grid (1990–2030), per-body manifests, a pure-stdlib validator, and the acceptance report. 
The validator checks angle equality <= 1e-5 degrees after wrap360, exact rasi parity, and node symmetry; all pass on this drop. 
For integrity, the SHA-256 for golden_all_v2_1.csv is embedded below. Observation-only; non-commercial evaluation and internal tooling.

Contents

golden_all_v2_1.csv (daily Lahiri, multi-planet; 1990-01-01 … 2030-12-31 UTC day grid)

manifests\calc_*.json (per-body release-truth manifests)

validate_golden_all.py (public validator)

acceptance_report_v2_1.txt (PASS log by planet)

Quick verify (Python 3.x)

python validate_golden_all.py --golden "golden_all_v2_1.csv" --manifests ".\manifests" --tol 1e-5


Expected: PASS for all planets; node symmetry check PASS.

Schema (golden_all_v2_1.csv)

planet,date,L_hat_deg,rasi
- planet    : {Sun,Moon,Mercury,Venus,Mars,Jupiter,Saturn,Uranus,Neptune,Rahu,Ketu}
- date      : YYYY-MM-DD (UTC day grid)
- L_hat_deg : sidereal ecliptic longitude (Lahiri), degrees in [0,360)
- rasi      : floor(L_hat_deg / 30)  (0..11)


Rāśi rule
rasi := floor((L_hat_deg % 360)/30) using Euclidean modulus.

Evaluator note
L_hat_deg := wrap360(a0 + n_deg_per_day*t + SUM_k( c_k*sin(omega_k*t) + d_k*cos(omega_k*t) ))
t := days_since(D, t0) at 05:30 IST; omega_k in rad/day; coefficients in degrees.

Coverage & bodies
Daily 1990–2030; Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Rahu, Ketu.
Deep-time capability: the kernel and manifests support a monthly-grid sampler for years 0001–9500 (optional; not included in this minimal bundle).

Integrity (known SHA-256)
Windows (either):

certutil -hashfile "golden_all_v2_1.csv" SHA256
PowerShell: Get-FileHash -Algorithm SHA256 .\golden_all_v2_1.csv


macOS/Linux:

sha256sum golden_all_v2_1.csv
# or: shasum -a 256 golden_all_v2_1.csv


Expected for golden_all_v2_1.csv:

00808FACBC298631018E8F4CA4B43D10BE10BDCCF47D674AA17F771E2BE2326F


Note: no separate checksums file in v2.1; digest embedded here.

Versioning / provenance
Emitted by the SSM-JTK v2.1 calculation pipeline; public validator PASS (rāśi parity & node identity). The acceptance report in this bundle covers the 1990–2030 daily grid.

License / use (summary)
Observation-only; non-commercial evaluation and internal tooling. No public redistribution. See full license.