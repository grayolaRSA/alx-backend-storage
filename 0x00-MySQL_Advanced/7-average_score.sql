-- script to update average student marks on projects

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
  DECLARE average_value FLOAT;

-- Calculate average score
  SELECT AVG(score) INTO average_value
  FROM corrections
  WHERE user_id = user_id;

  -- Insert the average marks for each user into the users table
  UPDATE users
  SET average_score = average_value
  WHERE id = user_id;
END;
//
DELIMITER ;
