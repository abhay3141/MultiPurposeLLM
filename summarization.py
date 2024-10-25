from huggingface_hub import InferenceApi
from constants import API_TOKEN

def summarization(text):
    summarization_api = summarization_api = InferenceApi(repo_id="facebook/bart-large-cnn", token=API_TOKEN)
    result = summarization_api(inputs=text)
    summary_text = result[0]['summary_text']
    return f"**Summary:** {summary_text}"

