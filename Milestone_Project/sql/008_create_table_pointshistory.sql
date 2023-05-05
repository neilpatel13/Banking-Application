CREATE TABLE IF NOT EXISTS IS601_TransactionHistory(
    id INT PRIMARY KEY AUTO_INCREMENT,
    account_src INT,
    account_dest INT,
    balance_change INT,
    transaction_type VARCHAR(20) NOT NULL COMMENT 'The type of transaction that occurred',
    memo VARCHAR(250) DEFAULT NULL COMMENT 'A desc of what the transc occured was for',
    expected_total INT,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
    FOREIGN KEY (account_src) REFERENCES IS601_Accounts(id),
    FOREIGN KEY(account_dest) REFERENCES IS601_Accounts(id),
    constraint S_ZeroTransferNotAllowed CHECK(balance_change != 0)
)