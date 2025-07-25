SELECT B.BOOK_ID, A.AUTHOR_NAME, DATE_FORMAT(B.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK AS B JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID 
WHERE B.CATEGORY IN ("경제")
ORDER BY PUBLISHED_DATE ASC;