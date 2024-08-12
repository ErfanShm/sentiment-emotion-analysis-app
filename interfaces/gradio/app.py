import gradio as gr
import urllib.parse
from utils import classify_text, get_emoji, get_fun_fact, analyze_sentiment_emotion, open_tweet_url
from visualization import create_bar_chart
import webbrowser

def main():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
        """
        # 🎭 Funtime Sentiment and Emotion Analyzer
        Discover the mood and emotions behind your words and have a blast!
        """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                text_input = gr.Textbox(
                    label="Enter your text here",
                    placeholder="Type or paste your text here... Let's see how it feels! 😊",
                    lines=5
                )
                analyze_button = gr.Button("Analyze Sentiment and Emotion", variant="primary")
            
            with gr.Column(scale=1):
                sentiment_output = gr.Textbox(label="Top Sentiment")
                detailed_output = gr.Textbox(label="Detailed Sentiment Scores")
                emotion_output = gr.Textbox(label="Top Emotion")
                detailed_emotion_output = gr.Textbox(label="Detailed Emotion Scores")
                plot_output = gr.Plot(label="Sentiment Scores")
                emotion_plot_output = gr.Plot(label="Emotion Scores")
                fun_fact_output = gr.Textbox(label="Fun Fact")
                tweet_url_output = gr.Textbox(label="Share on Twitter", visible=False)
                tweet_button = gr.Button("Share on Twitter! 🐦")
        
        gr.Examples(
            examples=[
                ["I absolutely love this product! It's amazing and has exceeded all my expectations."],
                ["This is the worst experience I've ever had. I'm extremely disappointed and frustrated."],
                ["The weather today is quite pleasant, making it a nice day for a walk in the park."],
                ["I'm feeling a bit under the weather today, but I hope I'll feel better tomorrow."]
            ],
            inputs=text_input,
            outputs=[sentiment_output, detailed_output, emotion_output, detailed_emotion_output, plot_output, emotion_plot_output, fun_fact_output, tweet_url_output],
            fn=analyze_sentiment_emotion,
            cache_examples=True,
        )
        
        analyze_button.click(
            fn=analyze_sentiment_emotion,
            inputs=text_input,
            outputs=[sentiment_output, detailed_output, emotion_output, detailed_emotion_output, plot_output, emotion_plot_output, fun_fact_output, tweet_url_output],
        )
        
        tweet_button.click(
            fn=open_tweet_url,
            inputs=tweet_url_output,
            outputs=tweet_url_output,
        )
    
    demo.launch()

if __name__ == "__main__":
    main()
