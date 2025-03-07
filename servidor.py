
import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="papu19",
    database="practica06_rubrica"
)

cursor = conexion.cursor()
print("Conexión exitosa a la base de datos")

# CRUD ---> INSERTAR
def insertar_linea(nombre_linea):
    sql = "INSERT INTO LineaInvestigacion (nombre_linea) VALUES (%s)"
    valores = (nombre_linea,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación insertada con éxito")

# Ejemplo de insercion
insertar_linea("Inteligencia Artificial")
insertar_linea("proyecto integrador")
insertar_linea("ejemplo de proyecto")

#CRUD -->LEER 
def obtener_lineas():
    sql = "SELECT * FROM LineaInvestigacion"
    cursor.execute(sql)
    resultados = cursor.fetchall()
    
    for fila in resultados:
        print(fila) 


obtener_lineas()
# CRUD --> ACTUALIZAR
def actualizar_linea(id_linea, nuevo_nombre):
    sql = "UPDATE LineaInvestigacion SET nombre_linea = %s WHERE id_linea = %s"
    valores = (nuevo_nombre, id_linea)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación actualizada con éxito")


actualizar_linea(1, "Machine Learning")

#CRUD --> ELIMINAR
def eliminar_linea(id_linea):
    sql = "DELETE FROM LineaInvestigacion WHERE id_linea = %s"
    valores = (id_linea,)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Línea de investigación eliminada con éxito")
eliminar_linea(1)

cursor.close()
conexion.close()



