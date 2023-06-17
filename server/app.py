#!/usr/bin/env python3
from flask import Flask

app = Flask(__name__)

# @app.route('/')
# def index():
#     return ('Hello, World!')

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    print(parameter)
    return parameter

# the implementation is not working i dont know why 
# because the test is expecting the response to include the number 10 but the actual response includes the number 10 twice at the end 
# this test is yet to pass will work on it later
@app.route('/count/<int:parameter>')
def count_route(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter)) 
    numbers += f"\n{parameter - 1}"  
    return numbers


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math_route(num1, operation, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
