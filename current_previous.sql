WITH CTE_Ratings AS (
    -- Assign row numbers to each row for each person_id ordered by date
    SELECT
        person_id,
        rating_value,
        date,
        final_flag,
        ROW_NUMBER() OVER (PARTITION BY person_id ORDER BY date DESC) AS rn
    FROM
        your_table
    WHERE
        final_flag = 1 -- Only consider rows with final flag
)
SELECT
    current.person_id,
    current.rating_value AS current_rating_value,
    current.date AS current_rating_date,
    previous.rating_value AS previous_rating_value,
    previous.date AS previous_rating_date
FROM
    CTE_Ratings AS current
LEFT JOIN
    CTE_Ratings AS previous
    ON current.person_id = previous.person_id
    AND current.rn = 1   -- Current latest rating
    AND previous.rn = 2  -- Previous rating (if exists)
WHERE
    current.rn = 1;  -- Get only the latest ratings
