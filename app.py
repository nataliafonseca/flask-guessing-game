import os
import random

from flask import Flask, render_template, request

app = Flask(__name__)

title = "Adivinhe o numero"
min_value = 1
max_value = 5


@app.route("/")
def index():
    return render_template(
        "index.html", title=title, min_value=min_value, max_value=max_value
    )


@app.route("/result", methods=["POST"])
def result():
    number = random.randint(min_value, max_value)
    guess = int(request.form.get("guess"))
    match = number == guess
    return render_template(
        "result.html", title=title, number=number, guess=guess, match=match
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()
