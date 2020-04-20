from flask import *

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("mainpage.html")


@app.route("/<name>", methods=["GET", "POST"])
def namepage(name):
    return render_template("name.html", name=name)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
