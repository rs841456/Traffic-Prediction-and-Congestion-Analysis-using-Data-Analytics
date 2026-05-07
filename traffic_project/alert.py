def check_alert(vehicle_count, avg_speed, location):
    if vehicle_count > 150:
        print(f"⚠️ HIGH TRAFFIC ALERT at {location}")

    if avg_speed < 10:
        print(f"🚨 SEVERE CONGESTION at {location}")