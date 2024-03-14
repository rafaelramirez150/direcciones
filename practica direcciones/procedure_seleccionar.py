#Seleccionar estado
import mysql.connector

def obtener_estado(id_estado):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('obtener_estado', (id_estado,))

        # Recuperar los resultados
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función obtener_estado con el valor deseado
obtener_estado(1)

#Seleccionar calle
import mysql.connector

def obtener_calle(id_calle):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('obtener_calle', (id_calle,))

        # Recuperar los resultados
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)

    #except mysql.connector.Error as err:
        #print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función obtener_calle con el valor deseado
obtener_calle(4)
obtener_calle(3)
obtener_calle(5)

#Seleccionar municipio
import mysql.connector

def obtener_municipio(id_municipio):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('obtener_municipio', (id_municipio,))

        # Recuperar los resultados
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función obtener_municipio con el valor deseado
obtener_municipio(1)

#Seleccionar colonia
import mysql.connector

def obtener_colonia(id_colonia):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('obtener_colonia', (id_colonia,))

        # Recuperar los resultados
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función obtener_colonia con el valor deseado
obtener_colonia(1)

#Seleccionar persona
import mysql.connector

def obtener_persona(id_persona):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('obtener_persona', (id_persona,))

        # Recuperar los resultados
        for result in cursor.stored_results():
            rows = result.fetchall()
            for row in rows:
                print(row)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función obtener_persona con el valor deseado
obtener_persona(1)