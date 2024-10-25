from huggingface_hub import InferenceClient
from constants import API_TOKEN
client = InferenceClient(token=API_TOKEN)


# Define specialized LLM functions
def sentiment_analysis(text):
    response = client.text_classification(
        text=text,
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )
    label = response[0]['label']
    score = response[0]['score']
    return f"**Sentiment:** {label} (Score: {score:.2f})"
