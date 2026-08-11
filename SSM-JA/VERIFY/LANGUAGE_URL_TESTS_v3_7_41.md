# SSM-JA v3.7.41 - Direct Language URL Verification

## Release Status

```text
DIRECT_LANGUAGE_URL_SUPPORT = PASS
SIX_LANGUAGE_PRESENTATION = PASS
LANGUAGE_PRESENTATION_ONLY = PASS
UNIVERSAL_FRESH_DEFAULT_LOCATION = PASS
SHARE_STATE_LANGUAGE_INDEPENDENCE = PASS
MULTILINGUAL_PRINT_PRESENTATION = PASS
CONTEXT_SENSITIVE_PAKSHA_TRANSLATION = PASS
HTML_RELEASE_READINESS = READY_FOR_RELEASE
HTML_RELEASE_BYTES = FROZEN
WHOLE_FILE_SHA256_STATUS = VERIFIED
WHOLE_FILE_SHA256 = 0fade1279bc389028ba05001e9d6542c5ab0ec40fc51988b06e55f1544451eb1
```

This document applies to the frozen SSM-JA v3.7.41 standalone HTML release and supersedes the earlier v3.7.33 language-routing verification record.

### Target Release

`demo\SSM-JA_v3_7_41.html`

### Target Public Launcher

`SSM-JA/`

## 1. LANGUAGE ROUTING SCHEME

`?lang=en  -> English`
`?lang=ta  -> Tamil`
`?lang=te  -> Telugu`
`?lang=kn  -> Kannada`
`?lang=ml  -> Malayalam`
`?lang=hi  -> Hindi`

Verified rules:

- the lang query parameter is read during application startup
- en/ta/te/kn/ml/hi map to the six supported presentation languages
- missing or unsupported language values fall back safely to English
- query parsing is case-normalized
- language selection applies to the same standalone application
- language selection does not select a separate astronomical engine
- language selection does not select a geographical subprofile
- all six languages use the same embedded deterministic kernel
- no language-specific duplicate HTML application is required

```text
DIRECT_LANGUAGE_URL_STARTUP = PASS
```

## 2. SHARE-STATE SCHEME

Structural application state:

`#ssmja=...`

Frozen separation rule:

`?lang=... controls presentation language.`
`#ssmja=... controls encoded application state.`

`LANGUAGE != STRUCTURAL_STATE`
`LANGUAGE != LOCATION_PROFILE`

Language and Share State remain independent.

## 3. UNIVERSAL FRESH DEFAULT LOCATION

The fresh/default location is the same in all six languages:

New Delhi, Delhi, India
Latitude: 28.6139
Longitude: 77.209
Timezone basis: Asia/Kolkata / current resolved offset

A user-selected or manually entered location remains user state and is not replaced merely by changing presentation language.

```text
UNIVERSAL_FRESH_DEFAULT_LOCATION = PASS
```

## 4. CANONICAL PUBLIC LANGUAGE URLS

After publication, the stable public launcher may be addressed as:

English
`.../SSM-JA/?lang=en`

Tamil
`.../SSM-JA/?lang=ta`

Telugu
`.../SSM-JA/?lang=te`

Kannada
`.../SSM-JA/?lang=kn`

Malayalam
`.../SSM-JA/?lang=ml`

Hindi
`.../SSM-JA/?lang=hi`

The repository host prefix may vary.
The path/query contract remains the same.

## 5. VERSIONED DIRECT URLS

The frozen release may be addressed directly as:

`.../SSM-JA/demo/SSM-JA_v3_7_41.html?lang=en`
`.../SSM-JA/demo/SSM-JA_v3_7_41.html?lang=ta`
`.../SSM-JA/demo/SSM-JA_v3_7_41.html?lang=te`
`.../SSM-JA/demo/SSM-JA_v3_7_41.html?lang=kn`
`.../SSM-JA/demo/SSM-JA_v3_7_41.html?lang=ml`
`.../SSM-JA/demo/SSM-JA_v3_7_41.html?lang=hi`

Verified behavior:

- one release identity
- one embedded kernel
- six presentation languages
- same calculations for the same structural input
- correct document language code
- no manual language click is required after direct startup

## 6. MISSING OR INVALID LANGUAGE PARAMETER

Representative forms:

no lang parameter
`?lang=xx`
`?lang=`
`?lang=unknown`
`?lang=123`
`?lang=fr`

Verified contract:

- safe fallback to English
- same release identity
- same embedded kernel
- no geographical side effect
- no malformed Share State behavior
- no blank application state

```text
MISSING_LANG_FALLBACK = PASS
INVALID_LANG_FALLBACK = PASS
```

## 7. CASE NORMALIZATION

Representative forms:

`?lang=EN`
`?lang=TA`
`?lang=Te`
`?lang=Kn`
`?lang=ML`
`?lang=Hi`

```text
LANG_PARAMETER_CASE_NORMALIZED = TRUE
```

## 8. SIX-LANGUAGE PRESENTATION IDENTITIES

