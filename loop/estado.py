import pymysql
import time

## BDD ##
connection=pymysql.connect(host='localhost',
                      port=3306,
                      user='LogiNAV',
                      password='LogiNAV@')
connection.select_db('LogiNAVDB')
###

def conexion():
    with connection.cursor() as cursor:
        consulta = "SELECT hora FROM sembradora WHERE id=1;"
        cursor.execute(consulta)
        connection.commit()
    return cursor.fetchall()

def rojo():
    with connection.cursor() as cursor:
        cursor.execute("UPDATE sembradora SET sensor1 = 1, sensor2 = 1, sensor3 = 1, sensor4 = 1, sensor5 = 1, sensor6 = 1, sensor7 = 1, sensor8 = 1, sensor9 = 1, sensor10 = 1,"
                                   "sensor11 = 1, sensor12 = 1, sensor13 = 1, sensor14 = 1, sensor15 = 1, sensor16 = 1, sensor17 = 1, sensor18 = 1, sensor19 = 1,sensor20 = 1,"
                                   "sensor21 = 1, sensor22 = 1, sensor23 = 1, sensor24 = 1, sensor25 = 1, sensor26 = 1, sensor27 = 1, sensor28 = 1, sensor29 = 1,sensor30 = 1,"
                                   "sensor31 = 1, sensor32 = 1, sensor33 = 1, sensor34 = 1, sensor35 = 1, sensor36 = 1, sensor37 = 1, sensor38 = 1, sensor39 = 1,sensor40 = 1,"
                                   "sensor41 = 1, sensor42 = 1, sensor43 = 1, sensor44 = 1, sensor45 = 1, sensor46 = 1, sensor47 = 1, sensor48 = 1, sensor49 = 1,sensor50 = 1 ")
        connection.commit()

while True:
    conexion1 = conexion()
    time.sleep(8) # espera en segundos
    conexion2 = conexion()

    if conexion1 == conexion2:
        rojo()
