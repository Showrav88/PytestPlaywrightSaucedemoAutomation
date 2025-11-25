import pytest
import json
from pathlib import Path
from playwright.async_api import async_playwright

@pytest.fixture
def testdata():
    # Go up ONE level from tests/ to SouceDemoPy
    file_path = Path(__file__).parent / "resource/testdata.json"
    file_path = file_path.resolve()  # resolves relative path to absolute
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)
