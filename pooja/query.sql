-- Query to check successful load
SELECT * FROM bitcoin;

SELECT * FROM ethereum;

-- Join tables on county_id
SELECT bitcoin.id "ID", bitcoin.date "Date", bitcoin.close "Bitcoin Close", ethereum.close "Ethereum Close"
FROM bitcoin
INNER JOIN ethereum
USING(date);
