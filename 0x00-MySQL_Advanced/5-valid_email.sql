-- a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.


CREATE TRIGGER resets_valid_email_attr
BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = IF(New.email REGEXP '^[[:alnum:]_.-]+@[[:alnum:]_-]+(\\.[[:alnum:]_-]+)*\\.[[:alpha:]]{2,4}$', 1, 0)
