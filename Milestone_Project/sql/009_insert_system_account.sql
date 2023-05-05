INSERT INTO IS601_Users (id, username, password, email) VALUES (-1, 'system', 'password123', 'system@example.com') ON DUPLICATE KEY UPDATE modified = CURRENT_TIMESTAMP;

INSERT INTO IS601_Accounts (id, account_number, account_type, user_id, balance) VALUES (-1, '000000000000', 'world', -1, 0) ON DUPLICATE KEY UPDATE modified = CURRENT_TIMESTAMP;
