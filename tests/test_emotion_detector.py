import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.emotion_detector import emotion_predictor

import pytest
from app.emotion_detector import emotion_predictor

def test_positive_emotion():
    result = emotion_predictor("I love this so much!")
    assert result["emotion"] == "positive"
    assert result["score"] > 0

def test_negative_emotion():
    result = emotion_predictor("This is terrible and I hate it.")
    assert result["emotion"] == "negative"
    assert result["score"] < 0

def test_neutral_emotion():
    result = emotion_predictor("This is a table.")
    assert result["emotion"] == "neutral"
    assert result["score"] == 0

def test_empty_input():
    result = emotion_predictor("   ")
    assert "error" in result
