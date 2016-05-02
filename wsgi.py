import codecs

from flask import Flask, request
from jeje import jeje

codecs.register(jeje)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def index():
    return request.stream.read().encode("jeje")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
