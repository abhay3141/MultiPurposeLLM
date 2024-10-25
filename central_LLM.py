from huggingface_hub import InferenceClient
import streamlit as st
from constants import API_TOKEN

client = InferenceClient(token=API_TOKEN)


def central_router(prompt):
    candidate_labels = ['translation', 'sentiment analysis', 'summarization']
    response = client.zero_shot_classification(
        text=prompt,
        labels=candidate_labels,
        model="facebook/bart-large-mnli"
    )
    # print(response.dtype)
    task = response[0]['label']  # Get the label with the highest score
    
    # Map the task to function names
    if task == 'translation':
        return 'translation'
    elif task == 'sentiment analysis':
        return 'sentiment_analysis'
    elif task == 'summarization':
        return 'summarization'
