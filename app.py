from flask import Flask, request
app = Flask(__name__)
@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise_request/<user>')
def exercise_request(user):
    return f'exercise_request:{user}'


