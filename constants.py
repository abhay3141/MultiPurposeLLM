import streamlit as st
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set your Hugging Face API token
API_TOKEN = st.secrets["API_KEY"]
