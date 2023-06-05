-- 프로그래머스 level 1 / 가장 비싼 상품 구하기
SELECT MAX(PRICE) as MAX_PRICE
FROM PRODUCT

-- 프로그래머스 level 2 / 가장 비싼 식품 정보 출력하기
SELECT *
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
FETCH FIRST 1 ROWS ONLY;
