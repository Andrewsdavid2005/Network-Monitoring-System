# Network Monitoring and Alerting System

A Python-based network monitoring and alerting system built on Ubuntu Linux to monitor device reachability, detect UP/DOWN status changes, maintain monitoring logs, and generate network availability reports.

## Overview

The Network Monitoring and Alerting System is designed to simplify basic network health monitoring. It uses ICMP ping to check whether configured network devices respond, records their status with timestamps, detects status transitions, and calculates availability statistics from collected monitoring data.

The system supports automated monitoring through Linux cron, making it a useful beginner-level project for Network Engineering, Linux Administration, Python Scripting, and Network Automation.

## Architecture

```text
                    NETWORK MONITORING SYSTEM
                              |
                              v
                    Device Inventory
                       devices.json
                              |
                              v
                     Monitoring Engine
                        monitor.py
                              |
                  ICMP Ping / Reachability
                              |
                              v
                    Device Status: UP/DOWN
                              |
              +---------------+---------------+
              |               |               |
              v               v               v
        Status Tracking   CSV Monitoring   Status Change
         status.json         Logs             Alerts
                              |             alerts.log
                              v
                       Availability Report
                           report.py
                              |
                              v
                 reports/availability_report.csv

                  Linux Cron Scheduler
                 Automatic periodic checks
```

## Features

- **Network Reachability Monitoring:** Checks configured IP addresses using the Linux `ping` command.
- **Device Status Detection:** Identifies devices as UP or DOWN based on ping responses.
- **Status Change Detection:** Compares current device status with previously recorded status.
- **Timestamped Logging:** Stores monitoring results in CSV format.
- **Alert Logging:** Records detected status transitions in a dedicated alert log.
- **Availability Reporting:** Calculates successful checks, failed checks, total checks, and availability percentage.
- **JSON Device Inventory:** Makes it easy to configure monitoring targets.
- **Linux Cron Automation:** Runs monitoring checks automatically at scheduled intervals.
- **Local Report Storage:** Saves monitoring history and generated reports locally.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Monitoring logic and report generation |
| Ubuntu Linux | Development and execution environment |
| ICMP / Ping | Network reachability checks |
| JSON | Device configuration and previous status storage |
| CSV | Monitoring history and availability reports |
| Linux Cron | Scheduled monitoring |
| Git and GitHub | Version control and project hosting |

## Project Structure

```text
Network-Monitoring-System/
├── monitor.py
├── report.py
├── devices.json
├── status.json
├── requirements.txt
├── README.md
├── .gitignore
├── logs/
│   ├── monitoring.csv
│   ├── alerts.log
│   └── cron.log
└── reports/
    └── availability_report.csv
```

- `monitor.py` — Checks device reachability, logs results, and detects status changes.
- `report.py` — Generates an availability report from monitoring history.
- `devices.json` — Contains the configured monitoring targets.
- `status.json` — Stores the latest known state of each device.
- `logs/monitoring.csv` — Stores timestamped monitoring results.
- `logs/alerts.log` — Stores detected status changes.
- `logs/cron.log` — Stores output from scheduled monitoring runs.
- `reports/availability_report.csv` — Contains calculated availability statistics.
- `requirements.txt` — Lists additional Python dependencies, if any.

## System Requirements

- Ubuntu Linux or another compatible Linux distribution
- Python 3
- Linux `ping` utility
- Linux cron service
- Git (optional, for version control)

The current implementation uses Python standard-library modules and does not require third-party Python packages.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Andrewsdavid2005/Network-Monitoring-System.git
cd Network-Monitoring-System
```

### 2. Check Python

```bash
python3 --version
```

### 3. Configure monitoring targets

Edit `devices.json`:

```json
{
  "devices": [
    {
      "name": "Ubuntu",
      "ip": "127.0.0.1"
    },
    {
      "name": "Network Gateway",
      "ip": "10.0.3.2"
    },
    {
      "name": "Internet DNS",
      "ip": "1.1.1.1"
    }
  ]
}
```

Replace the example IP addresses with targets that are reachable from your Linux machine.

### 4. Run the monitoring system

```bash
python3 monitor.py
```

### 5. Generate an availability report

```bash
python3 report.py
```

### 6. View monitoring results

```bash
cat logs/monitoring.csv
cat status.json
cat reports/availability_report.csv
```

View status-change alerts, if recorded:

```bash
cat logs/alerts.log
```

## Automating Monitoring with Cron

To run the monitoring script every minute, open the user's crontab:

```bash
crontab -e
```

Add the following line:

```cron
* * * * * /usr/bin/python3 /home/ubuntu/Network-Monitoring-System/monitor.py >> /home/ubuntu/Network-Monitoring-System/logs/cron.log 2>&1
```

Save the crontab and verify it:

```bash
crontab -l
```

Check scheduled execution logs:

```bash
tail -n 30 logs/cron.log
```

Update the paths if your project is stored in a different directory. The Linux VM must be running for the scheduled checks to execute.

## Availability Calculation

The report generator calculates availability using the following formula:

**Availability (%) = (Successful Checks / Total Valid Checks) × 100**

For example, if a device responds successfully to 95 out of 100 checks, its measured availability is 95%.

This percentage reflects the collected ping-check results, not a guaranteed measurement of real-world service uptime.

## Example Output

```text
[2026-10-21 10:00:00] Ubuntu (127.0.0.1) : UP
[2026-10-21 10:00:00] Network Gateway (10.0.3.2) : UP
[2026-10-21 10:00:00] Internet DNS (1.1.1.1) : UP

Monitoring results saved to:
.../logs/monitoring.csv
```

Actual output depends on network connectivity and the configured targets.

## Learning Outcomes

Through this project, I practised:

- Network reachability testing and troubleshooting
- Python subprocess execution
- Linux command-line administration
- JSON configuration management
- CSV logging and data processing
- Basic availability analysis
- Linux cron scheduling
- Git and GitHub project management

## Limitations

- ICMP ping may be blocked by firewalls even when a device is operating normally.
- The current implementation checks reachability rather than application-level service health.
- Availability statistics are based on recorded checks and can be affected by missing data.
- The current alert mechanism writes status-change events to a local log; it does not provide email or SMS notifications.
- The project does not currently include a web dashboard, SNMP polling, or automatic network-device recovery.

## Future Enhancements

- Email and Telegram notifications
- Real-time web dashboard
- Device latency and packet-loss tracking
- SNMP-based network monitoring
- Historical uptime charts
- Network topology visualization
- Monitoring of HTTP, SSH, and other service ports
- Role-based access and multi-user support

## Author

**Andrews GnanaSelvin D**

Computer Science and Engineering Student  
Interested in Network Engineering, Linux Administration, and Network Automation.

- GitHub: https://github.com/Andrewsdavid2005
- LinkedIn: https://www.linkedin.com/in/andrews-gnana-selvin-d

---

*This project was developed as a practical learning exercise in network monitoring, Linux administration, and Python scripting.*
