from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my new Website! Create a Website from python is greate experience for me"

app.run(host='0.0.0.0')
