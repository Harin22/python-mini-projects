from flask import Flask, render_template, request 
import secrets
import string

app = Flask(__name__)

def generate_password(length, upper, lower, digits, symbols):
    characters = ""
    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Select at least one character type!"

    return "".join(secrets.choice(characters) for _ in range(length))

@app.route("/", methods=["GET", "POST"])
def index():
    password = ""
    if request.method == "POST":
        length = int(request.form.get("length", 12))
        upper = request.form.get("upper") is not None
        lower = request.form.get("lower") is not None
        digits = request.form.get("digits") is not None
        symbols = request.form.get("symbols") is not None

        # Pass the correct variables to generate_password
        password = generate_password(length, upper, lower, digits, symbols)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
