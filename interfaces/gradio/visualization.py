import plotly.graph_objects as go

def create_bar_chart(result):
    labels = [item['label'] for item in result]
    scores = [item['score'] for item in result]
    colors = ['#00CC96' if label == 'positive' else '#EF553B' if label == 'negative' else '#636EFA' for label in labels]

    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=scores,
        marker_color=colors
    )])
    fig.update_layout(
        title='Sentiment Scores',
        xaxis_title='Sentiment',
        yaxis_title='Score',
        yaxis=dict(range=[0, 1])
    )
    return fig

def create_emotion_bar_chart(result):
    # Extract labels and scores from the result
    labels = [item['label'] for item in result]
    scores = [item['score'] for item in result]
    
    # Define a set of creative and vibrant colors for the emotions
    colors = ['#FF6347', '#FFD700', '#4CAF50', '#00BFFF', '#FF69B4', '#8A2BE2']  # Tomato, Gold, Green, Deep Sky Blue, Hot Pink, Blue Violet

    # Create bar chart
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=scores,
        marker_color=colors[:len(labels)]  # Assign colors to the bars
    )])
    
    # Update layout for better visualization
    fig.update_layout(
        title='Top 6 Emotions',
        xaxis_title='Emotion',
        yaxis_title='Score',
        yaxis=dict(range=[0, 1]),
        font=dict(family="Arial", size=14, color="#2D3E50")  # Dark Blue Gray for text
    )
    
    return fig