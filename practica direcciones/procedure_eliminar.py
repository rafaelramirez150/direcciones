# Eliminar estado
import mysql.connector

def eliminar_estado(id_estado):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Sentencia SQL para eliminar un registro en la tabla estado
        delete_query = "DELETE FROM estado WHERE id_estado = %s"
        
        # Ejecutar la sentencia SQL con el parámetro
        cursor.execute(delete_query, (id_estado,))

        # Hacer commit para aplicar los cambios
        cnx.commit()

        print(f"Registro con id_estado {id_estado} eliminado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función eliminar_estado con el id_estado deseado
eliminar_estado(1)

# Eliminar calle
import mysql.connector

def eliminar_calle(id_calle):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Sentencia SQL para eliminar un registro en la tabla calle
        delete_query = "DELETE FROM calle WHERE id_calle = %s"
        
        # Ejecutar la sentencia SQL con el parámetro
        cursor.execute(delete_query, (id_calle,))

        # Hacer commit para aplicar los cambios
        cnx.commit()

        print(f"Registro con id_calle {id_calle} eliminado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función eliminar_calle con el id_calle deseado
eliminar_calle(1)

# Eliminar colonia
import mysql.connector

def eliminar_colonia(id_colonia):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Sentencia SQL para eliminar un registro en la tabla colonia
        delete_query = "DELETE FROM colonia WHERE id_colonia = %s"
        
        # Ejecutar la sentencia SQL con el parámetro
        cursor.execute(delete_query, (id_colonia,))

        # Hacer commit para aplicar los cambios
        cnx.commit()

        print(f"Registro con id_colonia {id_colonia} eliminado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función eliminar_colonia con el id_colonia deseado
eliminar_colonia(1)

# Eliminar municipio
import mysql.connector

def eliminar_municipio(id_municipio):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Sentencia SQL para eliminar un registro en la tabla municipio
        delete_query = "DELETE FROM municipio WHERE id_municipio = %s"
        
        # Ejecutar la sentencia SQL con el parámetro
        cursor.execute(delete_query, (id_municipio,))

        # Hacer commit para aplicar los cambios
        cnx.commit()

        print(f"Registro con id_municipio {id_municipio} eliminado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función eliminar_municipio con el id_municipio deseado
eliminar_municipio(1)

# Eliminar persona
import mysql.connector

def eliminar_persona(id_persona):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Sentencia SQL para eliminar un registro en la tabla persona
        delete_query = "DELETE FROM persona WHERE id_persona = %s"
        
        # Ejecutar la sentencia SQL con el parámetro
        cursor.execute(delete_query, (id_persona,))

        # Hacer commit para aplicar los cambios
        cnx.commit()

        print(f"Registro con id_persona {id_persona} eliminado exitosamente.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función eliminar_persona con el id_persona deseado
eliminar_persona(1)

