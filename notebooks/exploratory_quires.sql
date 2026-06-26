-- Query 1: Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- Query 2: List all companies
SELECT id, company_name
FROM companies
ORDER BY company_name;

-- Query 3: Total records in Profit & Loss
SELECT COUNT(*)
FROM profitandloss;

-- Query 4: Top 10 companies by sales
SELECT company_id, year, sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;

-- Query 5: Companies with highest ROE
SELECT company_name, roe_percentage
FROM companies
ORDER BY roe_percentage DESC
LIMIT 10;

-- Query 6: Total Balance Sheet records
SELECT COUNT(*)
FROM balancesheet;

-- Query 7: Total Cash Flow records
SELECT COUNT(*)
FROM cashflow;

-- Query 8: Number of stock price records
SELECT COUNT(*)
FROM stock_prices;

-- Query 9: Companies by sector
SELECT broad_sector, COUNT(*)
FROM sectors
GROUP BY broad_sector
ORDER BY COUNT(*) DESC;

-- Query 10: Companies having annual reports
SELECT company_id, COUNT(*)
FROM documents
GROUP BY company_id
ORDER BY COUNT(*) DESC;