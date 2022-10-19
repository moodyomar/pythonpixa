from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    word = request.args.get('search')
    return render_template("index.html",searchedWord=word)

@app.route('/<word>')
def stringify(word):
    return f'<h1>{word}? what are you trying to do?</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=3000,debug=True)