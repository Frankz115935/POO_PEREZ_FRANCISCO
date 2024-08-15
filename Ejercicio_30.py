import os
os.system('cls')

import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='controlescolar'
)

if connection.is_connected():
    print("Conexión exitosa a la base de datos MySQL")


#EJEMPLO CONSULTA SELECT
cursor = connection.cursor()

cursor.execute("SELECT * FROM alumnos")

resultados = cursor.fetchall() #obtener datos

for fila in resultados:
    print(fila)
    


cursor.execute("INSERT INTO alumnos (nombre, edad, direccion) VALUES ('Prueba', 25, 'Calle Inventada')")

connection.commit()

cursor.close()

connection.close()