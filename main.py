import codecs

from flask import Flask, request
from jeje import jeje

codecs.register(jeje)

app = Flask(__name__)


@app.route("/")
def index():
    return request.args.get("m", "").encode("jeje")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
