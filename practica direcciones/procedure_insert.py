#Insertar estado
import mysql.connector

# Datos de ejemplo para el estado a insertar
id_estado = 1
descripcion = 'Guerrero'

try:
    # Conectar a la base de datos
    cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
    cursor = cnx.cursor()

    # Llamar al procedimiento almacenado directamente
    cursor.execute("""
        INSERT INTO estado (id_estado, descripcion)
        VALUES (%s, %s)
    """, (id_estado, descripcion))

    # Confirmar los cambios
    cnx.commit()

    print("Inserción de estado realizada con éxito.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar la conexión
    cursor.close()
    cnx.close()


#Insertar calle
import mysql.connector

# Datos de ejemplo para el estado a insertar
id_calle = 1
descripcion = 'Calle Reforma'

try:
    # Conectar a la base de datos
    cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
    cursor = cnx.cursor()

    # Llamar al procedimiento almacenado directamente
    cursor.execute("""
        INSERT INTO calle (id_calle, descripcion)
        VALUES (%s, %s)
    """, (id_calle, descripcion))

    # Confirmar los cambios
    cnx.commit()

    print("Inserción de calle realizada con éxito.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar la conexión
    cursor.close()
    cnx.close()

#Insertar municipio

import mysql.connector

# Datos de ejemplo para el estado a insertar
id_municipio = 1
descripcion = 'Nuevo Municipio'

try:
    # Conectar a la base de datos
    cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
    cursor = cnx.cursor()

    # Llamar al procedimiento almacenado directamente
    cursor.execute("""
        INSERT INTO municipio (id_municipio, descripcion)
        VALUES (%s, %s)
    """, (id_municipio, descripcion))

    # Confirmar los cambios
    cnx.commit()

    print("Inserción de municipio realizada con éxito.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar la conexión
    cursor.close()
    cnx.close()

#Insertar colonia

import mysql.connector

# Datos de ejemplo para el estado a insertar
id_colonia = 1
descripcion = 'Colonia Guerrero'
cp = '123456'

try:
    # Conectar a la base de datos
    cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
    cursor = cnx.cursor()

    # Llamar al procedimiento almacenado directamente
    cursor.execute("""
        INSERT INTO colonia (id_colonia, descripcion, cp)
        VALUES (%s, %s, %s)
    """, (id_colonia, descripcion, cp))

    # Confirmar los cambios
    cnx.commit()

    print("Inserción de colonia realizada con éxito.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Cerrar la conexión
    cursor.close()
    cnx.close()


#Insertar persona

import mysql.connector

id_persona = 10
nombre = 'Juan lopez'
num_calle = 123
telefono = '555-1234'
id_estado = 2
id_municipio = 2
id_colonia = 2  # Ajusta este valor según tu caso
id_calle = 2

try:
    cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
    cursor = cnx.cursor()

    cursor.execute("""
        INSERT INTO persona (
            id_persona, nombre, num_calle, telefono,
            id_estado, id_municipio, id_colonia, id_calle
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (id_persona, nombre, num_calle, telefono, id_estado, id_municipio, id_colonia, id_calle))

    cnx.commit()

    print("Inserción de persona realizada con éxito.")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    cursor.close()
    cnx.close()