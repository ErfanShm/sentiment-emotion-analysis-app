import gradio as gr
from transformers import pipeline
import random
import plotly.graph_objects as go

# Create a text classification pipeline
pipe = pipeline("text-classification", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

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
    fig.update_layout(height=300, width=400, margin=dict(l=20, r=20, t=50, b=20))
    return fig

def classify_text_gradio(text):
    result = pipe(text)[0]
    sentiment = result['label']
    score = result['score']
    
    gauge_chart = create_gauge_chart(score, sentiment)
    
    fun_fact = get_fun_fact(sentiment)
    
    return (
        f"{sentiment} {get_emoji(sentiment)}",
        f"{score:.2f}",
        gauge_chart,
        fun_fact
    )

def main():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
        """
        # 🎭 Funtime Sentiment Analyzer
        Discover the mood behind your words and have a blast!
        """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                text_input = gr.Textbox(
                    label="Enter your text here",
                    placeholder="Type or paste your text here... Let's see how it feels! 😊",
                    lines=5
                )
                analyze_button = gr.Button("Analyze Sentiment", variant="primary")
            
            with gr.Column(scale=1):
                with gr.Row():
                    sentiment_output = gr.Textbox(label="Sentiment")
                    score_output = gr.Textbox(label="Confidence Score")
                plot_output = gr.Plot(label="Sentiment Gauge")
                fun_fact_output = gr.Textbox(label="Fun Fact")
        
        gr.Examples(
            examples=[
                ["I absolutely love this product! It's amazing and has exceeded all my expectations."],
                ["This is the worst experience I've ever had. I'm extremely disappointed and frustrated."],
                ["The weather today is quite pleasant, making it a nice day for a walk in the park."],
                ["I'm feeling a bit under the weather today, but I hope I'll feel better tomorrow."]
            ],
            inputs=text_input,
            outputs=[sentiment_output, score_output, plot_output, fun_fact_output],
            fn=classify_text_gradio,
            cache_examples=True,
        )
        
        analyze_button.click(
            fn=classify_text_gradio,
            inputs=text_input,
            outputs=[sentiment_output, score_output, plot_output, fun_fact_output],
        )
    
    demo.launch()

if __name__ == "__main__":
    main()