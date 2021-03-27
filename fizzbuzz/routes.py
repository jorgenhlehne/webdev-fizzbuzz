from fizzbuzz import app
from flask import request
from fizzbuzz.functions import calculate_fizzbuzz


@app.route('/')
def home():
    return '<h1>Hello world!</h1>'


@app.route('/fizzbuzz')
def fizzbuzz_display():
    args = request.args

    count = 100
    fizzcount = 3
    buzzcount = 5
    fizzname = 'Fizz'
    buzzname = 'Buzz'

    if "count" in args and args["count"].isdigit():
        count = int(args["count"])

    ret = calculate_fizzbuzz(
            count=count,
            fizzcount=fizzcount,
            buzzcount=buzzcount,
            fizzname=fizzname,
            buzzname=buzzname)

    return {'msg': ret}


@app.route('/fizzbuzz/change')
def fizzbuzz_change():
    return 'changing fizzbuzz'
