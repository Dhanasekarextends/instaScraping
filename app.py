from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    return "hello world"

if __name__ == "__main__":
    app.run()


