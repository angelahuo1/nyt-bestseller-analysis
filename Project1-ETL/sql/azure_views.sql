-- Exploratory SQL Querie as Azure views for NYT Bestseller Data
-- Goal: As an aspiring author, I aim to understand what book traits help writers 
-- break into the list regarding publisher dominance, trends, seasonality, and longevity.

-- 1. Row counts for reference.
CREATE OR ALTER VIEW total_counts AS
SELECT 
    (SELECT COUNT(*) FROM books) AS total_books,
    (SELECT COUNT(*) FROM appearances) AS total_appearances;

-- 2. Most frequent authors on the bestsellers list?
CREATE OR ALTER VIEW top_authors AS
SELECT TOP 20
    b.author,
    COUNT(*) AS total_weeks,
    COUNT(DISTINCT a.list_date) AS unique_weeks,
    COUNT(DISTINCT b.title) AS unique_titles
FROM appearances a
JOIN books b ON a.isbn13 = b.isbn13
GROUP BY b.author
ORDER BY total_weeks DESC;

-- 3. Which publishers dominate the fiction bestsellers list?
CREATE OR ALTER VIEW top_publishers AS
SELECT
    b.publisher,
    COUNT(*) AS total_weeks,
    COUNT(DISTINCT b.title) AS unique_titles
FROM appearances a
JOIN books b ON a.isbn13 = b.isbn13
GROUP BY b.publisher
ORDER BY total_weeks DESC;

-- 4. Which books had the greatest longevity on the list?
CREATE OR ALTER VIEW top_longevity_books AS
SELECT TOP 20
    b.title,
    b.author,
    MAX(a.weeks_on_list) AS peak_weeks
FROM appearances a
JOIN books b ON a.isbn13 = b.isbn13
GROUP BY b.isbn13, b.title, b.author
ORDER BY peak_weeks DESC;

-- 5. Which books hit #1 the fastest after debut?
CREATE OR ALTER VIEW fastest_to_number_1 AS
WITH ranked AS (
    SELECT
        b.title,
        b.author,
        a.list_date,
        a.rank,
        ROW_NUMBER() OVER (PARTITION BY b.isbn13 ORDER BY a.list_date) AS first_week
    FROM appearances a
    JOIN books b ON a.isbn13 = b.isbn13
)
SELECT TOP 20
    title,
    author,
    list_date AS date_hit_1,
    first_week AS week_number
FROM ranked
WHERE rank = 1
ORDER BY week_number ASC;

-- 6. Which titles had the most volatile rank changes week-to-week?
CREATE OR ALTER VIEW most_volatile_books AS
WITH ordered AS (
    SELECT
        a.isbn13,
        b.title,
        b.author,
        a.list_date,
        a.rank,
        LAG(a.rank) OVER (PARTITION BY a.isbn13 ORDER BY a.list_date) AS prev_rank
    FROM appearances a
    JOIN books b ON a.isbn13 = b.isbn13
)
SELECT TOP 20
    title,
    author,
    list_date,
    rank,
    prev_rank,
    (prev_rank - rank) AS rank_change
FROM ordered
WHERE prev_rank IS NOT NULL
ORDER BY ABS(rank_change) DESC;

-- 7. What seasonal trends exist in new book entries? When are most bestsellers debuting?
CREATE OR ALTER VIEW seasonal_trends AS
SELECT
    MONTH(list_date) AS month,
    COUNT(*) AS new_entries
FROM (
    SELECT
        isbn13,
        MIN(list_date) AS list_date
    FROM appearances
    GROUP BY isbn13
) AS debut
GROUP BY MONTH(list_date)
ORDER BY month;

-- 8. What yearly trends exist in average weeks on the list? Is the market getting more competitive?
CREATE OR ALTER VIEW yearly_avg_weeks AS
SELECT
    YEAR(list_date) AS year,
    AVG(weeks_on_list) AS avg_weeks
FROM appearances
GROUP BY YEAR(list_date)
ORDER BY year;

-- 9. What is market turnover like? How many new books enter the list each year?
CREATE OR ALTER VIEW market_turnover AS
SELECT
    YEAR(MIN(list_date)) AS year,
    COUNT(*) AS new_books
FROM appearances
GROUP BY isbn13
ORDER BY year;

-- 10. Which books debut the highest on the list?
CREATE OR ALTER VIEW highest_debut_books AS
WITH debut AS (
    SELECT
        b.title,
        b.author,
        MIN(a.list_date) AS debut_date,
        MIN(a.rank) AS debut_rank
    FROM appearances a
    JOIN books b ON a.isbn13 = b.isbn13
    GROUP BY b.isbn13, b.title, b.author
)
SELECT TOP 20 *
FROM debut
ORDER BY debut_rank ASC;

-- 11. Which authors had repeat success on the list?
CREATE OR ALTER VIEW repeat_success_authors AS
SELECT
    author,
    COUNT(DISTINCT title) AS total_titles,
    SUM(weeks_on_list) AS total_weeks
FROM books b
JOIN appearances a ON a.isbn13 = b.isbn13
GROUP BY author
HAVING COUNT(DISTINCT title) >= 2
ORDER BY total_weeks DESC;

-- 12. Which books had the most consistent popularity (least rank fluctuation)?
CREATE OR ALTER VIEW most_consistent_books AS
WITH diffs AS (
    SELECT
        a.isbn13,
        b.title,
        b.author,
        a.list_date,
        a.rank,
        LAG(rank) OVER (PARTITION BY a.isbn13 ORDER BY a.list_date) AS prev
    FROM appearances a
    JOIN books b ON a.isbn13 = b.isbn13
)
SELECT TOP 20
    title,
    author,
    AVG(ABS(rank - prev)) AS avg_rank_change
FROM diffs
WHERE prev IS NOT NULL
GROUP BY isbn13, title, author
ORDER BY avg_rank_change ASC;
