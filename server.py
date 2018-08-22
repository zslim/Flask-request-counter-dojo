from flask import Flask, render_template, redirect, request

app = Flask(__name__)
counts = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0}


@app.route("/")
def main_page():
    global counts
    return render_template("index.html", counter=counts)


@app.route("/request-counter", methods=["GET", "POST", "PUT", "DELETE"])
def request_counter():
    global counts
    counts[request.method] += 1
    return redirect("/")


if __name__ == "__main__":
    app.run()
