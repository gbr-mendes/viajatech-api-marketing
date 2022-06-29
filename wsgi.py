import os
from app.main import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    PORT = os.getenv('PORT')
    DEBUG = os.getenv('DEBUG')
    print(f"App listening at port {PORT}...")
    app.run(port=PORT, debug=DEBUG)
