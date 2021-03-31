from fizzbuzz import app, db
from flask import request
from fizzbuzz.functions import calculate_fizzbuzz
from fizzbuzz.models import Variables


@app.route('/')
def home():
    return '<h1>Hello world!</h1>'


@app.route('/fizzbuzz')
def fizzbuzz_display():
    args = request.args

    count = 100
    fizz_count = 3
    buzz_count = 5
    fizz_name = 'Fizz'
    buzz_name = 'Buzz'

    db_variables = db.session.query(Variables).filter_by(id=1).first()
    if db_variables:
        if db_variables.fizz_count:
            fizz_count = db_variables.fizz_count
        if db_variables.buzz_count:
            buzz_count = db_variables.buzz_count
        if db_variables.fizz_name:
            fizz_name = db_variables.fizz_name
        if db_variables.buzz_name:
            buzz_name = db_variables.buzz_name

    if "count" in args and args["count"].isdigit():
        count = int(args["count"])

    ret = calculate_fizzbuzz(
            count=count,
            fizz_count=fizz_count,
            buzz_count=buzz_count,
            fizz_name=fizz_name,
            buzz_name=buzz_name)

    return {'msg': ret}


@app.route('/fizzbuzz/change')
def fizzbuzz_change():
    args = request.args

    db_variables = db.session.query(Variables).filter_by(id=1).first()
    new_db_model = False
    if not db_variables:
        db_variables = Variables()
        new_db_model = True

    if "fizz_count" in args and args["fizz_count"].isdigit():
        db_variables.fizz_count = int(args["fizz_count"])
    if "buzz_count" in args and args["buzz_count"].isdigit():
        db_variables.buzz_count = int(args["buzz_count"])
    if "fizz_name" in args:
        db_variables.fizz_name = args["fizz_name"]
    if "buzz_name" in args:
        db_variables.buzz_name = args["buzz_name"]

    if new_db_model:
        db.session.add(db_variables)

    db.session.commit()

    return {'msg': 'changing fizzbuzz'}, 200
