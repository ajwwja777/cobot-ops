#!/usr/bin/env python3
"""Compatibility entry only; the implementation is owned by cobot-web."""
from pathlib import Path
import runpy
import sys

target = Path(__file__).resolve().parents[2] / "cobot-web/scripts/console_recovery.py"
if not target.is_file():
    raise SystemExit("Cobot Web recovery tool is missing; restore its deployment before using this legacy entry")
sys.argv[0] = str(target)
runpy.run_path(str(target), run_name="__main__")
