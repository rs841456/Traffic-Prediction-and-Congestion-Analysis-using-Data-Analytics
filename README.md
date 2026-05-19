# 🚦 Smart Traffic Monitoring & Prediction System

A real-time traffic monitoring system that collects traffic data, detects congestion, triggers alerts, predicts future traffic using machine learning, and visualizes insights through a Power BI dashboard.

---

## 📁 Project Structure

```
traffic-monitoring/
│
├── main.py                  # Main loop: data simulation, DB insertion, signal logic
├── alert.py                 # Alert system for high traffic and severe congestion
├── db_config.py             # SQL Server database connection configuration
├── predict_module.py        # ML-based traffic prediction (Linear Regression)
├── schema.sql               # Database schema for SQL Server
├── traffic_dashboard.pbix   # Power BI dashboard for traffic visualization
└── __pycache__/             # Compiled Python bytecode
    ├── alert.cpython-312.pyc
    ├── db_config.cpython-312.pyc
    ├── predict_module.cpython-312.pyc
    └── traffic_predict_module.cpython-312.pyc
```

---

## ⚙️ Features

- **Real-Time Traffic Simulation** — Continuously generates vehicle count and speed data across multiple signal locations.
- **Congestion Classification** — Automatically labels traffic as `Low`, `Medium`, or `High` based on vehicle count thresholds.
- **Smart Signal Timing** — Dynamically adjusts traffic signal duration based on congestion level.
- **Alert System** — Prints real-time warnings for high traffic volume or severely low vehicle speed.
- **Traffic Prediction** — Uses Linear Regression (scikit-learn) to forecast the next 10 traffic readings and plots actual vs. predicted data with Matplotlib.
- **Database Integration** — Persists all traffic readings to a Microsoft SQL Server database using `pyodbc`.
- **Power BI Dashboard** — Interactive `.pbix` dashboard for visualizing historical traffic trends.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Database | Microsoft SQL Server (Express) |
| DB Driver | ODBC Driver 17 for SQL Server (`pyodbc`) |
| ML Model | Linear Regression (`scikit-learn`) |
| Visualization | Matplotlib, Power BI |

---

## 🗄️ Database Schema

```sql
CREATE DATABASE traffic_db;

CREATE TABLE traffic_data (
    id               INT IDENTITY(1,1) PRIMARY KEY,
    location         VARCHAR(50),
    vehicle_count    INT,
    avg_speed        FLOAT,
    congestion_level VARCHAR(20),
    timestamp        DATETIME DEFAULT GETDATE()
);
```

Run `schema.sql` in SQL Server Management Studio (SSMS) or Azure Data Studio to set up the database.

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.12+
- Microsoft SQL Server Express (running locally)
- ODBC Driver 17 for SQL Server
- Power BI Desktop (to open the `.pbix` dashboard)

### 2. Install Python Dependencies

```bash
pip install pyodbc numpy scikit-learn matplotlib
```

### 3. Set Up the Database

Open SQL Server Management Studio and run:

```bash
schema.sql
```

### 4. Configure the Database Connection

Edit `db_config.py` if your SQL Server instance name or database name differs:

```python
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'   # Change if needed
    'DATABASE=traffic_db;'
    'Trusted_Connection=yes;'
)
```

### 5. Run the Application

```bash
python main.py
```

The system will start collecting and inserting traffic data every **5 seconds**.

---

## 📊 How It Works

```
main.py runs in a loop every 5 seconds
    │
    ├── Randomly picks a location (Signal 1 / 2 / 3)
    ├── Generates vehicle_count and avg_speed
    ├── Classifies congestion level (Low / Medium / High)
    ├── Inserts record into SQL Server (traffic_data table)
    ├── Calls check_alert() → prints alerts if thresholds breached
    ├── Appends to traffic_history (last 20 readings)
    ├── Calls predict_traffic() every time history has ≥ 10 readings
    │       └── Trains Linear Regression → plots Actual vs Predicted
    └── Prints recommended signal timing
```

---

## 🚨 Alert Thresholds

| Condition | Threshold | Alert |
|---|---|---|
| High Traffic | `vehicle_count > 150` | ⚠️ HIGH TRAFFIC ALERT |
| Severe Congestion | `avg_speed < 10 km/h` | 🚨 SEVERE CONGESTION |

---

## 🚦 Signal Timing Logic

| Congestion Level | Vehicle Count | Signal Green Time |
|---|---|---|
| High | > 150 | 60 seconds |
| Medium | 80 – 150 | 40 seconds |
| Low | < 80 | 20 seconds |

---

## 📈 Power BI Dashboard

Open `traffic_dashboard.pbix` in **Power BI Desktop** and connect it to your local `traffic_db` SQL Server database to visualize:
- Traffic volume trends by location
- Congestion level distribution
- Average speed over time

---

## 📝 Notes

- The current `main.py` uses `random` to simulate sensor data. Replace the random generation block with real sensor/API input for production use.
- The prediction model retrains on every cycle using the last 20 readings — suitable for demonstration; consider a persistent or more advanced model for production.
- Ensure SQL Server is running before launching `main.py`, or the connection will fail on startup.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
