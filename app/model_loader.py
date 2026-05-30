import tensorflow as tf
from app.config import Config

_model = None

def load_model():
    global _model
    if _model is None:
        print(f"[Model] Loading from: {Config.MODEL_PATH}")
        loaded = tf.saved_model.load(Config.MODEL_PATH)
        _model = loaded.signatures["serving_default"]
        print("[Model] Loaded successfully.")
    return _model
