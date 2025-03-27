#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        output = num1 + num2

    elif operation == '-':
        output = num1 - num2

    elif operation == '*':
        output = num1 * num2

    elif operation == 'div':
        output = num1 / num2

    elif operation == '%':
        output = num1 % num2

    else:
        output = 'Please use "+", "-", "*", "div", or "%" as the operation'

    return str(output)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
