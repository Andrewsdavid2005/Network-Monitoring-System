# Network Monitoring and Alerting System

A Python-based network monitoring project developed on Ubuntu Linux.

## Features

- ICMP-based network device monitoring
- Automatic UP/DOWN status detection
- Network status-change alerts
- CSV monitoring logs
- Device availability reports
- Linux cron scheduling
- JSON-based device configuration

## Technologies

- Python 3
- Ubuntu Linux
- ICMP (Ping)
- JSON
- CSV
- Linux Cron
- Git and GitHub

## Project Structure

- monitor.py - Monitors network devices
- report.py - Generates availability reports
- devices.json - Stores device information
- logs/ - Stores monitoring and alert logs
- reports/ - Stores generated reports

## Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/Network-Monitoring-System.git

cd Network-Monitoring-System

## Run Monitoring

python3 monitor.py

## Generate Report

python3 report.py

## Automatic Monitoring

Schedule monitor.py using Linux cron to run every minute.

## Monitoring Targets

- Ubuntu localhost
- Network gateway
- Public DNS server

## Learning Outcomes

- Network monitoring fundamentals
- Linux administration
- Python scripting
- Network troubleshooting
- Automated reporting
- Cron job scheduling

## Future Enhancements

- Email notifications
- Telegram alerts
- Web-based monitoring dashboard
- Latency monitoring
- SNMP device monitoring
# Network-Monitoring-System
