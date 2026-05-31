import numpy as np
from PIL import Image
import io

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)

    # preprocess_input MobileNetV2: normalisasi ke [-1, 1]
    arr = (arr / 127.5) - 1.0
    return arr