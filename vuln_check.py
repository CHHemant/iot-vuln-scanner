import requests

NVD_API = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def check_vulnerabilities(devices):
    for device in devices:
        vendor = device.get('vendor', '')
        if vendor and vendor != "Unknown":
            query = f'?keywordSearch={vendor}&resultsPerPage=3'
            try:
                resp = requests.get(NVD_API + query)
                if resp.status_code == 200 and 'vulnerabilities' in resp.json():
                    device['vulnerabilities'] = resp.json()['vulnerabilities']
                else:
                    device['vulnerabilities'] = []
            except Exception:
                device['vulnerabilities'] = []
        else:
            device['vulnerabilities'] = []
    return devices
