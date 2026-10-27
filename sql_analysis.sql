USE ecommerce_db;


-- 2. BUSINESS KPIs
SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Cost) AS Total_Cost,
    SUM(Sales - Cost) AS Total_Profit,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin,
    SUM(Quantity) AS Total_Quantity,
    COUNT(DISTINCT Order_ID) AS Total_Orders
FROM sales;


-- 3. TOP 10 CUSTOMERS BY SALES
SELECT
    Customer,
    COUNT(DISTINCT Order_ID) AS Orders,
    SUM(Sales) AS Sales,
    SUM(Cost) AS Cost,
    SUM(Sales - Cost) AS Profit,
    SUM(Quantity) AS Quantity,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Customer
ORDER BY Sales DESC
LIMIT 10;


-- 4. TOP 10 CUSTOMERS BY PROFIT
SELECT
    Customer,
    SUM(Sales - Cost) AS Profit
FROM sales
GROUP BY Customer
ORDER BY Profit DESC
LIMIT 10;


-- 5. CUSTOMERS WITH MORE THAN 25 ORDERS
SELECT
    Customer,
    COUNT(DISTINCT Order_ID) AS Orders,
    SUM(Sales) AS Sales
FROM sales
GROUP BY Customer
HAVING COUNT(DISTINCT Order_ID) > 25
ORDER BY Orders DESC;


-- 6. REGION ANALYSIS
SELECT
    Region,
    SUM(Sales) AS Sales,
    SUM(Cost) AS Cost,
    SUM(Sales - Cost) AS Profit,
    SUM(Quantity) AS Quantity,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Region
ORDER BY Sales DESC;


-- 7. BEST REGION
SELECT
    Region,
    SUM(Sales) AS Sales,
    SUM(Sales - Cost) AS Profit
FROM sales
GROUP BY Region
ORDER BY Sales DESC
LIMIT 1;


-- 8. CATEGORY ANALYSIS
SELECT
    Category,
    SUM(Sales) AS Sales,
    SUM(Cost) AS Cost,
    SUM(Sales - Cost) AS Profit,
    SUM(Quantity) AS Quantity,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Category
ORDER BY Sales DESC;


-- 9. PRODUCT ANALYSIS
SELECT
    Product,
    SUM(Sales) AS Sales,
    SUM(Cost) AS Cost,
    SUM(Sales - Cost) AS Profit,
    SUM(Quantity) AS Quantity,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Product
ORDER BY Sales DESC;


-- 10. TOP 5 PRODUCTS
SELECT
    Product,
    SUM(Sales) AS Sales,
    SUM(Sales - Cost) AS Profit
FROM sales
GROUP BY Product
ORDER BY Sales DESC
LIMIT 5;


-- 11. LOWEST 5 PRODUCTS
SELECT
    Product,
    SUM(Sales) AS Sales,
    SUM(Sales - Cost) AS Profit
FROM sales
GROUP BY Product
ORDER BY Sales ASC
LIMIT 5;


-- 12. TOP PRODUCTS BY PROFIT
SELECT
    Product,
    SUM(Sales - Cost) AS Profit,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Product
ORDER BY Profit DESC
LIMIT 10;


-- 13. HIGHEST PROFIT MARGIN PRODUCT
SELECT
    Product,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Product
ORDER BY Profit_Margin DESC
LIMIT 1;


-- 14. MONTHLY SALES ANALYSIS
SELECT
    MONTH(Order_Date) AS Month_Number,
    MONTHNAME(Order_Date) AS Month_Name,
    SUM(Sales) AS Sales,
    SUM(Cost) AS Cost,
    SUM(Sales - Cost) AS Profit,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY Month_Number;


-- 15. BEST SALES MONTH
SELECT
    MONTHNAME(Order_Date) AS Month_Name,
    SUM(Sales) AS Sales
FROM sales
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY Sales DESC
LIMIT 1;


-- 16. HIGH SALES BUT LOW MARGIN PRODUCTS
SELECT
    Product,
    SUM(Sales) AS Sales,
    SUM(Sales - Cost) AS Profit,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Product
HAVING SUM(Sales) > 1000000
ORDER BY Profit_Margin ASC;


-- 17. REGION + CATEGORY ANALYSIS
SELECT
    Region,
    Category,
    SUM(Sales) AS Sales,
    SUM(Sales - Cost) AS Profit,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Region, Category
ORDER BY Sales DESC;


-- 18. CUSTOMER PROFITABILITY
SELECT
    Customer,
    SUM(Sales) AS Sales,
    SUM(Sales - Cost) AS Profit,
    ROUND(SUM(Sales - Cost) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM sales
GROUP BY Customer
ORDER BY Profit DESC
LIMIT 10;