English
document language code: en
presentation language: English

Tamil
document language code: ta
presentation language: Tamil

Telugu
document language code: te
presentation language: Telugu

Kannada
document language code: kn
presentation language: Kannada

Malayalam
document language code: ml
presentation language: Malayalam

Hindi
document language code: hi
presentation language: Hindi

All six language metadata identities and principal navigation labels were verified.

```text
SIX_LANGUAGE_PRESENTATION = PASS
LANG_ATTRIBUTE_MATCHES_UI_LANGUAGE = PASS
```

## 9. STARTUP LANGUAGE REALIZATION

For each supported non-English direct URL, the application settles directly into the requested presentation language without requiring a manual switch.

```text
DIRECT_LANGUAGE_STARTUP_WITHOUT_MANUAL_SWITCH = PASS
```

## 10. UI LANGUAGE SWITCH AND URL SYNCHRONIZATION

The in-application language selector synchronizes the lang query parameter while preserving application structure.

Verified behavior:

- current path is preserved
- active structural state is preserved
- selected language and visible URL agree
- obsolete region parameter is removed during canonicalization
- unrelated supported query parameters are retained
- language-only navigation uses history replacement behavior

```text
UI_LANGUAGE_URL_SYNC = PASS
```

## 11. LEGACY TELUGU URL CANONICALIZATION

Legacy forms such as:

`?lang=te&region=ts`
`?lang=te&region=ap`

resolve to the single Telugu presentation identity.

There is exactly one Telugu presentation mode.
The region parameter is not a separate language identity.

```text
TELUGU_CANONICALIZATION = PASS
```

## 12. LANGUAGE AND SHARE STATE

Canonical combined form:

...?lang=ta#ssmja=ENCODED_STATE

Verified contract:

- the language query remains presentation state
- the #ssmja fragment remains structural application state
- language switching does not destroy the state fragment
- state import does not silently create a different language identity
- hash-only Share State remains compatible with English fallback
- query-before-hash ordering is supported

```text
LANGUAGE_QUERY_PRESERVED_IN_SHARE_LINK = TRUE
SHARE_STATE_LANGUAGE_INDEPENDENCE = PASS
```

## 13. NUMERICAL INVARIANCE ACROSS LANGUAGES

Frozen principle:

same structural input
+ same release
+ same calculation settings
+ language-only change
`->`
same numerical realization

Presentation text may change.
The underlying numerical realization does not change because of presentation language.

Verified areas include:

- planetary values
- Rasi/Navamsa placement
- Nakshatra/Pada
- Vimshottari Dasha structure
- Panchang realization
- Transit realization
- committed structural state

```text
NUMERICAL_LANGUAGE_INVARIANCE = PASS
```

## 14. CONTEXT-SENSITIVE SHUKLA TRANSLATION

v3.7.41 distinguishes Shukla as a Paksha/Tithi qualifier from Shukla as the proper name of a Yoga where the language requires different forms.

Verified forms:

| Language | Paksha/Tithi form | Yoga-name form |
|---|---|---|
| English | Shukla | Shukla |
| Tamil | சுக்ல | சுக்லம் |
| Telugu | శుక్ల | శుక్లం |
| Kannada | ಶುಕ್ಲ | ಶುಕ್ಲ |
| Malayalam | ശുക്ല | ശുക്ലം |
| Hindi | शुक्ल | शुक्ल |

Representative verified Tithi phrases:

| Language | Form |
|---|---|
| English | Shukla Chaturdashi |
| Tamil | சுக்ல சதுர்த்தசி |
| Telugu | శుక్ల చతుర్దశి |
| Kannada | ಶುಕ್ಲ ಚತುರ್ದಶಿ |
| Malayalam | ശുക്ല ചതുര്ദശി |
| Hindi | शुक्ल चतुर्दशी |

The context distinction is applied to the normal Panchang presentation and to both print/report paths.

```text
CONTEXT_SENSITIVE_PAKSHA_TRANSLATION = PASS
PRINT_PAKSHA_CONTEXT_TRANSLATION = PASS
```

## 15. TELUGU TERMINOLOGY CLOSURE

Verified Telugu forms include:

| Term | Telugu |
|---|---|
| Gulika | గుళిక |
| Choghadiya | చౌఘడియా |

```text
TELUGU_TERMINOLOGY_CLOSURE = PASS
```

## 16. LOCALIZED FULL-MONTH DATE PRESENTATION

Localized month presentation was verified across the six supported languages.

Representative September forms:

| Language | September |
|---|---|
| English | September |
| Tamil | செப்டம்பர் |
| Telugu | సెప్టెంబర్ |
| Kannada | ಸೆಪ್ಟೆಂಬರ್ |
| Malayalam | സെപ്റ്റംബർ |
| Hindi | सितंबर |

Internal/state dates may remain ISO YYYY-MM-DD.
Ordinary user-facing date presentation uses localized month names.

```text
LOCALIZED_FULL_MONTH_DATE_ARCHITECTURE = PASS
```

