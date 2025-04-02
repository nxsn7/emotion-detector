"""Flask server to analyze emotions from text input."""

from flask import Flask, request, jsonify
from app.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    """API endpoint that detects emotion from given text."""
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    text = data["text"]
    result = emotion_predictor(text)

    if "error" in result:
        return jsonify(result), 400

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
