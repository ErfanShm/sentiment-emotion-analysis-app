import plotly.graph_objects as go

def create_bar_chart(result):
    # Extract labels and scores from the result
    labels = [item['label'] for item in result]
    scores = [item['score'] for item in result]
    
    # Define colors based on sentiment type
    colors = ['#00CC96' if label == 'positive' else '#EF553B' if label == 'negative' else '#636EFA' for label in labels]

    # Create bar chart
    fig = go.Figure(data=[go.Bar(
        x=labels,
        y=scores,
        marker_color=colors
    )])
    
    # Update layout for better visualization
    fig.update_layout(
        title='Sentiment Scores',
        xaxis_title='Sentiment',
        yaxis_title='Score',
        yaxis=dict(range=[0, 1]),
        font=dict(family="Arial", size=14, color="#636EFA")
    )
    
    return fig

def create_emotion_bar_chart(result):
    # Extract labels and scores from the result
    labels = [item['label'] for item in result]
    scores = [item['score'] for item in result]
    
    # Define a set of colors for the emotions
    colors = ['#FF6692', '#636EFA', '#00CC96', '#EF553B', '#AB63FA', '#FFA15A']

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
        font=dict(family="Arial", size=14, color="#636EFA")
    )
    
    return fig
