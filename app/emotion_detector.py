from textblob import TextBlob

def emotion_predictor(text):
    """使用 TextBlob 進行情緒分析"""
    if not text.strip():  # 處理空白輸入
        return {"error": "Input text cannot be empty."}

    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        emotion = "positive"
    elif polarity < 0:
        emotion = "negative"
    else:
        emotion = "neutral"

    return {"emotion": emotion, "score": polarity}
