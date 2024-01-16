-- 기본 조회 및 필터링

-- SELECT title, author FROM books; 
-- SELECT * FROM books WHERE rating >= 8.0;
-- SELECT title,review FROM books WHERE review >=100;
-- SELECT title,price FROM books WHERE price <20000;
-- SELECT * FROM books WHERE ranking_weeks > 4;
-- SELECT * FROM books WHERE author = "ETS 저";
-- SELECT * FROM books WHERE publisher = '시공주니어';

-- 조인 및 관계 
-- SELECT author, COUNT(*) FROM books GROUP BY author;
-- SELECT publisher , COUNT(*) as Count_publisher FROM books GROUP BY publisher ORDER BY Count_publisher DESC LIMIT 1;
-- SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author ORDER BY rating_avg DESC;
-- SELECT * FROM books WHERE ranking = 1;
-- SELECT  title ,sales,review FROM books ORDER BY sales DESC , review DESC LIMIT 10;
-- SELECT * FROM books ORDER BY publishing DESC LIMIT 5;

-- 집꼐 및 그룹화
--  SELECT author, AVG(rating) AS rating_avg FROM books GROUP BY author;
-- SELECT publishing, COUNT(*) FROM books GROUP BY publishing;
-- SELECT title, AVG(price) FROM books GROUP BY title;
-- SELECT * FROM books ORDER BY review DESC LIMIT 5;
-- SELECT ranking,AVG(review) FROM books GROUP BY ranking;

-- 서브쿼리 및 고급 기능
-- SELECT title, rating FROM books WHERE rating > (SELECT AVG(rating) FROM books) ORDER BY rating DESC; 
-- SELECT title, price FROM books WHERE price > (SELECT AVG(price) FROM books);
-- SELECT title, review FROM books WHERE review > (SELECT MAX(review) FROM books);
-- SELECT title, sales FROM books WHERE sales < (SELECT AVG(sales) FROM books); 
-- SELECT author, title FROM books WHERE author = (SELECT author FROM books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1);

-- 데이터 수정 및 관리 
-- UPDATE Books SET price = 23000 WHERE title = 'New Book Title';
-- UPDATE Books SET title = 'Updated Title' WHERE author = '홍길동';
-- DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books);
-- UPDATE Books SET rating = rating + 1 WHERE publisher = '민음사';

-- 데이터 분석 예제
-- SELECT author, AVG(rating), AVG(sales) FROM books GROUP BY author;
-- SELECT publishing, AVG(price) FROM books GROUP BY publishing ORDER BY publishing ASC;
-- SELECT publisher,COUNT(*) AS book_count,SUM(review) AS review_sum FROM books GROUP BY publisher ORDER BY book_count DESC;
-- SELECT ranking, AVG(sales) FROM books GROUP BY ranking; 
-- SELECT price, AVG(review),AVG(rating) FROM books GROUP BY price ORDER BY price ;

-- 난이도 있는 문제  
-- SELECT publisher, author, AVG(sales) as avg_sales
-- FROM Books
-- GROUP BY publisher, author
-- ORDER BY publisher, avg_sales DESC

-- SELECT title, review, price
-- FROM Books
-- WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);

-- SELECT author, COUNT(DISTINCT title) as num_books
-- FROM Books
-- GROUP BY author
-- ORDER BY num_books DESC
-- LIMIT 1;

-- SELECT author, MAX(sales) as max_sales
-- FROM Books
-- GROUP BY author;

-- SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
-- FROM Books
-- GROUP BY year;

-- SELECT publisher,COUNT(*), MAX(rating) - MIN(rating) as rating_difference
-- FROM Books
-- GROUP BY publisher
-- HAVING COUNT(*) >= 2
-- ORDER BY rating_difference DESC
-- LIMIT 1;

-- SELECT title,sales, rating / sales as ratio
-- FROM Books
-- ORDER BY ratio DESC


