import sqlite3

class DeviceDAO ():

    def __init__(self, db):
        self.db = db
        self.c = self.db.cursor()
        
        
    def getAll(self):
        self.c.execute("select * from Devices")
        datos = self.c.fetchall()
        return datos 
        
    def addDevice(self, name, ip, state):
        
        try:
            paramsSQL_tupla = (name, ip, status)
            self.c.execute("insert into Devices (name, ip, status) values(?, ?, ?)", paramsSQL_tupla)
            self.db.commit()
            return True

        except:

            return False        
        

    
    def setState(self, idDevice, state):
            
        try:
            paramsSQL_tupla = (state, idDevice)                  
            idTupla = tuple(idDevice)
            self.c.execute("select * from Devices where id = ?", idTupla)    

            if(len(self.c.fetchall()) == 0):
                return False
            else:
                self.c.execute("update Devices set status = ? where id = ?", paramsSQL_tupla)
                self.db.commit()
                return True
        except:
            return False
    
        
    
            
