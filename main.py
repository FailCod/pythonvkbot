from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Ku</h1>'

@app.route('/bot', methods=['GET', 'POST'])
def main():
	content = request.get_json()
    return str(content)

if __name__ == '__main__':
    app.run()