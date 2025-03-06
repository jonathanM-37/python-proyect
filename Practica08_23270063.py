#Jonathan Mendez Martinez
#23270063
#python -m pip install --upgrade pip


import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="papu19",
        database="practica05_usuarios"
    )

def insertar_tipo_proyecto(tipo, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    
    # Verificar si el tipo ya existe
    cursor.execute("SELECT * FROM tipoproyecto WHERE tipo = %s", (tipo,))
    existe = cursor.fetchone()

    if existe:
        print(f"El tipo de proyecto '{tipo}' ya existe.")
    else:
        sql = "INSERT INTO tipoproyecto (tipo, nombre) VALUES (%s, %s)"
        valores = (tipo, nombre)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Tipo de proyecto insertado correctamente.")

    conexion.close()


def leer_tipos_proyecto():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tipoproyecto")
    registros = cursor.fetchall()
    conexion.close()
    return registros

def actualizar_tipo_proyecto(tipo, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE tipoproyecto SET nombre = %s WHERE tipo = %s"
    valores = (nuevo_nombre, tipo)
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()
    print("Tipo de proyecto actualizado correctamente.")

def eliminar_tipo_proyecto(tipo):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM tipoproyecto WHERE tipo = %s"
    valores = (tipo,)
    cursor.execute(sql, valores)
    conexion.commit()
    conexion.close()
    print("Tipo de proyecto eliminado correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    insertar_tipo_proyecto("RCISP", "Estimación de peso de ganado bovino mediante aprendizaje profundo")
    insertar_tipo_proyecto("TDWM","Sistema en la Nube para la gestión")
    print(leer_tipos_proyecto())
    actualizar_tipo_proyecto("INV01", "Investigación Avanzada")
    eliminar_tipo_proyecto("INV01")
