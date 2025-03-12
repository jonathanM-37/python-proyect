
#Jonathan Mendez Martinez
#https://github.com/jonathanM-37/python-proyect

import mysql.connector

import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="papu19",
        database="practica05_usuarios"
    )

#CRUD tipo_proyecto
def insertar_tipo_proyecto(tipo, nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tipoproyecto WHERE tipo = %s", (tipo,))
    if cursor.fetchone():
        print(f"El tipo de proyecto '{tipo}' ya existe.")
    else:
        sql = "INSERT INTO tipoproyecto (tipo, nombre) VALUES (%s, %s)"
        cursor.execute(sql, (tipo, nombre))
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
    cursor.execute(sql, (nuevo_nombre, tipo))
    conexion.commit()
    conexion.close()
    print("Tipo de proyecto actualizado correctamente.")

def eliminar_tipo_proyecto(tipo):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM tipoproyecto WHERE tipo = %s"
    cursor.execute(sql, (tipo,))
    conexion.commit()
    conexion.close()
    print("Tipo de proyecto eliminado correctamente.")

# CRUD para Profesor
def insertar_profesor(nombreProf):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (nombreProf) VALUES (%s)"
    cursor.execute(sql, (nombreProf,))
    conexion.commit()
    conexion.close()
    print("Profesor insertado correctamente.")

def leer_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    registros = cursor.fetchall()
    conexion.close()
    return registros

def actualizar_profesor(idprofesor, nuevo_nombre):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
    cursor.execute(sql, (nuevo_nombre, idprofesor))
    conexion.commit()
    conexion.close()
    print("Profesor actualizado correctamente.")

def eliminar_profesor(idprofesor):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE idprofesor = %s"
    cursor.execute(sql, (idprofesor,))
    conexion.commit()
    conexion.close()
    print("Profesor eliminado correctamente.")

def menu_tipoproyecto():
    while True:
        print("\nMenú de Tipo de Proyecto")
        print("1. Insertar Tipo de Proyecto")
        print("2. Ver Tipos de Proyecto")
        print("3. Actualizar Tipo de Proyecto")
        print("4. Eliminar Tipo de Proyecto")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el código del tipo de proyecto: ")
            nombre = input("Ingrese el nombre del tipo de proyecto: ")
            insertar_tipo_proyecto(tipo, nombre)
        elif opcion == "2":
            tipos = leer_tipos_proyecto()
            for t in tipos:
                print(f"Código: {t[0]}, Nombre: {t[1]}")
        elif opcion == "3":
            tipo = input("Ingrese el código del tipo de proyecto a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            actualizar_tipo_proyecto(tipo, nuevo_nombre)
        elif opcion == "4":
            tipo = input("Ingrese el código del tipo de proyecto a eliminar: ")
            eliminar_tipo_proyecto(tipo)
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente nuevamente.")

def menu_profesor():
    while True:
        print("\nMenú de Profesor")
        print("1. Insertar Profesor")
        print("2. Ver Profesores")
        print("3. Actualizar Profesor")
        print("4. Eliminar Profesor")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del profesor: ")
            insertar_profesor(nombre)
        elif opcion == "2":
            profesores = leer_profesores()
            for p in profesores:
                print(f"ID: {p[0]}, Nombre: {p[1]}")
        elif opcion == "3":
            idprofesor = input("Ingrese el ID del profesor a actualizar: ")
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            actualizar_profesor(idprofesor, nuevo_nombre)
        elif opcion == "4":
            idprofesor = input("Ingrese el ID del profesor a eliminar: ")
            eliminar_profesor(idprofesor)
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intente nuevamente.")

def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. CRUD para Tipo de Proyecto")
        print("2. CRUD para Profesor")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_tipoproyecto()
        elif opcion == "2":
            menu_profesor()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
