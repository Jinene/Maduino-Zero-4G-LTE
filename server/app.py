from flask import Flask, request, jsonify
import csv
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = "data/vehicle_data.csv"

# Ensure CSV exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Latitude", "Longitude"])

@app.route("/update_location", methods=['GET'])
def update_location():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    if lat and lng:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DATA_FILE, mode='a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, lat, lng])
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "failed"}), 400

@app.route("/view_data", methods=['GET'])
def view_data():
    with open(DATA_FILE) as f:
        data = list(csv.DictReader(f))
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
