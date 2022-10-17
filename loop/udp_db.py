import socket
import pymysql

## UDP ##
UDP_IP = "10.0.0.1"
UDP_PORT = 4210
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

## BDD ##
connection=pymysql.connect(host='localhost',
                      port=3306,
                      user='LogiNAV',
                      password='LogiNAV@')
connection.select_db('LogiNAVDB')
###

while True:
    for id in range(1,121):
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        with connection.cursor() as cursor:
            cursor.execute("UPDATE sembradora SET hora = CURTIME() ,"
                           "sensor1 = %s , sensor2 = %s , sensor3 = %s , sensor4 = %s , sensor5 = %s , sensor6 = %s , sensor7 = %s , sensor8 = %s , sensor9 = %s ,sensor10 = %s,"
                           "sensor11 = %s, sensor12 = %s, sensor13 = %s, sensor14 = %s, sensor15 = %s, sensor16 = %s, sensor17 = %s, sensor18 = %s, sensor19 = %s,sensor20 = %s,"
                           "sensor21 = %s, sensor22 = %s, sensor23 = %s, sensor24 = %s, sensor25 = %s, sensor26 = %s, sensor27 = %s, sensor28 = %s, sensor29 = %s,sensor30 = %s,"
                           "sensor31 = %s, sensor32 = %s, sensor33 = %s, sensor34 = %s, sensor35 = %s, sensor36 = %s, sensor37 = %s, sensor38 = %s, sensor39 = %s,sensor40 = %s,"
                           "sensor41 = %s, sensor42 = %s, sensor43 = %s, sensor44 = %s, sensor45 = %s, sensor46 = %s, sensor47 = %s, sensor48 = %s, sensor49 = %s,sensor50 = %s "
                           "WHERE id = %s;",(data[3], data[49], data[11], data[2], data[16], data[9], data[4], data[14], data[8], data[1],
                                             data[15],data[17],data[0],data[13],data[12],data[6],data[10],data[7],data[5],data[18],
                                             data[24],data[19],data[20],data[22],data[25],data[23],data[26],data[21],data[27],data[28],
                                             data[30],data[31],data[29],data[32],data[35],data[33],data[45],data[38],data[36],data[48],
                                             data[34],data[37],data[46],data[41],data[42],data[44],data[39],data[43],data[47],data[40],id))
            connection.commit()
