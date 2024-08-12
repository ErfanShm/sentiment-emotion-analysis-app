#!/bin/bash

echo "Starting script..."

# Check if Conda is installed
if ! command -v conda &> /dev/null
then
    echo "Error: Conda is not installed or not in PATH. Please install it and try again."
    exit 1
fi

ENV_NAME="sentiment_analysis"

# Function to check if the environment exists and create it if it doesn't
check_and_create_env() {
    if conda env list | grep -q "$ENV_NAME"; then
        echo "Conda environment '$ENV_NAME' already exists. Activating..."
        eval "$(conda shell.bash hook)"
        conda activate "$ENV_NAME"
    else
        echo "Creating new Conda environment: $ENV_NAME"
        conda create -n "$ENV_NAME" python=3.8 -y
        if [ $? -ne 0 ]; then
            echo "Error: Failed to create environment '$ENV_NAME'."
            exit 1
        fi
        eval "$(conda shell.bash hook)"
        conda activate "$ENV_NAME"
    fi
}

# Check/create and activate the environment
check_and_create_env

# Verify activation
if conda env list | grep -q "$ENV_NAME"; then
    echo "Conda environment '$ENV_NAME' activated successfully."
else
    echo "Error: Failed to activate environment '$ENV_NAME'."
    exit 1
fi

echo "Setup completed successfully."

# Main menu
menu() {
    while true; do
        echo "Sentiment Analysis Tool"
        echo "======================="
        echo "1. Run with Streamlit interface"
        echo "2. Run with Gradio interface"
        echo "3. Update dependencies"
        echo "4. Exit"
        read -p "Enter your choice (1-4): " choice

        case $choice in
            1)
                echo "Running sentiment analysis with Streamlit interface..."
                streamlit run interfaces/streamlit/app.py
                echo "Press Enter to return to the menu."
                read
                ;;
            2)
                echo "Running sentiment analysis with Gradio interface..."
                python interfaces/gradio/app.py
                echo "Press Enter to return to the menu."
                read
                ;;
            3)
                echo "Updating dependencies..."
                if [ -f requirements.txt ]; then
                    echo "Installing/upgrading dependencies from requirements.txt..."
                    conda install -y pytorch==2.0.1 -c pytorch
                    pip install -r requirements.txt
                    if [ $? -ne 0 ]; then
                        echo "Error: Failed to install dependencies."
                        exit 1
                    fi
                else
                    echo "Error: requirements.txt file not found."
                    exit 1
                fi
                echo "Dependencies updated."
                ;;
            4)
                echo "Exiting..."
                conda deactivate
                exit 0
                ;;
            *)
                echo "Invalid choice. Please try again."
                ;;
        esac
    done
}

# Show the menu
menu
