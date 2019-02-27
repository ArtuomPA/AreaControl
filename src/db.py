#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import sys


class DB:
    def __init__(self):
        self._conn = ''
        self._cursor = ''

    def connect(self):
        self._conn = sqlite3.connect(sys.path[0]+"/../coordinates.sqlite")
        self._cursor = self._conn.cursor()

    def vrite(self, coordinates, delta, cam, Oid):
        if coordinates==None:
            x = 'Null'
            y = 'Null'
        else:
            x = coordinates[0]
            y = coordinates[1]
        self._cursor.execute("insert into Coordinates values (Null, '"
                                    +str(x)+"', '"+str(y)+"', '"+str(delta)
                                    +"', '"+str(cam)+"', '"+str(Oid)+"')")

    def disconnect(self):
        self._conn.close()

    def commit(self):
        self._conn.commit()
