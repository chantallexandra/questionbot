from flask import Flask, json, request
from flask_cors import CORS
from textblob import TextBlob
from server.bot import Bot
from utilities.yes_no_trainer import PosOrNeg

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    data = {
        "question": "What are the pizza restaurants in Boston",
        "answer": ["Pizza Hut", "Pizza Pizza", "Little Cesears"]
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/question')
def question():
    sentence = request.args.get("question").lower()
    answer = Bot(sentence)
    query, columns = answer.generate_query()
    print(query, columns)
    print(answer.get_response(query))
    data = {
        "question": sentence,
        "columns": columns,
        "query": query,
        "answer": answer.get_response(query)
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/spellcheck')
def spellcheck():
    input = TextBlob(request.args.get("spell"))
    data = {
        "input": input.lower().raw,
        "output": input.lower().correct().raw,
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/yesorno')
def yesorno():
    input = request.args.get("text").lower()
    cl = PosOrNeg();
    data = {
        "input": input,
        "response": cl.classify(input),
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response



app.run('0.0.0.0', debug=True)