import numpy as np
import os
from huggingface_hub import hf_hub_download

_interpreter = None

def load_model():
    global _interpreter
    if _interpreter is None:
        print("Downloading model from HuggingFace Hub...")
        model_path = hf_hub_download(
            repo_id=f"{os.getenv('REPO_ID')}",
            filename=f"{os.getenv('MODEL_FILENAME')}"  # ganti ke .tflite
        )

        from ai_edge_litert import interpreter as tflite
        _interpreter = tflite.Interpreter(model_path=model_path)
        _interpreter.allocate_tensors()
        print("Model loaded!")
    return _interpreter