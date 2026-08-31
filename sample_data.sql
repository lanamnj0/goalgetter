-- GoalGetter Moc Data
-- This script populates the database with mock data for testing and development 

USE goalgetter;
SET FOREIGN_KEY_CHECKS = 0;
TRUNCATE TABLE workout_exercises;
TRUNCATE TABLE goals;
TRUNCATE TABLE meals;
TRUNCATE TABLE exercises;
TRUNCATE TABLE workouts;
TRUNCATE TABLE users;
SET FOREIGN_KEY_CHECKS = 1;

-- USERS SAMPLE MOCK DATA
INSERT INTO users (username, email, password_hash, current_weight_kg)
VALUES
('tosin', 'tosin@email.com', 'hashedpassword1', 67.0),
('thelma', 'thelma@email.com', 'hashedpassword2', 62.5),
('lana', 'lana@email.com', 'hashedpassword3', 58.0),
('neha', 'neha@email.com', 'hashedpassword4', 60.5),
('adeyosola', 'adeyosola@email.com', 'hashedpassword5', 65.0),
('shalesa', 'shalesa@email.com', 'hashedpassword6', 63.5),
('sarah', 'sarah@email.com', 'hashedpassword7', 72.0),
('james', 'james@email.com', 'hashedpassword8', 81.5),
('alex', 'alex@email.com', 'hashedpassword9', 75.0),
('emma', 'emma@email.com', 'hashedpassword10', 63.0),
('oliver', 'oliver@email.com', 'hashedpassword11', 85.0),
('grace', 'grace@email.com', 'hashedpassword12', 59.5),
('daniel', 'daniel@email.com', 'hashedpassword13', 78.0),
('mia', 'mia@email.com', 'hashedpassword14', 55.0),
('ethan', 'ethan@email.com', 'hashedpassword15', 88.0);

SELECT * FROM users;

-- EXERCISES SAMPLE MOCK DATA
INSERT INTO exercises
    (exercise_name, body_part, target_muscle, equipment, exercise_type)
VALUES
    ('Squat', 'Thighs', 'Quadriceps', 'Barbell', 'Strength'),
    ('Push Up', 'Chest', 'Pectoralis Major', 'Body Weight', 'Strength'),
    ('Plank', 'Waist', 'Rectus Abdominis', 'Body Weight', 'Strength');

SELECT * FROM exercises;

-- WORKOUTS SAMPLE MOCK DATA
INSERT INTO workouts (user_id, workout_date, duration_minutes, calories_burned)
VALUES
(1, '2026-06-13', 60, 350),
(2, '2026-06-13', 45, 250),
(3, '2026-06-14', 50, 300),
(4, '2026-06-14', 45, 250),
(5, '2026-06-14', 60, 400),
(6, '2026-06-14', 40, 220),
(7, '2026-06-14', 55, 350),
(8, '2026-06-14', 35, 180),
(9, '2026-06-14', 70, 500),
(10, '2026-06-14', 50, 320),
(11, '2026-06-14', 45, 280),
(12, '2026-06-14', 60, 410),
(13, '2026-06-14', 40, 240),
(14, '2026-06-14', 55, 360),
(15, '2026-06-14', 65, 450);

SELECT * FROM workouts;

SELECT user_id, username
FROM users;

-- WORKOUT_EXERCISES SAMPLE MOCK DATA
INSERT INTO workout_exercises (workout_id, exercise_id, set_count, reps, weight_kg)
VALUES
    (1, 1, 4, 12, 40),
    (1, 3, 3, 60, 0),
    (2, 2, 3, 15, 0);

SELECT * FROM workout_exercises;

-- GOALS SAMPLE MOCK DATA
INSERT INTO goals (user_id, goal_type, target_value, current_value, target_date, goal_status)
VALUES
(1, 'Weight Loss', 65, 67, '2026-08-01', 'In Progress'),
(2, 'Muscle Gain', 70, 62.5, '2026-09-01', 'In Progress'),
(3, 'Weight Loss', 55, 58, '2026-08-01', 'In Progress'),
(4, 'Muscle Gain', 68, 60.5, '2026-09-01', 'In Progress'),
(5, 'Weight Loss', 60, 65, '2026-08-15', 'In Progress'),
(6, 'Weight Loss', 60, 63.5, '2026-08-15', 'In Progress'),
(7, 'Weight Loss', 68, 72, '2026-09-01', 'In Progress'),
(8, 'Muscle Gain', 85, 81.5, '2026-09-15', 'In Progress'),
(9, 'Weight Loss', 70, 75, '2026-08-20', 'In Progress'),
(10, 'Maintain Weight', 63, 63, '2026-12-01', 'In Progress'),
(11, 'Weight Loss', 80, 85, '2026-10-01', 'In Progress'),
(12, 'Maintain Weight', 60, 59.5, '2026-12-01', 'In Progress'),
(13, 'Weight Loss', 72, 78, '2026-09-15', 'In Progress'),
(14, 'Muscle Gain', 60, 55, '2026-10-01', 'In Progress'),
(15, 'Weight Loss', 82, 88, '2026-11-01', 'In Progress');

SELECT * FROM goals;

-- MEALS SAMPLE MOCK DATA
INSERT INTO meals (user_id, meal_name, calories, meal_date)
VALUES
(1, 'Chicken Salad', 450, '2026-06-13'),
(2, 'Protein Oats', 350, '2026-06-13'),
(3, 'Chicken Wrap', 500, '2026-06-14'),
(4, 'Protein Pancakes', 420, '2026-06-14'),
(5, 'Turkey Sandwich', 450, '2026-06-14'),
(6, 'Greek Yogurt Bowl', 350, '2026-06-14'),
(7, 'Salmon and Rice', 650, '2026-06-14'),
(8, 'Scrambled Eggs', 300, '2026-06-14'),
(9, 'Beef Stir Fry', 700, '2026-06-14'),
(10, 'Tuna Salad', 400, '2026-06-14'),
(11, 'Pasta Bolognese', 750, '2026-06-14'),
(12, 'Fruit Smoothie', 280, '2026-06-14'),
(13, 'Chicken and Sweet Potato', 600, '2026-06-14'),
(14, 'Protein Oats', 380, '2026-06-14'),
(15, 'Grilled Chicken Salad', 450, '2026-06-14');

SELECT * FROM meals;