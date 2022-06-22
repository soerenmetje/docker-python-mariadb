# creates tables holding data from studentenwerk backend

USE goeschmack;
CREATE TABLE mensa
(
    name VARCHAR(15) PRIMARY KEY
);
CREATE TABLE opening
(
    mensa   VARCHAR(15),
    weekday VARCHAR(10),
    open    TIME NULL,
    close   TIME NULL,
    PRIMARY KEY (mensa, weekday),
    FOREIGN KEY (mensa) REFERENCES mensa (name)
);
