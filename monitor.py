import json
import csv
import subprocess
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DEVICES_FILE = BASE_DIR / "devices.json"
STATUS_FILE = BASE_DIR / "status.json"
LOG_DIR = BASE_DIR / "logs"
REPORT_DIR = BASE_DIR / "reports"
CSV_FILE = LOG_DIR / "monitoring.csv"
ALERT_FILE = LOG_DIR / "alerts.log"
ALERT_FILE = LOG_DIR / "alerts.log"

LOG_DIR.mkdir(exist_ok=True)
REPORT_DIR.mkdir(exist_ok=True)

def check_device(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", "-W", "2", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=4
        )
        return "UP" if result.returncode == 0 else "DOWN"
    except (subprocess.TimeoutExpired, OSError):
        return "DOWN"

def main():
    with open(DEVICES_FILE, encoding="utf-8") as f:
        devices = json.load(f)["devices"]

    try:
        with open(STATUS_FILE, encoding="utf-8") as f:
            previous = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        previous = {}

    current = {}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if f.tell() == 0:
            writer.writerow(["Timestamp", "Device", "IP Address", "Status"])

        for device in devices:
            name = device["name"]
            ip = device["ip"]
            status = check_device(ip)
            current[name] = status

            print(f"[{timestamp}] {name} ({ip}) : {status}")

            writer.writerow([timestamp, name, ip, status])

            if name in previous and previous[name] != status:
                message = (
                    f"[{timestamp}] ALERT: {name} ({ip}) changed "
                    f"from {previous[name]} to {status}!"
                )
                print(message)
                with ALERT_FILE.open("a", encoding="utf-8") as alert_log:
                    alert_log.write(message + "\\n")

            elif name not in previous:
                print(f"INFO: First status recorded for {name}: {status}")

    with open(STATUS_FILE, "w", encoding="utf-8") as f:
        json.dump(current, f, indent=2)

    print(f"\nResults saved to: {CSV_FILE}")
    print(f"Current status saved to: {STATUS_FILE}")

if __name__ == "__main__":
    main()
