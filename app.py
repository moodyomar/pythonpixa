from flask import Flask, render_template, request
from utils import apiReq, api

app = Flask(__name__)


@app.route('/')
def index():
    query = request.args.get('query')
    print(f'app query is: {query}')
    if query is None:
        query == api['query']
    else:
        api['query'] = query
        
    data = apiReq(query)
    return render_template("index.html", data=data, arrayLen=len(data))

@app.route('/<word>')
def stringify(word):
    return f'<h1>{word}? what are you trying to do?</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
