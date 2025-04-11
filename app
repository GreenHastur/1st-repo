from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Witaj ze świata Render!"

if __name__ == '__main__':
    app.run(debug=True)
