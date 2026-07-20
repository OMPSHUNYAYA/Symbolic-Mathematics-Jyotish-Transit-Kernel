# SSM-Jyotish Transit Kernel (SSM-JTK) - runtime-ephemeris-independent daily sidereal longitudes (Lahiri), with rasi and node identity
*v2.1 - Public research release (observation-only)*

![GitHub Release](https://img.shields.io/github/v/release/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel?style=flat&logo=github) ![GitHub Stars](https://img.shields.io/github/stars/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel?style=flat&logo=github) [![Validate](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/actions/workflows/validate.yml/badge.svg)](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/actions/workflows/validate.yml)

**SSM-JTK - v2.1 (PDF):** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/SSM_Jyotish%20Transit%20Kernel_ver2.1.pdf) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/SSM_Jyotish%20Transit%20Kernel_ver2.1.pdf)

---

# NEW — **SSM-JA Offline Deterministic Observatory**

**Live GitHub Pages observatory:**

https://ompshunyaya.github.io/Symbolic-Mathematics-Jyotish-Transit-Kernel/SSM-JA/demo/SSM-JA_v3_3_11.html

The repository now includes:

`SSM-JA/`

A browser-native observational layer built directly on the deterministic SSM-JTK kernel direction.

| Layer | Role |
|---|---|
| **SSM-JTK** | Deterministic transit-kernel foundation |
| **SSM-JA** | Runtime-ephemeris-independent offline Jyotish atlas and observational interface |

SSM-JA demonstrates **deterministic observational realization** from embedded structure:

- offline chart realization
- browser-native Panchang and transit observation
- Vimshottari Dasha continuity
- runtime kernel integrity verification
- runtime-ephemeris-independent observational continuity

The complete observatory runs from:

`one offline HTML file`

without requiring the following during local execution after download:

- runtime access to external ephemeris APIs
- cloud infrastructure
- external CSV loading
- server installation
- external astronomical services

Standalone observatory release:

[Launch SSM-JA_v3_3_11.html](./SSM-JA/demo/SSM-JA_v3_3_11.html)

Architectural milestone:

`~29 MB deterministic kernel -> embedded -> compressed -> ~3.93 MB standalone observatory`

Core structural direction:

`offline deterministic structure + fixed release -> reproducible observational realization`

See:

- [SSM-JA README](./SSM-JA/README.md)
- [SSM-JA LICENSE](./SSM-JA/LICENSE)
- [SSM-JA VERIFY](./SSM-JA/VERIFY/)

**License note:**  
The standalone `SSM-JA/` reference implementation is free to use, copy, modify, test, study, and redistribute without a license fee, subject to the terms stated in `SSM-JA/LICENSE`.

Documentation, architecture materials, specifications, diagrams, and explanatory content within `SSM-JA/` are subject to the separate terms stated in that license.

---

## What this is
Runtime-ephemeris-independent Jyotish transit kernel (SSM-JTK) that provides **daily sidereal (Lahiri) longitudes**, derived **rasi index**, and **node identity** — shipped as a golden CSV with calculation manifests and an **offline validator** for public research and observation.

---

## Quick verify (one-liner)
`python validate_golden_all.py --golden golden_all_v2_1.csv --manifests . --tol 1e-5`

---

## Files (Preview • Download)

- **Golden CSV (v2.1):** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/golden_all_v2_1.csv) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/golden_all_v2_1.csv)
- **Acceptance report:** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/acceptance_report_v2_1.txt) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/acceptance_report_v2_1.txt)
- **Validator (Python):** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/validate_golden_all.py) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/validate_golden_all.py)

See the [Spec (PDF)](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/SSM_Jyotish%20Transit%20Kernel_ver2.1.pdf).

---

## Manifests
Manifests are included in this repository as `calc_*.json` (currently in the repository root). The validator will discover them via the `--manifests .` path used above.

---

## How it works (tiny)
- Evaluator (base-linear): `t := days_since(D, t0)`; `L_hat_deg := wrap360(a0_deg + n_deg_per_day * t)`
- Wrapping helpers: `wrap360(x) := x - 360*floor(x/360)`; `rasi_idx := floor(L_hat_deg / 30)`
- Nodes identity: `wrap360(Ketu_deg(t) - Rahu_deg(t)) = 180.0`

---

## Invariants (must hold)
- Angles in `[0,360)` for all rows
- Exact rasi parity vs angles (no off-by-one)
- Nodes identity across shared dates (`max_abs_diff_from_180 = 0.0 deg`)

---

## Acceptance gates (v2.1)
- Per-body angle agreement vs golden: `max_abs_err <= 1e-5 deg`
- Rasi parity: exact match for all rows
- Nodes check: `max_abs_diff_from_180 <= 1e-9 deg` (reported as `0.000000000 deg` at current precision)

---

## Expected validator output (shape)
Planet  | rows=14975 | max_abs_err=0.00000000 deg | mismatches=  0 | PASS
         | manifest: calc_<Planet>_v20.json
...
Nodes   | shared_dates=14975 | max_abs_diff_from_180=0.000000000 deg | PASS
RESULT: PASS

---

## License

### **SSM-JTK Core Repository**

The core SSM-JTK architecture, manifests, documentation, and research materials are released under:

**CC BY-NC 4.0** (non-commercial, with attribution)

Observation-only; not for operational, safety-critical, or legal decision-making.

We do not redistribute third-party raw data unless the licence explicitly permits it.

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---

### **SSM-JA Reference Implementation**

See: [`SSM-JA/LICENSE`](SSM-JA/LICENSE)

The SSM-JA reference implementation and associated verification artifacts are free to use, copy, modify, test, study, and redistribute without a license fee, subject to the license terms stated in `SSM-JA/LICENSE`.

Documentation, architecture materials, specifications, diagrams, and explanatory content are subject to the separate terms stated in `SSM-JA/LICENSE`.

This repository does not claim recognition as a formal technical standard, security certification, production qualification, or third-party verification.

---

## Suggested GitHub Topics (Repo → About)
jyotish • runtime-ephemeris-independent • sidereal • lahiri • rasi • nodes • offline-observatory • astronomy • celestial-mechanics • time-series • csv • validator • reproducibility • offline • ascii • shunyaya • ssm • research

