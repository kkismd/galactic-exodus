"""Test-suite entrypoint for the repository-root Python prototype.

The implementation modules and their historical test modules live at the
repository root and under ``srs``.  Keep that layout intact while exposing a
single ``tests`` discovery target for the standard unittest command.
"""

from __future__ import annotations

import importlib
import os
import sys
from pathlib import Path
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))
os.chdir(REPOSITORY_ROOT)
(REPOSITORY_ROOT / ".tmp").mkdir(exist_ok=True)


def load_tests(
    loader: unittest.TestLoader,
    _standard_tests: unittest.TestSuite,
    pattern: str | None,
) -> unittest.TestSuite:
    """Load the active root and SRS tests through ``tests`` discovery."""

    suite = unittest.TestSuite()
    module_names = [path.stem for path in sorted(REPOSITORY_ROOT.glob("test_*.py"))]
    module_names.extend(
        f"srs.{path.stem}"
        for path in sorted((REPOSITORY_ROOT / "srs").glob("test_*.py"))
    )
    for module_name in module_names:
        suite.addTests(loader.loadTestsFromModule(importlib.import_module(module_name)))
    return suite
