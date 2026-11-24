
from flask import Flask, render_template, request
import re

app = Flask(__name__)

def analyze_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        feedback.append("Add a special character.")

    levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]

    return {
        "score": score,
        "strength": levels[score],
        "feedback": feedback
    }


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        password = request.form.get("password", "")
        result = analyze_password(password)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
