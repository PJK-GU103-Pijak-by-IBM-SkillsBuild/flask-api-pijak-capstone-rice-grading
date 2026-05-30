import tensorflow as tf
import os
from huggingface_hub import hf_hub_download

_model = None

def load_model():
    global _model
    if _model is None:
        print("Downloading model from HuggingFace Hub...")
        model_path = hf_hub_download(
            repo_id=f"{os.getenv('REPO_ID')}",
            filename=f"{os.getenv('MODEL_FILENAME')}"
        )
        _model = tf.keras.models.load_model(model_path)
        print("Model loaded!")
    return _model