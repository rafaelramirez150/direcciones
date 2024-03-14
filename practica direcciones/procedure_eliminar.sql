DELIMITER //

CREATE PROCEDURE eliminar_estado(IN p_id_estado INT)
BEGIN
    DELETE FROM estado WHERE id_estado = p_id_estado;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE eliminar_calle(IN p_id_calle INT)
BEGIN
    DELETE FROM calle WHERE id_calle = p_id_calle;
END //

DELIMITER ;


DELIMITER //

CREATE PROCEDURE eliminar_municipio(IN p_id_municipio INT)
BEGIN
    DELETE FROM municipio WHERE id_municipio = p_id_municipio;
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE eliminar_colonia(IN p_id_colonia INT)
BEGIN
    DELETE FROM colonia WHERE id_colonia = p_id_colonia;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE eliminar_persona(IN p_id_persona INT)
BEGIN
    DELETE FROM persona WHERE id_persona = p_id_persona;
END //

DELIMITER ;



