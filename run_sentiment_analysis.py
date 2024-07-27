import subprocess
import os
import sys

def launch_streamlit():
    subprocess.run(["streamlit", "run", "interfaces/streamlit_interface.py"])

def launch_gradio():
    import interfaces.gradio_interface as gradio_interface
    gradio_interface.main()

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in ['streamlit', 'gradio']:
        print("Usage: python run_sentiment_analysis.py [streamlit|gradio]")
        sys.exit(1)

    interface = sys.argv[1]

    if interface == 'streamlit':
        launch_streamlit()
    elif interface == 'gradio':
        launch_gradio()