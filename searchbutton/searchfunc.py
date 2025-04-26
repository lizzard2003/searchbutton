from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Access data sent from the HTML form safely
        data = request.form.get("data", "")
        # Call your Python function with the data
        result = my_python_function(data)
        return render_template("index.html", result=result)
    return render_template("index.html", result=None)


def my_python_function(data):
    # Process the data and return a result
    return f"Processed: {data}"


if __name__ == "__main__":
    app.run(debug=True)
