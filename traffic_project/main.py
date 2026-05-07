import random
import time
from datetime import datetime
from db_config import connect_db
from alert import check_alert
from predict_module import predict_traffic
locations = ["Signal 1", "Signal 2", "Signal 3"]

traffic_history = []

conn = connect_db()
cursor = conn.cursor()

while True:
    location = random.choice(locations)
    vehicle_count = random.randint(50, 200)
    avg_speed = random.randint(5, 60)

    # Congestion logic
    if vehicle_count > 150:
        congestion = "High"
    elif vehicle_count > 80:
        congestion = "Medium"
    else:
        congestion = "Low"

    # Insert into DB
    query = """
INSERT INTO traffic_data (location, vehicle_count, avg_speed, congestion_level)
VALUES (?, ?, ?, ?)
"""
    cursor.execute(query, (location, vehicle_count, avg_speed, congestion))
    conn.commit()

    print(f"{datetime.now()} | {location} | Vehicles: {vehicle_count} | Speed: {avg_speed}")

    # Alert system
    check_alert(vehicle_count, avg_speed, location)

    # Store for prediction
    traffic_history.append(vehicle_count)

    # Keep last 20 values
    if len(traffic_history) > 20:
        traffic_history.pop(0)

    # Run prediction every 5 cycles
    if len(traffic_history) >= 10:
        predict_traffic(traffic_history)

    # Smart signal logic
    if congestion == "High":
        print("🚦 Signal Time: 60 sec")
    elif congestion == "Medium":
        print("🚦 Signal Time: 40 sec")
    else:
        print("🚦 Signal Time: 20 sec")

    print("-" * 50)

    time.sleep(5)