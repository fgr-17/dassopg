from flask import Flask
from flask import url_for
app = Flask(__name__)

@app.route('/prueba')
def hello_world():
    return 'test flask2'


with app.test_request_context():
    print(url_for('static', filename='archivo.txt'))

