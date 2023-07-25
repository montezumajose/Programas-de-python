#importacion de librerias
from furl import furl
import mysql.connector
#Obtener el valor de ID proporsionado por el usuario
url = furl("https://prueba.com/search?id=23")
id = url.args['id']

#Conexion a la base de datos

conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "Montezuma29@", database = "wordpress")

cursor = conn.cursor()
#Consulta preparada con INNER JOIN seguro

stmt = ("SELECT u.Nombre, t.NumeroTarjeta, t.FechaExpiracion FROM Usuarios u INNER JOIN TarjetasDeCredito t ON u.ID = t.IDUsuario  WHERE u.ID = %s")

cursor.execute(stmt, (id))
result = cursor.fetchall()

#Procesar resultados

for row in result:
    print("Nombre: ",row['Nombre'])
    print("Numero de Tarjeta: ",row['NumeroTarjeta'])
    print("Fecha de Expiracion: ",row['FechaExpiracion'])

#Cerrar la conexion y liberar recursos
cursor.close()
conn.close()
