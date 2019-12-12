import sqlite3
import sys


if(len(sys.argv) < 2):
    print("uso: python3 ./ej1.py <<path base de datos>>")
    exit()

conn = sqlite3.connect(sys.argv[1])

if (conn == 0):
    print("no se encontro la base seleccionada")
    exit()

c = conn.cursor()

sentenciaSQL = input("ingrese comando SQL a ejecutar:\n")

c.execute(sentenciaSQL)

#print(c.fetchone())     #lee uno
#print(c.fetchone())


if(sentenciaSQL.split(' ')[0] == "select"):
#    print(c.fetchall())    #lee todos
    for row in c:          #iterable
        print(row)

if(sentenciaSQL.split(' ')[0] == 'insert'):
    conn.commit()


conn.close()

