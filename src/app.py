from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world!"

@app.route("/index2")
def indexTwo():
    return "Httlo"

if __name__ == "__main__":
    app.run()