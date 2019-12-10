from flask import Flask
app = Flask(__name__)

@app.route('/prueba')
def hello_world():
    return 'test flask'
    
@app.route('/test2')
def hola():
    return "q onda"    
