CREATE TABLE IF NOT EXISTS IS601_Accounts(
    id int AUTO_INCREMENT PRIMARY KEY,
    account_number varchar(12) unique,
    account_type varchar(15),
    user_id int,
    balance int DEFAULT 0,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES IS601_Users(id),
    check((account_number != '000000000000' and balance >= 0) or account_number = '000000000000'))
