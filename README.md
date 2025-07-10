# IoT Device Vulnerability Scanner

## Overview

The **IoT Device Vulnerability Scanner** is a Python-based tool designed to help users secure their home or office networks by detecting IoT (Internet of Things) devices, identifying them, checking for known vulnerabilities, and generating easy-to-understand security reports with actionable recommendations.

---

## How It Works

1. **Network Scanning:** The tool scans a specified local network range using nmap to discover all connected devices.
2. **Device Fingerprinting:** It identifies each device’s vendor and type by looking up the MAC address (OUI lookup) and optionally analyzing open ports.
3. **Vulnerability Lookup:** For each identified device, the tool queries public vulnerability databases such as NVD (CVE) to check for known security issues related to the vendor or device type.
4. **Report Generation:** A detailed Markdown report is produced, listing all devices found, their details, vulnerabilities discovered, and security recommendations.

---

## Features

- **Automatic Network Scanning:** Finds all devices on your local network.
- **Device Identification:** Uses MAC addresses to identify device vendors and types.
- **Vulnerability Detection:** Checks for known vulnerabilities using public databases (like NVD/CVE).
- **Clear Reporting:** Generates a user-friendly Markdown report with device details and vulnerabilities.
- **Actionable Recommendations:** Provides suggestions for securing each device.
- **Extensible:** Modular code makes it easy to add more fingerprinting methods, vulnerability sources, or a web dashboard.

---

## How to Use

### Prerequisites

- Python 3.8+
- [nmap](https://nmap.org/) installed and available in your system PATH
- Python libraries from `requirements.txt`
- (Optional) API keys for Shodan or other services, if you extend functionality

### Installation

```sh
git clone https://github.com/CHHemant/iot-vuln-scanner.git
cd iot-vuln-scanner
pip install -r requirements.txt
```

### Running the Scanner

Replace `192.168.1.0/24` with your own local network range:

```sh
python scanner.py --network 192.168.1.0/24
```

By default, a report will be generated as `report.md` in your project directory.

### Output

The tool outputs a Markdown file listing:
- Each device’s IP, MAC address, and vendor
- Any vulnerabilities found for the vendor/device
- Actionable steps to secure each device

---

## Who Can Use This Tool?

- **Home Users:** Easily check if your smart devices (TVs, cameras, bulbs, etc.) are vulnerable.
- **Small Businesses:** Audit office IoT devices for security risks.
- **Cybersecurity Learners:** Practice network scanning, device identification, and vulnerability research.
- **Penetration Testers:** Quickly enumerate and assess IoT devices on client networks.
- **IT Administrators:** Monitor and report on network security posture regarding IoT.

---

## Example Use Case

1. A home user runs the scanner on their WiFi network.
2. The tool finds a smart TV and a security camera.
3. It identifies that the camera vendor has a recent vulnerability listed in the NVD.
4. The report recommends updating the firmware or changing the default password.
5. The user takes action, improving their home network security.

---

## Extending the Project

- **Deeper Fingerprinting:** Add port scans or banner grabbing for more accurate device detection.
- **Additional Vulnerability Sources:** Integrate APIs from Shodan, ExploitDB, or vendor advisories.
- **Web Dashboard:** Visualize results using Flask/Django for easier management.
- **Continuous Monitoring:** Set up the scanner to run on a schedule and alert users to new vulnerabilities.

---

## Project Structure

```
iot-vuln-scanner/
├── scanner.py         # Main entry point
├── network.py         # Network scanning
├── fingerprint.py     # Device fingerprinting
├── vuln_check.py      # Vulnerability lookup
├── report.py          # Report generation
├── requirements.txt   # Python dependencies
└── README.md
```

---

## Security and Privacy

- The tool runs locally and does not send device data to third parties (unless you enable optional APIs).
- Reports are saved only on your machine.

---

## License

MIT

---

**Start securing your IoT devices today—run the IoT Device Vulnerability Scanner and get a clear view of your network’s security!**
