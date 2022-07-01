import os
from app.main import create_app

app = create_app()

if __name__ == '__main__':
    PORT = os.getenv('PORT')
    DEBUG = os.getenv('DEBUG')
    print(f"App listening at port {PORT}...")
    app.run(port=PORT, debug=DEBUG)
