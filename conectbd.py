import mysql.connector

# Establecer la conexión
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Abcd123",
    database="calculadora",
    auth_plugin='mysql_native_password',
    autocommit=True # Autoguardado de las consultas
)

# Crear un cursor para ejecutar consultas
cursor = conexion.cursor()

def agregar(opcion, num1, num2, resultadofinal):
    # Consulta para agregar datos a la tabla
    consulta = "INSERT INTO historial(opcion, numero1, numero2, resultadofinal) VALUES (%s, %s, %s, %s)"
    cursor.execute(consulta,(opcion, num1, num2, resultadofinal))
    return consulta

def consulta():
    con_datos = "SELECT * FROM historial"
    cursor.execute(con_datos)
    resultados = cursor.fetchall()
    return resultados

def eliminar(cursor):
    el_datos = "DELETE FROM historial ORDER BY idhistorial ASC LIMIT 1"
    cursor.execute(el_datos)
    return el_datos

# Cerrar la conexión al final del script o cuando ya no se necesite
#cursor.close()
#conexion.close()







