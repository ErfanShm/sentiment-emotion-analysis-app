import random
import time
import streamlit as st

def classify_text(text, pipe):
    result = pipe(text)[0]  # Extract the inner list from the pipeline output
    return result

def get_emoji(sentiment):
    if sentiment == "positive":
        return random.choice(["😊", "😄", "🎉", "👍", "🌟"])
    elif sentiment == "neutral":
        return random.choice(["😐", "😶", "🤔", "😑", "😏"])
    else:
        return random.choice(["😔", "😢", "👎", "🌧️", "💔"])

def get_fun_fact(sentiment):
    positive_facts = [
        "Did you know? Smiling can boost your mood and immune system!",
        "Optimists tend to live longer than pessimists. Keep up the positivity!",
        "Laughing for 15 minutes burns up to 40 calories. Time for a comedy!",
    ]
    neutral_facts = [
        "Neutral emotions can be a sign of a balanced perspective.",
        "Did you know? Being neutral can help in making unbiased decisions.",
        "Keeping a neutral stance can sometimes be the best approach in conflicts."
    ]
    negative_facts = [
        "Chocolate can help improve your mood. Maybe it's time for a treat?",
        "Negative emotions can be useful for problem-solving and critical thinking.",
        "Did you know? Crying can help release stress and improve your mood.",
    ]
    if sentiment == "positive":
        return random.choice(positive_facts)
    elif sentiment == "neutral":
        return random.choice(neutral_facts)
    else:
        return random.choice(negative_facts)

def get_sentiment_history():
    if 'history' not in st.session_state:
        st.session_state.history = []
    return st.session_state.history

def add_to_history(text, sentiment, sentiment_score, emotion, emotion_score):
    history = get_sentiment_history()
    history.append({
        "text": text,
        "sentiment": sentiment,
        "sentiment_score": sentiment_score,
        "emotion": emotion,
        "emotion_score": emotion_score,
        "timestamp": time.time()
    })
    st.session_state.history = history


def display_history():
    history = get_sentiment_history()
    if history:
        st.markdown("### Sentiment and Emotion Analysis History")
        for item in reversed(history):
            sentiment_emoji = {"positive": "🟢", "neutral": "🟡", "negative": "🔴"}[item["sentiment"]]
            st.markdown(f"{sentiment_emoji} **Sentiment:** {item['sentiment']} (Score: {item['sentiment_score']:.2f})")
            st.markdown(f"Top Emotion: **{item['emotion']}** (Score: {item['emotion_score']:.2f})")
            st.markdown(f"Text: _{item['text'][:50]}{'...' if len(item['text']) > 50 else ''}_")
            st.markdown(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['timestamp']))}")
            st.markdown("---")
    else:
        st.info("No history available yet. Start analyzing to build your history!")
