# CyberSec-Lab-Scripts
A collection of basic cybersecurity scripts in Bash, Python, and PowerShell
# CyberSec-Lab-Scripts

A collection of simple, real-world cybersecurity scripts for threat detection, network scanning, log analysis, and incident response.

Built as part of my transition into cybersecurity, this repo showcases practical skills using Bash, Python, and PowerShell. These scripts are designed for beginners and junior analysts to demonstrate hands-on ability with real-world tools and scenarios.

---

## 🔧 Scripts Included

### 🛠️ Network Scanning
- **basic_nmap_scan.sh**  
  Performs a basic TCP SYN scan with version detection using Nmap.

### 📜 Log Parsing
- **failed_login_parser.py**  
  Parses `/var/log/auth.log` to identify failed SSH login attempts.

### 🕵️‍♂️ Threat Intelligence
- **hash_lookup_script.py**  
  Queries VirusTotal API to fetch reputation data for file hashes. *(API key required)*

### 🚨 Incident Response
- **isolate_machine.ps1**  
  PowerShell script to isolate a compromised Windows host by blocking all network connections via firewall rules.

## 🧪 SIEM & Endpoint Monitoring

### `usb_insert_detector.sh`
Monitors Linux system logs for USB device insertions and logs alerts to a local file. Useful in SOC/Blue Team environments for identifying unauthorized devices.

---

## 🎯 Skills Demonstrated
- Bash scripting
- Python for automation and analysis
- PowerShell for host-level response
- Network security fundamentals
- Threat intelligence APIs
- Log analysis
- Incident containment

---

## 📫 About Me
I’m transitioning into cybersecurity with a Master’s in Information Systems (March 2026) and certifications including ISC2 CC (May 2025) and SSCP (June 2025). My goal is to contribute to a SOC or SecOps team while continuing to grow into cloud and system security.

Connect on [LinkedIn](http://linkedin.com/in/philliplgross) or reach me at `philgross22@icloud.com`.

