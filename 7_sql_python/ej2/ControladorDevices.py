import json 
from DeviceDAO import DeviceDAO
from Device import Device

class ControladorDevices():
    
    def __init__ (self, app, request, db):
        self.app = app
        self.request = request
        self.db = db
    
    def get(self):
        
        devDAO = DeviceDAO(self.db)
        
        listaDevices = devDAO.getAll()
        
        jsonData = json.dumps(listaDevices, default = Device.encodeDevice)
        
        respuesta = self.app.response_class(
            response = jsonData,
            status = 200,
            mimetype = 'application/json')

        return respuesta        
