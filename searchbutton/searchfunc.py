# This is the begining of a search button

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        data = request.form.get("data", "")
        # Call your Python function with the data
        result = my_python_function(data)
        return render_template("index.html", result=result)  # pulls frm html
    return render_template("index.html", result=None)


def my_python_function(data):
    # Process the data and return a result
    return f"Processed: {data}"


if __name__ == "__main__":
    app.run(debug=True)
