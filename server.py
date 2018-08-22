from flask import Flask, render_template, redirect, request
import data_handler

app = Flask(__name__)


@app.route("/")
def main_page():
    counts = data_handler.get_numbers_from_file()
    return render_template("index.html", counter=counts)


@app.route("/request-counter", methods=["GET", "POST", "PUT", "DELETE"])
def request_counter():
    counts = data_handler.get_numbers_from_file()
    counts[request.method] += 1
    data_handler.write_numbers_to_file(counts)
    return redirect("/")


if __name__ == "__main__":
    app.run()
