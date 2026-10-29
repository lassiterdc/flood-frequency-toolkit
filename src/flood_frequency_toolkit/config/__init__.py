"""Configuration package for flood-frequency-toolkit.

Submodules:
    defaults  — analysis-method-level default constants (return periods,
                depth thresholds, bootstrap count, plotting position)
    model     — Pydantic config models: SystemConfig, SsfhaConfig, BdsConfig,
                SSFHAConfig discriminated union, and all sub-models
    loader    — YAML loading: load_system_config, load_config, load_config_from_dict
"""

from flood_frequency_toolkit.config.loader import load_config, load_config_from_dict, load_system_config
from flood_frequency_toolkit.config.model import (
    BdsConfig,
    EventDataConfig,
    ExecutionConfig,
    FloodRiskConfig,
    GeospatialConfig,
    PPCCTConfig,
    SlurmConfig,
    SsfhaConfig,
    SSFHAConfig,
    SystemConfig,
    TritonOutputsConfig,
)

__all__ = [
    # Loader
    "load_config",
    "load_config_from_dict",
    "load_system_config",
    # Models
    "SSFHAConfig",
    "SsfhaConfig",
    "BdsConfig",
    "SystemConfig",
    "GeospatialConfig",
    "TritonOutputsConfig",
    "EventDataConfig",
    "PPCCTConfig",
    "FloodRiskConfig",
    "ExecutionConfig",
    "SlurmConfig",
]
