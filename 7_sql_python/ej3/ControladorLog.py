import sqlite3
import json
from LogDAO import LogDAO
from Log import Log

class ControladorLog:

    def __init__(self, app, request, db):
        self.app = app
        self.request = request
        self.db = db

    def getPage(self):
        
        logDAO = LogDAO(self.db)
        
        # el segundo parametro del get es el valor default
        pag = int(self.request.args.get('page', '0'))
        siz = int(self.request.args.get('size', '0'))
        
        paginaLog = logDAO.getAll(pag, siz)
        jsonData = json.dumps(paginaLog, default = Log.encode_log)
        
        
        respuesta = self.app.response_class(
            response = jsonData,
            status = 200,
            mimetype = 'application/json')

        return respuesta
                          
