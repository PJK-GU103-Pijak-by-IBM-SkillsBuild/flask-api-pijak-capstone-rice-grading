from flask import Blueprint, request, jsonify
import numpy as np
from app.config import Config
from app.model_loader import load_model
from app.preprocessing import preprocess_image

predict_bp = Blueprint("predict", __name__)

def allowed_file(filename: str) -> bool:
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in Config.ALLOWED_EXTENSIONS
    )

@predict_bp.route("/predict", methods=["POST"])
def predict():
    # --- Validasi file ---
    if "image" not in request.files:
        return jsonify({
            "success": False,
            "data": {},
            "message": "Tidak ada file gambar yang dikirim. Gunakan key 'image'."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "success": False,
            "data": {},
            "message": "Nama file kosong."
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "success": False,
            "data": {},
            "message": "Format gambar tidak didukung. Gunakan JPEG atau PNG."
        }), 415

    # --- Preprocessing ---
    try:
        file_bytes = file.read()
        image_tensor = preprocess_image(file_bytes)
    except Exception as e:
        return jsonify({
            "success": False,
            "data": {},
            "message": f"Gagal memproses gambar: {str(e)}"
        }), 422

    # --- Inferensi ---
    try:
        model = load_model()
        output = model(image_tensor)
        # predictions = model(image_tensor, training=False)
        probabilities = list(output.values())[0].numpy()[0]

        predicted_index = int(np.argmax(probabilities))
        label = Config.CLASS_LABELS[predicted_index]
        confidence = round(float(probabilities[predicted_index]), 4)
    except Exception as e:
        return jsonify({
            "success": False,
            "data": {},
            "message": f"Gagal melakukan inferensi: {str(e)}"
        }), 500

    return jsonify({
        "success": True,
        "data": {
            "label": label,
            "confidence": confidence
        },
        "message": "Klasifikasi berhasil dilakukan"
    }), 200


@predict_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "success": True,
        "data": {
            "status": "ok"
        },
        "message": "Inference service berjalan."
    }), 200
