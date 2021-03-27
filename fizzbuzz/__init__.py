from flask import Flask


app = Flask(__name__)

from fizzbuzz import routes  # noqa
