from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "It's working..."

if __name__ == "__main__":
    port = 3001
    print(f"App listening at port {port}...")
    app.run(debug=True, port=port)
