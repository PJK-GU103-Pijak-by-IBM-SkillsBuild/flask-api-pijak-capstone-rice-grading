import numpy as np
from PIL import Image
import io
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)
    return arr