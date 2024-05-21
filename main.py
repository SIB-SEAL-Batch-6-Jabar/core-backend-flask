from flask import Flask
from app.blueprint import Blueprint
from app.config import HTTPResponse, ErrorHandler

app = Flask(__name__, static_folder=None)

ErrorHandler.registerErrorHandler(app)

Blueprint.register(app)


@app.route("/")
def hello():
    return HTTPResponse.success("Hello, World!")


if __name__ == "__main__":
    app.run(debug=False)
