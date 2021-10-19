from flask import Flask, request, render_template
import random


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    if request.method == "GET":
        r = str(random.randint(0, 100000000))
        return r
    return "<p>Hello, world!!!</p>"


if __name__ == "__main__":
    #app.secret_key = 'super secret key'
    app.run(debug=True, host="0.0.0.0", port=8777)