# import
import streamlit as st
import pandas as pd
import os
from io import BytesIO
import pyttsx3

st.set_page_config(page_title="Data Sweeper", layout='wide')
st.title("Data Sweeper")
st.write("By cleaning & visualization by transforming of your CSV & Excel files")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"],
accept_multiple_files=True)


# Initialize the pyttsx3 engine for text-to-speech
engine = pyttsx3.init()

# Function to speak the text
def speak_text(text):
    engine.say(text)  # Convert the text to speech
    engine.runAndWait()  # Wait until speech is finished

# Streamlit app
def main():
    
        # Call the function to speak the text aloud
        speak_text("By cleaning & visualization by transforming of your CSV & Excel files")

# Run the Streamlit app
if __name__ == "__main__":
    main()