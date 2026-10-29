---
impact: High
urgency: High
loe: Low
risk: Low
priority: 2.70
priority-label: "Do now"
created: 2026-03-14
description: "Phase 1 — quick-win fixes from SE audit: assert→raise, SSFHAConfig consolidation, dead file cleanup, geo ext dedup"
master: docs/planning/refactors/se_audit_remediation/master.md
---

# Phase 1: Quick Wins

## Dependencies

**Upstream**: None.
**Downstream**: Phases 2, 3, 4 (SSFHAConfig consolidation is consumed by all later phases).

## Task Understanding

### Requirements

Address audit findings Section 1, items 1, 3, 4, and 5. Item 2 (unseeded RNG) moves to Phase 2 because it requires threading a `rng` parameter through the call chain — not a quick win.

### Success Criteria

- `assert` replaced with `raise ConfigurationError` in `event_comparison.py`
- `SSFHAConfig` defined in one place, imported everywhere else
- `utils.py` deleted; `cli.py` reduced to minimal stub
- `_supported_geo_ext` in `validation.py` imports from `gis_io.py`
- All tests pass

## File-by-File Change Plan

### Modified Files

| File | Change |
|------|--------|
| `src/flood_frequency_toolkit/analysis/event_comparison.py` | Replace `assert ev_vars is not None` (line 435) with `if ev_vars is None: raise ConfigurationError(...)` |
| `src/flood_frequency_toolkit/validation.py` | Delete `SSFHAConfig = Union[SsfhaConfig, BdsConfig]` (line 30) and the `Union` import. Import `SSFHAConfig` from `flood_frequency_toolkit.config.model` instead. Delete `_supported_geo_ext` (line 215) and import `_SUPPORTED_GEO_EXTENSIONS` from `flood_frequency_toolkit.io.gis_io` — rename local usage to match. |
| `src/flood_frequency_toolkit/paths.py` | Delete `SSFHAConfig = SsfhaConfig \| BdsConfig` (line 48, inside `TYPE_CHECKING`). Import `SSFHAConfig` from `flood_frequency_toolkit.config.model` instead. |
| `src/flood_frequency_toolkit/cli.py` | Replace entire body with minimal stub: `app = typer.Typer()` + a `main()` command that prints "CLI not yet implemented — see docs/planning/refactors/2026-02-25_full_codebase_refactor/work_chunks/04B_execution_and_cli.md". Remove `from flood_frequency_toolkit import utils`. |

### Deleted Files

| File | Reason |
|------|--------|
| `src/flood_frequency_toolkit/utils.py` | Placeholder-only file. Not imported by any production code or test except `cli.py`, which will stop importing it. |

### Import Sites to Update

- `validation.py`: add `from flood_frequency_toolkit.config.model import SSFHAConfig` and `from flood_frequency_toolkit.io.gis_io import _SUPPORTED_GEO_EXTENSIONS`; remove `from typing import Union` if no other usage
- `paths.py`: add `from flood_frequency_toolkit.config.model import SSFHAConfig` inside `TYPE_CHECKING` block
- `event_comparison.py`: add `from flood_frequency_toolkit.exceptions import ConfigurationError` if not already imported (verify)

## Risks and Edge Cases

| Risk | Mitigation |
|------|-----------|
| Circular import between `validation.py` → `config.model` | `validation.py` already imports from `flood_frequency_toolkit.config` (line 24-29). Adding `SSFHAConfig` to that import is safe — no cycle. |
| Circular import between `validation.py` → `io.gis_io` | `gis_io` does not import from `validation`. Safe. |
| `paths.py` import under `TYPE_CHECKING` | Runtime-safe by definition — only used by type checkers. |
| `cli.py` change breaks installed console script | The stub still defines `app = typer.Typer()` with a `main()` command, so `flood_frequency_toolkit` console entry point works — it just prints a "not yet implemented" message. |

## Validation Plan

```bash
conda run -n fft pytest tests/ -v
conda run -n fft python -c "from flood_frequency_toolkit.validation import SSFHAConfig; print(SSFHAConfig)"
conda run -n fft python -c "from flood_frequency_toolkit.paths import SSFHAConfig; print(SSFHAConfig)"
```

## Definition of Done

- [ ] `assert` → `raise ConfigurationError` in `event_comparison.py`
- [ ] `SSFHAConfig` imported from `config.model` in `validation.py` and `paths.py` — no local definitions
- [ ] `_supported_geo_ext` replaced with `_SUPPORTED_GEO_EXTENSIONS` import in `validation.py`
- [ ] `src/flood_frequency_toolkit/utils.py` deleted
- [ ] `src/flood_frequency_toolkit/cli.py` reduced to minimal stub
- [ ] All tests pass
- [ ] Architecture.md not changed (no module structure changes)
- [ ] Move this doc to `implemented/`
