-- SQL script that creates a table users, same as in previous task but with
-- country, enumeration of countries: US, CO and TN, never null (= default US)

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country VARCHAR(10) DEFAULT 'US',
    PRIMARY KEY (id)
);
