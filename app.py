from flask import Flask, render_template, request
import random

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
    app.run()
