import numpy as np
import tensorflow as tf
from PIL import Image
import io
from app.config import Config

def preprocess_image(file_bytes: bytes) -> tf.Tensor:
    """
    Membaca bytes gambar, resize ke 224x224,
    normalisasi ke [0, 1], dan tambahkan batch dimension.
    """
    image = Image.open(io.BytesIO(file_bytes)).convert("RGB")
    image = image.resize(Config.IMAGE_SIZE)
    image_array = np.array(image, dtype=np.float32) / 255.0
    image_tensor = tf.expand_dims(image_array, axis=0)  # (1, 224, 224, 3)
    return image_tensor
