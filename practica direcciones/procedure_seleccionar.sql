DELIMITER //

CREATE PROCEDURE obtener_estado(IN p_id_estado INT)
BEGIN
    SELECT * FROM estado WHERE id_estado = p_id_estado;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE obtener_calle(IN p_id_calle INT)
BEGIN
    SELECT * FROM calle WHERE id_calle = p_id_calle;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE obtener_municipio(IN p_id_municipio INT)
BEGIN
    SELECT * FROM municipio WHERE id_municipio = p_id_municipio;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE obtener_colonia(IN p_id_colonia INT)
BEGIN
    SELECT * FROM colonia WHERE id_colonia = p_id_colonia;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE obtener_persona(IN p_id_persona INT)
BEGIN
    SELECT * FROM persona WHERE id_persona = p_id_persona;
END //

DELIMITER ;

