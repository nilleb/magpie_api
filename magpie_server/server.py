from flask import render_template

import connexion

app = connexion.App(__name__, specification_dir="./")
app.add_api("swagger.yaml")


@app.route("/")
def home():
    return render_template("home.html")


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == "__main__":
    main()
