import nmap

def scan_network(network_range):
    nm = nmap.PortScanner()
    print(f"[*] Running nmap scan on {network_range} ...")
    nm.scan(hosts=network_range, arguments='-sn')  # Ping scan, no port scan
    devices = []
    for host in nm.all_hosts():
        if 'mac' in nm[host]['addresses']:
            devices.append({
                'ip': host,
                'mac': nm[host]['addresses']['mac']
            })
        else:
            devices.append({
                'ip': host,
                'mac': None
            })
    return devices
