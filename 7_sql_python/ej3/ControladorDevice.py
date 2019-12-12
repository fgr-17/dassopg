import json
from ControladorLog import ControladorLog
from DeviceDAO import DeviceDAO
from LogDAO import LogDAO

class ControladorDevice:

    def __init__(self, app, request, db):
        self.app = app
        self.request = request
        self.db = db
        
        
    def putID(self, idDevice):
    
        devDAO = DeviceDAO(self.db)

        stateRecibido = self.request.form.get("state")
    
        if devDAO.setState(idDevice, stateRecibido) == True :
            log = LogDAO(self.db)
            if(log.add(idDevice, stateRecibido) == True):
                ret = "OK"
            else:
                ret = "ERROR"
        else:
            ret = "ERROR"
    
        respuesta = self.app.response_class(
                    response = json.dumps({"state":ret}),
                    status = 200,
                    content_type = 'application/json')    
        
        return respuesta                   
        
