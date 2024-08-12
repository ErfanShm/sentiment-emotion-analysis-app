import streamlit as st
import time
import urllib.parse
from config import get_theme_color, sentiment_pipe, emotion_pipe
from utils import classify_text, get_fun_fact, add_to_history, display_history, get_emoji
from visualization import create_bar_chart, create_emotion_bar_chart

def main():
    st.set_page_config(page_title="Funtime Sentiment and Emotion Analyzer", page_icon="🎭", layout="wide")
    
    theme = st.sidebar.selectbox("Choose Theme", ["Normal", "Unnormal", "Fun"])
    primary_color = get_theme_color(theme)
    
    st.markdown(f"""
    <style>
    .big-font {{
        font-size: 50px !important;
        font-weight: bold;
        color: {primary_color};
        text-align: center;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }}
    .subheader {{
        font-size: 25px;
        font-style: italic;
        color: {primary_color};
        text-align: center;
        margin-bottom: 30px;
    }}
    .stButton > button {{
        background-color: {primary_color};
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        border: none;
        cursor: pointer;
        transition: all 0.3s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .stButton > button:hover {{
        background-color: {primary_color};
        opacity: 0.8;
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }}
    .info-box {{
        border-radius: 12px;
        color: #333333;
        background: linear-gradient(145deg, #f5f5f5, #e0e0e0);
        padding: 20px;
        box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.1);
        font-size: 16px;
        margin-top: 20px;
    }}
    .tweet-button {{
        margin-top: 15px;
        background-color: #2413B4;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 18px;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.3s;
        justify-content: center;
        align-items: center;
        text-align: center;
        margin: 0 auto; /* Center horizontally */
    }}
    .tweet-button:hover {{
        background-color: #1991DA;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Funtime Sentiment and Emotion Analyzer 🎭🎉</p>', unsafe_allow_html=True)
    st.markdown('<p class="subheader">Discover the mood behind your words and have a blast!</p>', unsafe_allow_html=True)
    
    if 'tutorial_complete' not in st.session_state:
        st.session_state.tutorial_complete = False

    if not st.session_state.tutorial_complete:
        st.info("Welcome to the Funtime Sentiment and Emotion Analyzer! Let's take a quick tour.")
        step = st.empty()
        
        if st.button("Start Tutorial"):
            for i in range(1, 5):
                if i == 1:
                    step.info("Step 1: Enter your text in the text area below.")
                elif i == 2:
                    step.info("Step 2: Click the 'Analyze Sentiment' button to see the results.")
                elif i == 3:
                    step.info("Step 3: Explore your sentiment history and achievements in the sidebar.")
                else:
                    step.success("Tutorial complete! Enjoy analyzing sentiments and emotions!")
                    st.session_state.tutorial_complete = True
                    step.empty()  # Clear the tutorial step after completion
                    break
                time.sleep(2)
        
        if not st.session_state.tutorial_complete:
            st.stop()  # Stop the script execution until the tutorial is complete

    with st.sidebar:
        st.image("https://exemplary.ai/img/blog/sentiment-analysis/sentiment-analysis.svg", use_column_width=True)
        st.markdown("## About")
        st.info("This app uses AI to analyze the sentiment and emotion of your text. Have fun exploring emotions!")
        
        if st.button("View Analysis History"):
            display_history()
    
    user_input = st.text_area("Enter your text here:", height=150, 
                              placeholder="Type or paste your text here... Let's see how it feels! 😊")
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        if st.button("Analyze Sentiment", key="analyze"):
            if user_input:
                with st.spinner("Analyzing your text... 🕵️‍♂️"):
                    sentiment_result = classify_text(user_input, sentiment_pipe)
                    emotion_result = classify_text(user_input, emotion_pipe)

                    sentiment_result_sorted = sorted(sentiment_result, key=lambda x: x['score'], reverse=True)
                    emotion_result_sorted = sorted(emotion_result, key=lambda x: x['score'], reverse=True)[:6]  # Top 6 emotions

                    top_sentiment = sentiment_result_sorted[0]['label']
                    top_sentiment_score = sentiment_result_sorted[0]['score']
                    top_emotion = emotion_result_sorted[0]['label']
                    top_emotion_score = emotion_result_sorted[0]['score']

                    add_to_history(user_input, top_sentiment, top_sentiment_score, top_emotion, top_emotion_score)
                    
                    st.plotly_chart(create_bar_chart(sentiment_result), use_container_width=True)
                    
                    st.markdown("### All Sentiment Scores")
                    for sentiment in sentiment_result_sorted:
                        st.write(f"{sentiment['label'].capitalize()}: {sentiment['score']:.2f}")
                    
                    if top_sentiment == "positive":
                        st.success(f"Your text has a positive vibe with a confidence score of {top_sentiment_score:.2f}!")
                        st.balloons()
                    elif top_sentiment == "neutral":
                        st.info(f"Your text has a neutral tone with a confidence score of {top_sentiment_score:.2f}.")
                    else:
                        st.error(f"Your text seems a bit negative with a confidence score of {top_sentiment_score:.2f}.")
                        st.snow()

                    st.markdown("---")
                    st.markdown("### Top 6 Emotions")
                    st.plotly_chart(create_emotion_bar_chart(emotion_result_sorted), use_container_width=True)
                    
                    for emotion in emotion_result_sorted:
                        st.write(f"{emotion['label'].capitalize()}: {emotion['score']:.2f}")

                    st.markdown("---")
                    st.markdown("### Fun Fact", unsafe_allow_html=True)
                    st.markdown(f'<div class="info-box">{get_fun_fact(top_sentiment)}</div>', unsafe_allow_html=True)

                    tweet_text = f"I just analyzed my text and got a {top_sentiment} sentiment with a confidence score of {top_sentiment_score:.2f}!\nTop emotion: {top_emotion} with a score of {top_emotion_score:.2f}!\nCheck out this cool Sentiment and Emotion Analyzer! #SentimentAnalysis #EmotionDetection #NLP"
                    tweet_text_encoded = urllib.parse.quote(tweet_text)
                    tweet_url = f"https://twitter.com/intent/tweet?text={tweet_text_encoded}"
                    st.markdown("---")
                    st.markdown(f'<a href="{tweet_url}" target="_blank" class="tweet-button">Tweet this result! 🐦</a>', unsafe_allow_html=True)
            else:
                st.warning("Oops! The text box seems lonely. Give it some words to analyze! 📝😉")

    st.markdown("---")
    st.markdown("### Recent Updates")
    updates = [
        "Added a theme switcher for personalized experience",
        "Implemented an interactive tutorial for new users",
        "Introduced animated transitions for a more dynamic feel",
        "Enhanced the layout and styling of the app",
        "Changed the model to lxyuan/distilbert-base-multilingual-cased-sentiments-student for comprehensive sentiment analysis (positive, negative, and neutral scores).",
        "Added emotion detection feature using SamLowe/roberta-base-go_emotions model."
    ]
    for update in updates:
        st.markdown(f"- {update}")

if __name__ == "__main__":
    main()
