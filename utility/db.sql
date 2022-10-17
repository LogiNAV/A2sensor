CREATE DATABASE LogiNAVDB;
CREATE USER 'LogiNAV'@'localhost' IDENTIFIED BY 'LogiNAV@';
GRANT ALL PRIVILEGES ON LogiNAVDB.* TO 'LogiNAV'@'localhost';
FLUSH PRIVILEGES;

USE LogiNAVDB

CREATE TABLE sembradora (
    id tinyint PRIMARY KEY,
    hora time,
    sensor1 tinyint,
    sensor2 tinyint,
    sensor3 tinyint,
    sensor4 tinyint,
    sensor5 tinyint,
    sensor6 tinyint,
    sensor7 tinyint,
    sensor8 tinyint,
    sensor9 tinyint,
    sensor10 tinyint,
    sensor11 tinyint,
    sensor12 tinyint,
    sensor13 tinyint,
    sensor14 tinyint,
    sensor15 tinyint,
    sensor16 tinyint,
    sensor17 tinyint,
    sensor18 tinyint,
    sensor19 tinyint,
    sensor20 tinyint,
    sensor21 tinyint,
    sensor22 tinyint,
    sensor23 tinyint,
    sensor24 tinyint,
    sensor25 tinyint,
    sensor26 tinyint,
    sensor27 tinyint,
    sensor28 tinyint,
    sensor29 tinyint,
    sensor30 tinyint,
    sensor31 tinyint,
    sensor32 tinyint,
    sensor33 tinyint,
    sensor34 tinyint,
    sensor35 tinyint,
    sensor36 tinyint,
    sensor37 tinyint,
    sensor38 tinyint,
    sensor39 tinyint,
    sensor40 tinyint,
    sensor41 tinyint,
    sensor42 tinyint,
    sensor43 tinyint,
    sensor44 tinyint,
    sensor45 tinyint,
    sensor46 tinyint,
    sensor47 tinyint,
    sensor48 tinyint,
    sensor49 tinyint,
    sensor50 tinyint
);

DELIMITER $$
CREATE PROCEDURE sensores()
BEGIN
	DECLARE contador INT;
	DECLARE idd TINYINT;
	DECLARE horaa TIME;
	SET contador = 1;
	inicio: LOOP
	IF contador<=120 THEN BEGIN SET idd=contador; SET horaa=CURTIME();
	END;
	END IF;
	IF contador = 121 THEN LEAVE inicio;
	END IF;
	INSERT INTO sembradora (id, hora) VALUES (idd, horaa);
	SET contador = contador+1;
	END LOOP;
END;$$

CALL sensores();$$

