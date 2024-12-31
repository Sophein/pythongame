import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from pythongame.translations import load_translations

def test_load_translations_valid_language():
    translations = load_translations("en")
    assert "hp_left" in translations
    assert translations["hp_left"] == "{character} has {hp} HP left."

def test_load_translations_invalid_language():
    translations = load_translations("unknown")
    assert translations == {}  # Should return an empty dictionary for unsupported languages
