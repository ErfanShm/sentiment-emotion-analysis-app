# Practical Sentiment and Emotion Analysis with DistilBERT and RoBERTa

Welcome to the Sentiment and Emotion Analysis Application repository! This guide provides a detailed overview of how to run a sentiment and emotion analysis tool using both Streamlit and Gradio interfaces. This project demonstrates how to integrate advanced AI models with user-friendly interfaces for practical natural language processing tasks.

- **Script Folder:** This repository contains the scripts required to run the sentiment and emotion analysis application with both Streamlit and Gradio.

## Overview

This application utilizes the `distilbert-base-multilingual-cased-sentiments-student` model for sentiment analysis and the `roberta-base-go_emotions ` model for emotion detection. The sentiment analysis covers three categories: positive, negative, and neutral, while the emotion detection identifies the top six emotions with corresponding scores.

The application provides two interfaces:

- **Streamlit Interface**: For a web-based interactive experience with additional features.
- **Gradio Interface**: For a quick and easy web-based demo with suggestion capabilities.

This guide covers:

- **Prerequisites**: Necessary tools and software.
- **Installation Instructions**: How to set up your environment.
- **Running the Application**: Detailed commands to launch either interface.
- **Troubleshooting**: Common issues and their solutions.
- **Contribution Guidelines**: How to contribute to the project.
- **Additional Resources**: Links for further reading.

## Prerequisites

Before you begin, ensure you have the following tools installed on your system:

1. **Conda**: Follow the instructions on the [Miniconda installation page](https://docs.conda.io/en/latest/miniconda.html) to install Conda.
2. **Bash**: Bash is typically included with Unix-based systems (Linux, macOS). For Windows users, consider using Git Bash or the Windows Subsystem for Linux (WSL).

## Installation Instructions

Follow these steps to set up your environment and install the necessary packages:

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/sentiment-analysis-app.git
   cd sentiment-analysis-app
   ```

2. **Run the Setup Script**

   The `setup_environment.sh` script automates the environment setup process. It creates and activates a Conda environment, installs necessary packages, and provides options to run the application using Streamlit or Gradio.

   ```bash
   bash setup_environment.sh
   ```

   The script will prompt you with a menu to choose between the following options:
   - Run with Streamlit interface
   - Run with Gradio interface
   - Update dependencies
   - Exit

   Choose the appropriate option to proceed.

## Running the Application

You can run the application using the provided script:

### Launch Streamlit Interface

To run the application with Streamlit, select the Streamlit interface option from the setup script menu, or use the following command:

```bash
python run_sentiment_analysis.py --interface streamlit
```

This will start a local Streamlit server and open your default web browser to view the application. The Streamlit interface includes:
- **Theme Selection**: Choose between Normal, Unnormal, or Fun themes.
- **Sentiment and Emotion History**: View past sentiment and emotion analyses.
- **Interactive Tutorial**: Get a guided tour of the application.
- **Animated Transitions**: Experience dynamic visual effects for sentiment scores.
- **Twitter Sharing**: Share your analysis results directly on Twitter.
- **Visualization**: Displays sentiment and emotion scores using colorful bar charts.

### Launch Gradio Interface

To run the application with Gradio, select the Gradio interface option from the setup script menu, or use the following command:

```bash
python run_sentiment_analysis.py --interface gradio
```

This will start a local Gradio server and open your default web browser to view the application. The Gradio interface features:
- **Twitter Sharing**: Share your analysis results directly on Twitter.
- **Visualization**: Displays sentiment and emotion scores using bar charts.
- **Suggestion Options**: Offers pre-prepared text options that users can pick from to facilitate analysis.

## Troubleshooting

- **Streamlit Command Not Found**: Ensure Streamlit is installed correctly. Verify by running `streamlit --version`.
- **Gradio Command Not Found**: Ensure Gradio is installed correctly. Verify by running `pip show gradio`.
- **Environment Activation**: Ensure the Conda environment is activated with `conda activate sentiment_analysis`.

If you encounter issues, verify that you are in the correct directory and that all dependencies are installed.

## Contributing

Contributions to enhance this application are welcome! If you have suggestions, improvements, or additional features, please feel free to open an issue or create a pull request. Let's collaborate to make this tool even more useful for sentiment and emotion analysis.

## Additional Resources

Explore additional resources to deepen your understanding of sentiment and emotion analysis and the tools used:

- [Hugging Face Transformers Documentation](https://huggingface.co/transformers/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Gradio Documentation](https://gradio.app/docs/)
- [DistilBERT Model Overview](https://huggingface.co/lxyuan/distilbert-base-multilingual-cased-sentiments-student)
- [RoBERTa Model Overview](https://huggingface.co/SamLowe/roberta-base-go_emotions)

## License

The content in this repository is licensed under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute the code, provided you include the original copyright notice and license.

---

© 2024 Erfan Shafiee Moghaddam