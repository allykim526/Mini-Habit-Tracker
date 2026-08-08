"""Flask entry point for the Firebase Mini Habit Tracker."""

from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    """Render the one-page habit tracker."""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
