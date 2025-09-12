-- 맛을 기준으로 total order 구해야함
-- 7월 flavor 별 total_order 끼리 합하고, 상반기 flavor 별 total_order 합하고
-- 이 두 결과를 합한 후 그 테이블의 TOTAL_ORDER를 order by 한 후, limit 3으로 조회
-- select는 flavor로
-- 그럼 from 절에서 flavor 별 합한 7월 테이블과 상반기 테이블을 합친 테이블 만들자!!


SELECT FLAVOR
FROM (SELECT FLAVOR, TOTAL_ORDER
      FROM FIRST_HALF 
      UNION ALL 
      SELECT FLAVOR, TOTAL_ORDER 
      FROM JULY) AS SUM_TAB
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3;



-- SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER)
-- FROM FIRST_HALF
-- GROUP BY FLAVOR
-- +
-- SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER)
-- FROM JULY
-- GROUP BY FLAVOR

-- SELECT SHIPMENT_ID, FLAVOR, SUM(TOTAL_ORDER)
-- FROM FIRST_HALF AS F JOIN JULY AS J ON F.FLAVOR=J.FLAOVR
-- GROUP BY FLAVOR