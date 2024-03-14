DELIMITER //

CREATE PROCEDURE insertar_estado(
    IN p_id_estado int,
	IN p_descripcion varchar(50)
)
BEGIN
    INSERT INTO estado (
        id_estado, descripcion
    )
    VALUES (
        p_id_estado, p_descripcion
    );
END //

DELIMITER ;

drop procedure insertar_estado;

DELIMITER //

CREATE PROCEDURE insertar_calle(
    IN p_id_calle int,
	IN p_descripcion varchar(50)
)
BEGIN
    INSERT INTO calle (
        id_calle, descripcion
    )
    VALUES (
        p_id_calle, p_descripcion
    );
END //

DELIMITER ;

drop procedure insertar_calle;

DELIMITER //

CREATE PROCEDURE insertar_municipio(
    IN p_id_municipio int,
    in p_descripcion varchar(50)
)
BEGIN
    INSERT INTO municipio (
        id_municipio, descripcion
    )
    VALUES (
        p_id_municipio, p_descripcion
    );
END //

DELIMITER ;

drop procedure insertar_municipio;

DELIMITER //

CREATE PROCEDURE insertar_colonia(
    IN p_id_colonia int,
    in p_descripcion varchar(100)
)
BEGIN
    INSERT INTO colonia (
        id_colonia, descripcion
    )
    VALUES (
        p_id_colonia, p_descripcion
    );
END //

DELIMITER ;

drop procedure insertar_colonia;

DELIMITER //

CREATE PROCEDURE insertar_persona(
    IN p_id_persona INT,
    IN p_nombre VARCHAR(30),
    IN p_num_calle INT,
    IN p_telefono VARCHAR(12),
    IN p_id_estado INT,
    IN p_id_municipio INT,
    IN p_id_colonia INT,
    IN p_id_calle INT
)
BEGIN
    INSERT INTO persona (
        id_persona, nombre, num_calle, telefono,
        id_estado, id_municipio, id_colonia, id_calle
    )
    VALUES (
        p_id_persona, p_nombre, p_num_calle, p_telefono,
        p_id_estado, p_id_municipio, p_id_colonia, p_id_calle
    );
END //

DELIMITER ;

drop procedure insertar_persona;