def generate_report(devices, filename):
    with open(filename, "w") as f:
        f.write("# IoT Device Vulnerability Report\n\n")
        for device in devices:
            f.write(f"## Device: {device['ip']}\n")
            f.write(f"- MAC: {device.get('mac', 'N/A')}\n")
            f.write(f"- Vendor: {device.get('vendor', 'N/A')}\n")
            vulns = device.get('vulnerabilities', [])
            if vulns:
                f.write(f"- Vulnerabilities:\n")
                for vuln in vulns:
                    cve = vuln.get('cve', {}).get('id', 'N/A')
                    desc = vuln.get('cve', {}).get('descriptions', [{}])[0].get('value', 'No description')
                    f.write(f"  - **{cve}**: {desc}\n")
            else:
                f.write("- Vulnerabilities: None found\n")
            f.write("\n")
