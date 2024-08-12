from transformers import pipeline

def get_theme_color(theme):
    if theme == "Normal":
        return "#636EFA"
    elif theme == "Unnormal":
        return "#00CC96"
    else:  # Fun theme
        return "#FF6692"

# Create a text classification pipeline for sentiment analysis
sentiment_pipe = pipeline("text-classification", model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", top_k=None)

# Create a text classification pipeline for emotion detection
emotion_pipe = pipeline("text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)
