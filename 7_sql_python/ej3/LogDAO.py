from datetime import datetime

class LogDAO:

    def __init__(self, db):
        self.db = db
        self.c = self.db.cursor()

    def getAll(self, page, size):
        self.c.execute("select * from Log limit ?,?", (page*size, size))
        datos = self.c.fetchall()
        return datos 


    def add(self, idDevice, status):
        
        try:
            timestamp = datetime.now()
            paramsSQL_tupla = (idDevice, status, timestamp)
            self.c.execute("insert into Log(id_dev, status, ts) values(?, ?, ?)", paramsSQL_tupla)
            self.db.commit()
            return True

        except:
            return False      
