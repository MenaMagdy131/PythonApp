CREATE DATABASE IF NOT EXISTS flaskapp;
USE flaskapp;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(100),
    email VARCHAR(150) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example admin user (password hashed later) pass: Admin123
INSERT INTO users (name,email,password) VALUES ('Admin','admin@gmail.com','$2b$12$wEjYJr9mLJb6kaWvHJj9nOae3F6xRGQrtX1aC/TnnEmG9YsDk9nC6');