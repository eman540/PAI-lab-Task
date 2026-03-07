from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Home route to serve HTML
@app.route('/')
def home():
    return render_template("index.html")

# API route for random joke
@app.route('/joke', methods=['GET'])
def get_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = response.json()
        joke = {"setup": data.get("setup"), "punchline": data.get("punchline")}
        return jsonify(joke)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)