from flask import Flask, request
import sqlite3
import json
from flask import g
from ControladorDevices import ControladorDevices
from ControladorDevice import ControladorDevice

app = Flask(__name__)

#************** Manejo de DB ****************************
DATABASE = 'devices.db3'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
#________________________________________________________

@app.route('/')
def hello_world():
	return "<b>url raiz</b>"

@app.route('/devices', methods=['GET'])
def Devices():
	cont = ControladorDevices(app, request, get_db())
	return cont.get()

@app.route('/device/<idRecibido>', methods=['PUT'])
def putID(idRecibido):

    cont = ControladorDevice(app, request, get_db())
    return cont.putID(idRecibido)
    

if __name__ == '__main__':
	app.debug = True
	app.run()
