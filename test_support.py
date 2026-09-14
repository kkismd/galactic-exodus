"""Shared filesystem locations for tests that may run from any CWD."""

from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent
TEMP_DIR = REPOSITORY_ROOT / ".tmp"
TEMP_DIR.mkdir(exist_ok=True)
