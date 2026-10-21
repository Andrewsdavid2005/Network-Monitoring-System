import csv
from collections import defaultdict
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "logs" / "monitoring.csv"
REPORT_FILE = BASE_DIR / "reports" / "availability_report.csv"

stats = defaultdict(lambda: {"UP": 0, "DOWN": 0})

if not CSV_FILE.exists():
    print("ERROR: Monitoring log not found. Run monitor.py first.")
    raise SystemExit(1)

with CSV_FILE.open(newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Device"]
        status = row["Status"].strip().upper()

        if status in ("UP", "DOWN"):
            stats[name][status] += 1

REPORT_FILE.parent.mkdir(exist_ok=True)

with REPORT_FILE.open("w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Generated At", "Device", "Successful Checks",
        "Failed Checks", "Total Checks", "Availability (%)"
    ])

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("\n===== NETWORK AVAILABILITY REPORT =====")

    for name, counts in sorted(stats.items()):
        up = counts["UP"]
        down = counts["DOWN"]
        total = up + down
        availability = (up / total * 100) if total else 0

        writer.writerow([
            timestamp, name, up, down, total, f"{availability:.2f}"
        ])

        print(
            f"{name}: {availability:.2f}% uptime | "
            f"UP: {up} | DOWN: {down} | Total: {total}"
        )

print(f"\nReport saved to: {REPORT_FILE}")
