from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() :
    return "Helloworld"

if __name__ == "_main_":
    app.run()