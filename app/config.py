import os

class Config:
    # Model
    IMAGE_SIZE = (224, 224)
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

    # Labels — sesuaikan urutan dengan output neuron model kamu
    CLASS_LABELS = {
        0: "Medium",
        1: "Premium",
        2: "Rendah"
    }

    # Upload
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
