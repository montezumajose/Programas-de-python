#importacion de librerias
from furl import furl
import mysql.connector
#Obtener el valor de la categoría proporcionado por el usuario
url = furl("https://prueba.com/search?categoria=electrodomestico")

categoria = url.args['categoria']

#Conexión a la base de datos
conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "Montezuma29@", database = "wordpress")

cursor = conn.cursor()

#Validar y sanitizar la entrada del usuario
#consulta preparada segura
stmt = ("SELECT Nombre, Descripcion FROM Productos WHERE Categoria = %s")

#Vincular el parametro y ejecucion
cursor.execute(stmt, (categoria))

#procesar resultados
result = cursor.fetchall()

for row in result:
    print("Nombre: ",row['Nombre'])
    print("Descripcion: ",row['Descripcion'])

#Cerrar la conexion y liberar recursos
cursor.close()
conn.close()