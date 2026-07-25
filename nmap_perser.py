import xml.etree.ElementTree as ET

def parse_nmap(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    results = []

    for host in root.findall("host"):
        address = host.find("address")
        ip = address.get("addr") if address is not None else "Unknown"

        ports = host.find("ports")
        if ports is None:
            continue

        for port in ports.findall("port"):
            state = port.find("state")
            service = port.find("service")

            if state is not None and state.get("state") == "open":
                results.append({
                    "IP Address": ip,
                    "Port": port.get("portid"),
                    "Protocol": port.get("protocol"),
                    "Service": service.get("name") if service is not None else "Unknown"
                })

    return results
