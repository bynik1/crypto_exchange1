from flask import Flask, request, render_template
import random


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    if request.method == "GET":
        random_cource = str(random.randint(0, 100000000))
        return random_cource
    return "<p>Hello, world!!!</p>"


if __name__ == "__main__":
    #app.secret_key = 'super secret key'
    app.run(debug=True, host="127.0.0.1", port=8777)


#href="/personal-cabinet?url=127.0.0.1:8777"