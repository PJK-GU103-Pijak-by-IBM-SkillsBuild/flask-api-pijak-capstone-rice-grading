import os
from dotenv import load_dotenv
load_dotenv()
from app.factory import create_app


app = create_app()

if __name__ == "__main__":
    app.run(host=f"{os.getenv('HOST')}", port=int(f"{os.getenv('PORT')}"), debug=False)
