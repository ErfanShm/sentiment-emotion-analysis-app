import streamlit as st
from transformers import pipeline
import plotly.graph_objects as go
import random
import urllib.parse
import time

# 1. Utility Functions
def classify_text(text):
    result = pipe(text)[0]
    return result

def get_emoji(sentiment):
    if sentiment == "POSITIVE":
        return random.choice(["😊", "😄", "🎉", "👍", "🌟"])
    else:
        return random.choice(["😔", "😢", "👎", "🌧️", "💔"])

def get_fun_fact(sentiment):
    positive_facts = [
        "Did you know? Smiling can boost your mood and immune system!",
        "Optimists tend to live longer than pessimists. Keep up the positivity!",
        "Laughing for 15 minutes burns up to 40 calories. Time for a comedy!",
    ]
    negative_facts = [
        "Chocolate can help improve your mood. Maybe it's time for a treat?",
        "Negative emotions can be useful for problem-solving and critical thinking.",
        "Did you know? Crying can help release stress and improve your mood.",
    ]
    return random.choice(positive_facts if sentiment == "POSITIVE" else negative_facts)

# 2. Visualization Functions
def create_gauge_chart(score, sentiment):
    color = "#00CC96" if sentiment == "POSITIVE" else "#EF553B"
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"Confidence Score {get_emoji(sentiment)}", 'font': {'size': 24}},
        gauge = {
            'axis': {'range': [0, 1], 'tickwidth': 1, 'tickcolor': "#636EFA"},
            'bar': {'color': color},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#636EFA",
            'steps': [
                {'range': [0, 0.5], 'color': '#E8E8E8'},
                {'range': [0.5, 1], 'color': '#D3D3D3'}],
            'threshold': {
                'line': {'color': "#FF97FF", 'width': 4},
                'thickness': 0.75,
                'value': 0.5}}))
    fig.update_layout(height=300, font={'color': "#636EFA", 'family': "Arial"})
    return fig

# 3. New Functionalities
def get_sentiment_history():
    if 'history' not in st.session_state:
        st.session_state.history = []
    return st.session_state.history

def add_to_history(text, sentiment, score):
    history = get_sentiment_history()
    history.append({"text": text, "sentiment": sentiment, "score": score, "timestamp": time.time()})
    st.session_state.history = history

def display_history():
    history = get_sentiment_history()
    if history:
        st.markdown("### Sentiment Analysis History")
        for item in reversed(history):
            sentiment_emoji = "🟢" if item["sentiment"] == "POSITIVE" else "🔴"
            st.markdown(f"{sentiment_emoji} **{item['sentiment']}** (Score: {item['score']:.2f})")
            st.markdown(f"Text: _{item['text'][:50]}{'...' if len(item['text']) > 50 else ''}_")
            st.markdown(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(item['timestamp']))}")
            st.markdown("---")
    else:
        st.info("No history available yet. Start analyzing to build your history!")

# 4. Streamlit App Main Logic
def main():
    st.set_page_config(page_title="Funtime Sentiment Analyzer", page_icon="🎭", layout="wide")
    
    # Custom CSS
    st.markdown("""
    <style>
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        color: #636EFA;
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subheader {
        font-size: 25px;
        font-style: italic;
        color: #636EFA;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton > button {
        background-color: #636EFA;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #00CC96;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
    .info-box {
        border-radius: 12px;
        color: #333333;
        background: linear-gradient(145deg, #f5f5f5, #e0e0e0);
        padding: 20px;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
        font-size: 16px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Funtime Sentiment Analyzer 🎭🎉</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Discover the mood behind your words and have a blast!</p>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.image("https://exemplary.ai/img/blog/sentiment-analysis/sentiment-analysis.svg", use_column_width=True)
        st.markdown("## About")
        st.info("This app uses a machine learning model to classify the sentiment of a given text. Try it out and see how it interprets your words!")
        st.markdown("### How to use:")
        st.write("1. Enter your text in the text area")
        st.write("2. Click 'Analyze Sentiment'")
        st.write("3. See the results and have fun!")
        
        if st.button("View Analysis History"):
            display_history()
    
    user_input = st.text_area("Enter your text here:", height=150, 
                              placeholder="Type or paste your text here... Let's see how it feels! 😊")
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("Analyze Sentiment", key="analyze"):
            if user_input:
                with st.spinner("Analyzing your text... 🕵️‍♂️"):
                    result = classify_text(user_input)
                    sentiment = result['label']
                    score = result['score']
                    
                    add_to_history(user_input, sentiment, score)
                    
                    st.markdown(f"## Sentiment: {sentiment} {get_emoji(sentiment)}")
                    st.plotly_chart(create_gauge_chart(score, sentiment), use_container_width=True)
                    
                    if sentiment == "POSITIVE":
                        st.success(f"Your text has a positive vibe with a confidence score of {score:.2f}!")
                        st.balloons()
                    else:
                        st.error(f"Your text seems a bit negative with a confidence score of {score:.2f}.")
                        st.snow()
                    
                    st.markdown("### Fun Fact", unsafe_allow_html=True)
                    st.markdown(f'<div class="info-box">{get_fun_fact(sentiment)}</div>', unsafe_allow_html=True)
                    
                    tweet_text = f"I just analyzed my text and got a {sentiment.lower()} sentiment with a confidence score of {score:.2f}! Check out this cool Sentiment Analyzer! #SentimentAnalysis #NLP"
                    tweet_text_encoded = urllib.parse.quote(tweet_text)
                    tweet_url = f"https://twitter.com/intent/tweet?text={tweet_text_encoded}"
                    st.markdown(f"[Tweet this result!]({tweet_url})")
            else:
                st.warning("Oops! The text box seems lonely. Give it some words to analyze! 📝😉")

    st.markdown("---")
    st.markdown("### Recent Updates")
    updates = [
        "Added a sentiment analysis history feature",
        "Implemented a view history button in the sidebar",
        "Enhanced the layout and styling of the app",
        "Included timestamps for each analysis in the history",
        "Improved error handling and user feedback"
    ]
    for update in updates:
        st.markdown(f"- {update}")

if __name__ == "__main__":
    # Create a text classification pipeline
    pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
    main()