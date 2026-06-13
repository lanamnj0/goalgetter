CREATE DATABASE goalgetter;

USE goalgetter;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(80) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    current_weight_kg DECIMAL (5,2)
);

CREATE TABLE workouts (
    workout_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    workout_date DATE NOT NULL,
    duration_minutes INT,
    calories_burned INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE exercises (
    exercise_id INT AUTO_INCREMENT PRIMARY KEY,
    exercise_name VARCHAR(100) NOT NULL,
    muscle_group VARCHAR(50),
    calories_burned INT
);

CREATE TABLE workout_exercises (
    id INT AUTO_INCREMENT PRIMARY KEY,
    workout_id INT NOT NULL,
    exercise_id INT NOT NULL,
    sets INT,
    reps INT,
    weight_kg DECIMAL(5,2),
    FOREIGN KEY (workout_id) REFERENCES workouts(workout_id),
    FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_id)
);

CREATE TABLE meals (
    meal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    meal_name VARCHAR(100) NOT NULL,
    calories INT,
    meal_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE goals (
    goal_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    goal_type VARCHAR(50) NOT NULL,
    target_value DECIMAL(10,2),
    current_value DECIMAL(10,2),
    target_date DATE,
    goal_status VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);