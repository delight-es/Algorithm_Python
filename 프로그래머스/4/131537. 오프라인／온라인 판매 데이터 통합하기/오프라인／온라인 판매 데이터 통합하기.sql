-- 온라인
SELECT  DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
PRODUCT_ID, USER_ID, SALES_AMOUNT FROM ONLINE_SALE
WHERE (SALES_DATE LIKE '2022-03-%')
-- 합침
UNION
-- 오프라인
SELECT  DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE, 
PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT FROM OFFLINE_SALE
WHERE (SALES_DATE LIKE '2022-03-%')
-- 정렬
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC