from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.routes import predict_bp
from app.model_loader import load_model

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Izinkan request dari Hapi.js (localhost:3000)
    CORS(app, resources={r"/*": {"origins": "*"}})
    # CORS(app, resources={
    #     r"/api/v1/*": {
    #         "origins": ["http://localhost:3000", "http://localhost:5500"]
    #     },
    #     r"/docs/*": {
    #         "origins": ["http://localhost:5500"]
    #     }
    # })

    # Load model saat startup
    with app.app_context():
        load_model()

    # Register blueprint
    app.register_blueprint(predict_bp, url_prefix="/api/v1")

    return app
