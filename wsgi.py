import os
from app.main import create_app
from dotenv import load_dotenv

load_dotenv()

app = create_app()

if __name__ == '__main__':
    PORT = os.getenv('PORT')
    DEBUG = os.getenv('DEBUG')
    print(f"App listening at port {PORT}...")
    app.run(port=PORT, debug=DEBUG)
