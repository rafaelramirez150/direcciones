DELIMITER //
CREATE PROCEDURE actualizar_estado(
    IN p_id_estado INT,
    IN p_nueva_descripcion VARCHAR(50)
)
BEGIN
    UPDATE estado
    SET descripcion = p_nueva_descripcion
    WHERE id_estado = p_id_estado;
END //
DELIMITER ;


DELIMITER //
CREATE PROCEDURE actualizar_calle(
    IN p_id_calle INT,
    IN p_nueva_descripcion VARCHAR(50)
)
BEGIN
    UPDATE calle
    SET descripcion = p_nueva_descripcion
    WHERE id_calle = p_id_calle;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE actualizar_municipio(
    IN p_id_municipio INT,
    IN p_nueva_descripcion VARCHAR(50)
)
BEGIN
    UPDATE municipio
    SET descripcion = p_nueva_descripcion
    WHERE id_municipio = p_id_municipio;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE actualizar_colonia(
    IN p_id_colonia INT,
    IN p_nueva_descripcion VARCHAR(100),
    IN p_nuevo_cp INT
)
BEGIN
    UPDATE colonia
    SET descripcion = p_nueva_descripcion,
        cp = p_nuevo_cp
    WHERE id_colonia = p_id_colonia;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE actualizar_persona(
    IN p_id_persona INT,
    IN p_nuevo_nombre VARCHAR(30),
    IN p_nuevo_num_calle INT,
    IN p_nuevo_telefono VARCHAR(12),
    IN p_nuevo_id_estado INT,
    IN p_nuevo_id_municipio INT,
    IN p_nuevo_id_colonia INT,
    IN p_nuevo_id_calle INT
)
BEGIN
    UPDATE persona
    SET nombre = p_nuevo_nombre,
        num_calle = p_nuevo_num_calle,
        telefono = p_nuevo_telefono,
        id_estado = p_nuevo_id_estado,
        id_municipio = p_nuevo_id_municipio,
        id_colonia = p_nuevo_id_colonia,
        id_calle = p_nuevo_id_calle
    WHERE id_persona = p_id_persona;
END //
DELIMITER ;