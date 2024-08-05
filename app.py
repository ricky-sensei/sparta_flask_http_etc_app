from flask import Flask, request

app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def home():
    print(request.method)
    return "login page"


if __name__ == "__main__":
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8000, debug=True)
