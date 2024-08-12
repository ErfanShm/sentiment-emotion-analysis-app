from transformers import pipeline

# Initialize the sentiment analysis model pipeline
SENTIMENT_MODEL_NAME = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
SENTIMENT_PIPE = pipeline("text-classification", model=SENTIMENT_MODEL_NAME, top_k=None)

# Initialize the emotion detection model pipeline
EMOTION_MODEL_NAME = "SamLowe/roberta-base-go_emotions"
EMOTION_PIPE = pipeline("text-classification", model=EMOTION_MODEL_NAME , top_k=None)
