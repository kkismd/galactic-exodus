"""Bridge the repository's active tests into unittest discovery."""

import sys
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from tests import load_tests

__all__ = ["load_tests"]
