# SSM-Jyotish Transit Kernel (SSM-JTK) - ephemeris-independent daily sidereal longitudes (Lahiri), with rasi and node identity
*v2.1 - Public research release (observation-only)*

![GitHub Release](https://img.shields.io/github/v/release/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel?style=flat&logo=github) ![GitHub Stars](https://img.shields.io/github/stars/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel?style=flat&logo=github) ![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-blue?style=flat&logo=creative-commons) [![Validate](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/actions/workflows/validate.yml/badge.svg)](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/actions/workflows/validate.yml)

**SSM-JTK - v2.1 (PDF):** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/SSM_Jyotish%20Transit%20Kernel_ver2.1.pdf) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/SSM_Jyotish%20Transit%20Kernel_ver2.1.pdf)

## What this is
Ephemeris-independent Jyotish transit kernel (SSM-JTK) that provides **daily sidereal (Lahiri) longitudes**, derived **rasi index**, and **node identity** — shipped as a golden CSV with calc manifests and an **offline validator** (public research).

## Quick verify (one-liner)
`python validate_golden_all.py --golden golden_all_v2_1.csv --manifests . --tol 1e-5`

## Files (Preview • Download)
- **Golden CSV (v2.1):** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/golden_all_v2_1.csv) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/golden_all_v2_1.csv)
- **Acceptance report:** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/acceptance_report_v2_1.txt) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/acceptance_report_v2_1.txt)
- **Validator (Python):** [Preview](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/validate_golden_all.py) • [Download](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/raw/main/validate_golden_all.py)

See the [Spec (PDF)](https://github.com/OMPSHUNYAYA/Symbolic-Mathematics-Jyotish-Transit-Kernel/blob/main/SSM_Jyotish%20Transit%20Kernel_ver2.1.pdf).

## Manifests
Manifests are included in this repository as `calc_*.json` (currently in the repository root). The validator will discover them via the `--manifests .` path used above.

## How it works (tiny)
- Evaluator (base-linear): `t := days_since(D, t0)`; `L_hat_deg := wrap360(a0_deg + n_deg_per_day * t)`
- Wrapping helpers: `wrap360(x) := x - 360*floor(x/360)`; `rasi_idx := floor(L_hat_deg / 30)`
- Nodes identity: `wrap360(Ketu_deg(t) - Rahu_deg(t)) = 180.0`

## Invariants (must hold)
- Angles in `[0,360)` for all rows
- Exact rasi parity vs angles (no off-by-one)
- Nodes identity across shared dates (`max_abs_diff_from_180 = 0.0 deg`)

## Acceptance gates (v2.1)
- Per-body angle agreement vs golden: `max_abs_err <= 1e-5 deg`
- Rasi parity: exact match for all rows
- Nodes check: `max_abs_diff_from_180 <= 1e-9 deg` (reported as `0.000000000 deg` at current precision)

## Expected validator output (shape)
Planet  | rows=14975 | max_abs_err=0.00000000 deg | mismatches=  0 | PASS
         | manifest: calc_<Planet>_v20.json
...
Nodes   | shared_dates=14975 | max_abs_diff_from_180=0.000000000 deg | PASS
RESULT: PASS

## License 
© The Authors of Shunyaya Framework and Shunyaya Symbolic Mathematics. Released under CC BY-NC 4.0 (non-commercial, with attribution).  
Observation-only; not for operational, safety-critical, or legal decision-making.  
We do not redistribute third-party raw data unless the licence explicitly permits it.

[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

## Suggested GitHub Topics (Repo → About)
jyotish • ephemeris-independent • sidereal • lahiri • rasi • nodes • ephemeris-free • astronomy • celestial-mechanics • time-series • csv • validator • reproducibility • offline • ascii • shunyaya • ssm • research

