CREATE DATABASE traffic_db;
GO

USE traffic_db;
GO

CREATE TABLE traffic_data (
    id INT IDENTITY(1,1) PRIMARY KEY,
    location VARCHAR(50),
    vehicle_count INT,
    avg_speed FLOAT,
    congestion_level VARCHAR(20),
    timestamp DATETIME DEFAULT GETDATE()
); 
select * from traffic_data;
