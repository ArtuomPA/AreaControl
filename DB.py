import sqlite3

class DB:
    def __init__(self):
        self._conn = ''
        self._cursor = ''
        
    def connect(self):
        self._conn = sqlite3.connect('Coordinates.sqlite')
        self._cursor = self._conn.cursor()
    
    def vrite(self, coordinates, delta, cam):
        if coordinates==None:
            x = 'Null'
            y = 'Null'
        else:
            x = coordinates[0]
            y = coordinates[1]
        self._cursor.execute("insert into Coordinates values (Null, '"+str(x)+"', '"+str(y)+"', '"+str(delta)+"', '"+str(cam)+"')")
    
    def disconnect(self):
        self._conn.close()
        
    def commit(self):
        self._conn.commit()
