import socket
import pymysql

## UDP ##

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("127.0.0.1", 9091)); #Se asigna un puerto libre para el socket
serverSocket.listen();

## BDD ##
connection=pymysql.connect(host='localhost',
                      port=3306,
                      user='LogiNAV',
                      password='LogiNAV@')
connection.select_db('LogiNAVDB')
###

while True:
    (clientConnected, clientAddress) = serverSocket.accept();
    lista = []
    for i in range(1, 51):  #Bucle para comprobar el String de la consulta y hacer una cadena con todos los resultados
        def consulta():
            with connection.cursor() as cursor:
                consulta = ("SELECT sensor{} FROM sembradora;".format(str(i)))
                cursor.execute(consulta)
                connection.commit()
                resultado = str(cursor.fetchall())
            #Comprueba el String de la consulta 120
            if resultado == "((0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,), (0,))":
                lista.append ("Vacio")
            elif resultado == "((1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,), (1,))":
                lista.append ("Atascado")
            else:
                lista.append ("OK")
            sensor = "|".join(lista) #Junta los resultados uniendolos con |
            return sensor
        consulta()

    clientConnected.send(consulta().encode()); #Envio de información al cliente (main.py)
