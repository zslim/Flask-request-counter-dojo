from flask import Flask, render_template, redirect

app = Flask(__name__)
counts = 0


@app.route("/")
def main_page():
    global counts
    return render_template("index.html", counter=counts)


@app.route("/request-counter")
def request_counter():
    global counts
    counts += 1
    return redirect("/")


if __name__ == "__main__":
    app.run()
