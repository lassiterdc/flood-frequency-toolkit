"""Runner scripts for flood-frequency-toolkit workflows.

Each runner is a CLI entry point invocable by Snakemake via
``python -m flood_frequency_toolkit.runners.<name>``. Runners log to stdout
(captured by Snakemake into logfiles) and emit a structured
completion marker on success.
"""
