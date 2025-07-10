import argparse
from network import scan_network
from fingerprint import fingerprint_devices
from vuln_check import check_vulnerabilities
from report import generate_report

def main():
    parser = argparse.ArgumentParser(description="IoT Device Vulnerability Scanner")
    parser.add_argument("--network", required=True, help="Network range to scan (e.g., 192.168.1.0/24)")
    parser.add_argument("--output", default="report.md", help="Output report file")
    args = parser.parse_args()

    print(f"[+] Scanning network: {args.network}")
    devices = scan_network(args.network)
    print(f"[+] Found {len(devices)} devices. Fingerprinting...")

    fingerprinted = fingerprint_devices(devices)
    print(f"[+] Checking for vulnerabilities...")

    results = check_vulnerabilities(fingerprinted)
    print(f"[+] Generating report at {args.output} ...")

    generate_report(results, args.output)
    print("[+] Done.")

if __name__ == "__main__":
    main()
