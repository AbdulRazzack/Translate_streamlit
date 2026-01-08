# Translate_streamlit
Translation for English, German, French, Romanian
# T5-Base Streamlit Translator

A simple, local neural machine translation app built with Python, Streamlit, and Hugging Face's T5-Base model. This application allows users to translate text between English, German, French, and Romanian.

## Features
- **Model:** Google's T5-Base (Text-to-Text Transfer Transformer).
- **Interface:** Streamlit Web UI.
- **Languages Supported:** English, German, French, Romanian.
- **Optimization:** Uses Streamlit caching to prevent reloading the model on every interaction.

## Prerequisites
- Python 3.8 or higher

## Installation

1. **Clone the repository** (or ensure you are in the project directory containing `app.py`).

2. **Set up a virtual environment (Recommended)**
   It is best practice to run this in a virtual environment to avoid conflicting library versions.
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Installing the required python packages in requirements.txt**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Streamlit App Execute the following command in your terminal:**
   ```bash
   streamlit run app.py
   ```
2. Access the App Streamlit will automatically open the application in your default web browser. If it does not, navigate to the URL shown in the terminal (usually http://localhost:8501).

3. First Run Note When you run the app for the first time, it will download the T5-Base model (approx. 890MB). This happens only once; subsequent runs will use the cached model.
