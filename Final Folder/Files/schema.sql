-- Create and use crypto_db
DROP DATABASE IF EXISTS crypto_db;
CREATE DATABASE crypto_db;
USE crypto_db;

-- Create Two Tables
CREATE TABLE bitcoin (
  id INT PRIMARY KEY,
  date VARCHAR(14),
  btc_close DECIMAL(12, 2)
);

CREATE TABLE ethereum (
  id INT PRIMARY KEY,
  date VARCHAR(14),
  eth_close DECIMAL(12, 2)
);
