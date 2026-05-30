import os

class Config:
    # Model
    MODEL_PATH = os.getenv("MODEL_PATH", "app/model/rice_grading")
    IMAGE_SIZE = (224, 224)
    ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}

    # Labels — sesuaikan urutan dengan output neuron model kamu
    CLASS_LABELS = ["Arborio", "Basmati", "Ipsala"]

    # Upload
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB
