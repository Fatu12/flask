from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route("/")
def initial_render():
    return redirect("/play")


@app.route("/play")
def level1_box(num=3):
    return render_template("playground.html", number=num)


@app.route("/play/<int:num>")
def level2_box(num):
    return render_template("playground.html", number=num)


@app.route("/play/<int:num>/<string:color>")
def level3_box(num, color):
    return render_template("playground.html", number=num, color=color)


if __name__ == "__main__":
    app.run(debug=True)
