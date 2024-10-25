from huggingface_hub import InferenceApi
from constants import API_TOKEN


#translation from english to french...
def translation(text):
    translation_api = InferenceApi(repo_id="Helsinki-NLP/opus-mt-en-fr", token=API_TOKEN)
    result = translation_api(inputs=text)
    translation_text = result[0]['translation_text']
    return f"**Translation:** {translation_text}"
