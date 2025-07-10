import requests

OUI_API = "https://api.macvendors.com/"

def lookup_oui(mac):
    if not mac:
        return "Unknown"
    try:
        resp = requests.get(OUI_API + mac)
        return resp.text
    except Exception:
        return "Unknown"

def fingerprint_devices(devices):
    for device in devices:
        device['vendor'] = lookup_oui(device['mac'])
        # Optionally, add port scan for further fingerprinting
    return devices
