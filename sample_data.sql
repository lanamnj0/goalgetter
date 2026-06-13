USE goalgetter;

-- USERS
INSERT INTO users (username, email, password_hash, current_weight_kg)
VALUES
('tosin', 'tosin@email.com', 'hashedpassword1', 67.0),
('thelma', 'thelma@email.com', 'hashedpassword2', 62.5);

-- EXERCISES
INSERT INTO exercises (exercise_name, muscle_group, calories_burned)
VALUES
('Squat', 'Legs', 100),
('Push Up', 'Chest', 50),
('Plank', 'Core', 40);

-- WORKOUTS
INSERT INTO workouts (user_id, workout_date, duration_minutes, calories_burned)
VALUES
(1, '2026-06-13', 60, 350),
(2, '2026-06-13', 45, 250);

-- WORKOUT_EXERCISES
INSERT INTO workout_exercises (workout_id, exercise_id, sets, reps, weight_kg)
VALUES
(1, 1, 4, 12, 40),
(1, 3, 3, 60, 0),
(2, 2, 3, 15, 0);

-- GOALS
INSERT INTO goals (user_id, goal_type, target_value, current_value, target_date, goal_status)
VALUES
(1, 'Weight Loss', 65, 67, '2026-08-01', 'In Progress'),
(2, 'Muscle Gain', 70, 62.5, '2026-09-01', 'In Progress');

-- MEALS
INSERT INTO meals (user_id, meal_name, calories, meal_date)
VALUES
(1, 'Chicken Salad', 450, '2026-06-13'),
(2, 'Protein Oats', 350, '2026-06-13');