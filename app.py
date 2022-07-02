from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from test_model import Person
from test_model import Human
from sqlalchemy import or_

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def inex():
    return 'Response Data'

@app.route('/another')
def another():
    return 'Another Response'

@app.route('/test_request')
def test_request():
    return f'test_request:{request.args.get("dummy")}'


@app.route('/exercise request/<user_name>')
def test_sample(user_name):
    return user_name

@app.route('/show_html')
def show_html():
    return render_template('test_html.html')

@app.route('/exercise_html')
def exercise_html():
    return render_template('exercise.html')

@app.route('/answer')
def answer_html():
    result = request.args.get("my_name")
    return render_template('answer.html',name=result)

@app.route('/try_rest',methods=['POST'])
def try_rest():
    #リクエストデータをJSONとして受け取る
    request_json = request.get_json()
    print(request_json)
    print(type(request_json))
    name = request_json['name']
    print(name)
    response_json = {"response_json":request_json}
    return jsonify(response_json)

@app.route('/person_search')
def person_search():
    return render_template('./person_search.html')

@app.route('/person_result')
def person_result():
    search_size = request.args.get("search_size")
    persons = db.session.query(Person).filter(Person.size > search_size)
    return render_template('./person_result.html', persons=persons, search_size=search_size)


@app.route('/human_search')
def human_search():
    return render_template('./human_search.html')

@app.route('/human_result')
def human_result():
    search_height = request.args.get("search_height")
    search_weight = request.args.get("search_weight")
    humans = db.session.query(Human).filter(or_(Human.height >= search_height,Human.weight >= search_weight))
    return render_template('./human_result.html', humans=humans, search_height=search_height,search_weight=search_weight)



@app.route('/try_html')
def try_html():
    return render_template('./try_html.html')


@app.route('/show_data', methods=["GET", "POST"])
def show_data():
    text = request.form.get('text_input')
    return render_template('/show_data.html',text_input=text) 