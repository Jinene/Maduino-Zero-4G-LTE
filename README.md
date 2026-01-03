# Maduino-Zero-4G-LTE Vehicle Tracker 🚗📡

A professional IoT project using the **Maduino Zero** with **4G LTE** connectivity to track vehicles in real-time.

---

## Features
- Collect GPS coordinates from vehicle.
- Send data via 4G LTE to a Python Flask server.
- Server stores vehicle location in CSV.
- Real-time monitoring of vehicle positions.
- Can be extended to a web map visualization.

---

## Hardware Required
- Maduino Zero board
- 4G LTE module
- GPS module
- SIM card with data

---

## Firmware Setup
1. Open `main.ino` in Arduino IDE.
2. Update `config.h` with your APN, GPS pins, and server IP.
3. Upload to Maduino Zero.

---

## Server Setup
1. Install Python dependencies:
```bash
pip install -r requirements.txt
Run server:

bash
Copier le code
python app.py
Server will start at http://localhost:5000

Endpoints:

/update_location?lat=...&lng=... → receives data from Maduino

/view_data → view all vehicle logs