## 17. MOON-CYCLE DATE LOCALIZATION

The Moonrise-cycle presentation preserves the underlying event date while localizing the displayed month text.

Verified cross-date example for New Delhi:

Selected cycle:
Moonrise raw local date = 2016-06-19
Moonset raw local date  = 2016-06-20

Previous cycle:
Moonrise raw local date = 2016-06-18
Moonset raw local date  = 2016-06-19

The same event dates remain valid when the display language changes.

```text
MOON_CYCLE_LOCALIZED_DATE_PRESENTATION = PASS
```

## 18. RESPONSIVE MULTILINGUAL PRESENTATION

Verified release expectations:

- desktop presentation remains usable across all six languages
- <= 980px responsive stacking is supported
- <= 560px single-column control layout is supported
- localized labels remain inside their intended controls
- the Previous-date Moonrise Cycle reference remains full-width and wrap-safe
- no language-driven location reset occurs
- no language-driven calculation mutation occurs

```text
RESPONSIVE_MULTILINGUAL_PRESENTATION = PASS
```

## 19. PRINT / REPORT LANGUAGE PRESENTATION

Brief and Detailed print/report paths remain language-aware.

v3.7.41 specifically verifies that Paksha/Tithi text uses the Paksha-context translation instead of the generic Yoga-name translation.

Verified principles:

- presentation localization remains separate from calculation
- Rasi/Navamsa localization remains presentation-only
- user-facing dates use localized month names
- Unicode names and Indic scripts remain supported
- print/report generation does not create a separate calculation engine

```text
MULTILINGUAL_PRINT_PRESENTATION = PASS
```

## 20. OFFLINE / LOCAL-FILE BEHAVIOR

The standalone HTML remains usable locally/offline through the same application and in-application language selector.

Direct web URL language routing is a convenience layer, not an external runtime calculation dependency.

```text
OFFLINE_LANGUAGE_SELECTION = PASS
```

## 21. PUBLIC LAUNCHER

If a separate SSM-JA/index.html stable launcher is published, verify after upload that it preserves:

- ?lang=...
- #ssmja=...
- current stable version routing
- direct access to the frozen versioned HTML
- historical versioned files

```text
PUBLIC_LAUNCHER_POST_UPLOAD_SMOKE_TEST = PENDING_IF_APPLICABLE
```

## 22. ACCEPTANCE MATRIX

| LANGUAGE | DIRECT URL | DEFAULT LOCATION | UI | NUMERICAL ISOLATION | SHARE STATE | PRINT | RESPONSIVE |
|---|---|---|---|---|---|---|---|
| English | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Tamil | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Telugu | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Kannada | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Malayalam | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| Hindi | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

## 23. RELEASE FREEZE IDENTITY

Frozen file:
`demo\SSM-JA_v3_7_41.html`

File size: **4,635,245 bytes**

Whole-file SHA-256:
`0fade1279bc389028ba05001e9d6542c5ab0ec40fc51988b06e55f1544451eb1`

Embedded Golden Kernel SHA-256:
`7bdebadfc764ef1f1cc2fc75cd3aaccdc48733f343f3e7311bc4503c354fa351`

Important:

`EMBEDDED_KERNEL_SHA256`
`!=`
`WHOLE_FILE_HTML_SHA256`

The whole-file HTML SHA-256 identifies the exact frozen release bytes.
The embedded-kernel SHA-256 identifies the deterministic embedded kernel used by the runtime integrity mechanism.

## 24. FINAL PUBLICATION STATUS

- [x] six direct language startup routes verified
- [x] missing/invalid language fallback verified
- [x] case-normalized language query verified
- [x] universal New Delhi fresh-default rule verified
- [x] manual location protection verified
- [x] language/state independence verified
- [x] Share State query/hash separation verified
- [x] six-language presentation verified
- [x] localized month presentation verified
- [x] numerical invariance under language-only switching verified
- [x] context-sensitive Shukla Paksha/Yoga translation verified
- [x] print/report Paksha translation verified
- [x] Telugu terminology closure verified
- [x] responsive multilingual presentation verified
- [x] frozen whole-file SHA-256 independently confirmed
- [ ] public launcher smoke test after upload, if a separate launcher is used

## Final Document Status

```text
RELEASE = SSM-JA v3.7.41
DIRECT_LANGUAGE_URL_SUPPORT = PASS
SIX_LANGUAGE_PRESENTATION = PASS
LANGUAGE_PRESENTATION_ONLY = PASS
CONTEXT_SENSITIVE_PAKSHA_TRANSLATION = PASS
MULTILINGUAL_PRINT_PRESENTATION = PASS
BROWSER_QA = PASS
HTML_RELEASE_READINESS = READY_FOR_RELEASE
HTML_RELEASE_BYTES = FROZEN
WHOLE_FILE_SHA256_STATUS = VERIFIED
WHOLE_FILE_SHA256 = 0fade1279bc389028ba05001e9d6542c5ab0ec40fc51988b06e55f1544451eb1
```
