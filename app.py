from flask import Flask, render_template
import random

app = Flask(__name__)

# list of gif images - To-Be-Updated
images = []

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
