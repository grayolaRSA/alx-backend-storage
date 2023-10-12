-- script to update average student marks on projects

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
DECLARE average_value FLOAT;
-- DECLARE project_id INT;

  -- Check if the project_name exists in the projects table
  -- SELECT id INTO project_id FROM projects WHERE name = project_name;

  -- If project_name doesn't exist, create it
  -- IF project_id IS NULL THEN
   -- INSERT INTO projects (name) VALUES (project_name);
    -- SET project_id = LAST_INSERT_ID();
  -- END IF;

-- Calculate average values for each user
-- SELECT id INTO user_id FROM users WHERE id = corrections.user_id;
-- SELECT user_id, AVG(score) AS average_value
SELECT AVG(score) INTO average_value
FROM corrections
WHERE user_id = user_id;
-- GROUP BY user_id;


  -- Insert the average marks for each user into the users table
-- INSERT INTO users (average_score) VALUES (average_value)
-- WHERE user_id = user_id;
UPDATE users
SET average_score = average_value
WHERE id = user_id;
END;
//

DELIMITER ;
