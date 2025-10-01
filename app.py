from flask import Flask, render_template, request

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if any(char in "!@#$%^&*()-_=+[]{};:,.<>?/" for char in password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")

    return strength, feedback

@app.route("/", methods=["GET", "POST"])
def index():
    strength = None
    feedback = []
    if request.method == "POST":
        password = request.form.get("password")
        strength, feedback = check_password_strength(password)
    return render_template("index.html", strength=strength, feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
