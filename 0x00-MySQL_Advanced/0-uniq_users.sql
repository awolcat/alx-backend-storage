-- Create users table if it doesn't already exist
CREATE TABLE IF NOT EXISTS users (
    -- Unique identifier for user
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    
    -- Email of the user
    email VARCHAR(255) NOT NULL UNIQUE,
    
    -- Name of the user
    name VARCHAR(255)
);
