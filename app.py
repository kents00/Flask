from flask import Flask, render_template

app = Flask(__name__, template_folder='static')
app.secret_key = "your secret key"

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True, host=localhost, port=5000)
