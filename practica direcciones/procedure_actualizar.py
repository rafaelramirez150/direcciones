# Actualizar estado
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user="root",
    password="root",
    database="direcciones"
)

# Crear un objeto cursor
cursor = conexion.cursor()

# Procedimiento para actualizar registros en la tabla estado
def actualizar_estado(id_estado, nueva_descripcion):
    try:
        cursor.callproc('actualizar_estado', (id_estado, nueva_descripcion))
        conexion.commit()
        print("Registro actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el registro: {str(e)}")
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
actualizar_estado(2, 'Oaxaca')



# Actualizar calle
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user="root",
    password="root",
    database="direcciones"
)

# Crear un objeto cursor
cursor = conexion.cursor()

# Procedimiento para actualizar registros en la tabla calle
def actualizar_calle(id_calle, nueva_descripcion):
    try:
        cursor.callproc('actualizar_calle', (id_calle, nueva_descripcion))
        conexion.commit()
        print("Registro de calle actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el registro de calle: {str(e)}")
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
actualizar_calle(2, 'Calle Vieja')



# Actualizar municipio
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user="root",
    password="root",
    database="direcciones"
)

# Crear un objeto cursor
cursor = conexion.cursor()

# Procedimiento para actualizar registros en la tabla municipio
def actualizar_municipio(id_municipio, nueva_descripcion):
    try:
        cursor.callproc('actualizar_municipio', (id_municipio, nueva_descripcion))
        conexion.commit()
        print("Registro de municipio actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el registro de municipio: {str(e)}")
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
actualizar_municipio(2, 'Municipio Viejo')


# Actualizar colonia
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user="root",
    password="root",
    database="direcciones"
)

# Crear un objeto cursor
cursor = conexion.cursor()

# Procedimiento para actualizar registros en la tabla colonia
def actualizar_colonia(id_colonia, nueva_descripcion, nuevo_cp):
    try:
        cursor.callproc('actualizar_colonia', (id_colonia, nueva_descripcion, nuevo_cp))
        conexion.commit()
        print("Registro de colonia actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el registro de colonia: {str(e)}")
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
actualizar_colonia(2, 'Vieja Colonia', 98765)


# Actualizar persona
import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    user="root",
    password="root",
    database="direcciones"
)

# Crear un objeto cursor
cursor = conexion.cursor()

# Procedimiento para actualizar registros en la tabla persona
def actualizar_persona(id_persona, nuevo_nombre, nuevo_num_calle, nuevo_telefono, nuevo_id_estado, nuevo_id_municipio, nuevo_id_colonia, nuevo_id_calle):
    try:
        cursor.callproc('actualizar_persona', (id_persona, nuevo_nombre, nuevo_num_calle, nuevo_telefono, nuevo_id_estado, nuevo_id_municipio, nuevo_id_colonia, nuevo_id_calle))
        conexion.commit()
        print("Registro de persona actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar el registro de persona: {str(e)}")
    finally:
        cursor.close()
        conexion.close()

# Ejemplo de uso
actualizar_persona(2, 'María', 123, '1234567890', 2, 2, 2, 2)