import mysql.connector

class TipoProyectoCRUD:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def insertar(self, tipo, nombre):
        conexion = self.conectar()
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

    def leer(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tipoproyecto")
        registros = cursor.fetchall()
        conexion.close()
        return registros

    def actualizar(self, tipo, nuevo_nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        sql = "UPDATE tipoproyecto SET nombre = %s WHERE tipo = %s"
        cursor.execute(sql, (nuevo_nombre, tipo))
        conexion.commit()
        conexion.close()
        print("Tipo de proyecto actualizado correctamente.")

    def eliminar(self, tipo):
        conexion = self.conectar()
        cursor = conexion.cursor()
        sql = "DELETE FROM tipoproyecto WHERE tipo = %s"
        cursor.execute(sql, (tipo,))
        conexion.commit()
        conexion.close()
        print("Tipo de proyecto eliminado correctamente.")

class ProfesorCRUD:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def conectar(self):
        return mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def insertar(self, nombreProf):
        conexion = self.conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO profesor (nombreProf) VALUES (%s)"
        cursor.execute(sql, (nombreProf,))
        conexion.commit()
        conexion.close()
        print("Profesor insertado correctamente.")

    def leer(self):
        conexion = self.conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM profesor")
        registros = cursor.fetchall()
        conexion.close()
        return registros

    def actualizar(self, idprofesor, nuevo_nombre):
        conexion = self.conectar()
        cursor = conexion.cursor()
        sql = "UPDATE profesor SET nombreProf = %s WHERE idprofesor = %s"
        cursor.execute(sql, (nuevo_nombre, idprofesor))
        conexion.commit()
        conexion.close()
        print("Profesor actualizado correctamente.")

    def eliminar(self, idprofesor):
        conexion = self.conectar()
        cursor = conexion.cursor()
        sql = "DELETE FROM profesor WHERE idprofesor = %s"
        cursor.execute(sql, (idprofesor,))
        conexion.commit()
        conexion.close()
        print("Profesor eliminado correctamente.")

# Ejemplo de uso
if __name__ == "__main__":
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "papu19",
        "database": "practica05_usuarios"
    }
    
    tipoproyecto_crud = TipoProyectoCRUD(**db_config)
    profesor_crud = ProfesorCRUD(**db_config)
    
    # Ejemplos de uso
    tipoproyecto_crud.insertar("RCISP", "Estimación de peso de ganado bovino mediante aprendizaje profundo")
    tipoproyecto_crud.insertar("TDWM","Sistema en la Nube para la gestión")
    print(tipoproyecto_crud.leer())
    tipoproyecto_crud.actualizar("INV01", "Investigación Avanzada")
    tipoproyecto_crud.eliminar("INV01")
    
    profesor_crud.insertar("Dr. Juan Pérez")
    profesor_crud.insertar("Jesus Juan carlos perez")
    profesor_crud.insertar("Octavio Rios")
    print(profesor_crud.leer())
    profesor_crud.actualizar(1, "Dr. Pedro Gómez")
    profesor_crud.eliminar(1)




