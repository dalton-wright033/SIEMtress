# Extracts relevant information from line
import re

ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
def extract_event(line):
    extracted_data = {}

    
    
    part = line.split()

    extracted_data["month"] = part[0]
    extracted_data["day"] = part[1]
    extracted_data["time"] = part[2]
    extracted_data["host"] = part[3]
    ipv4 = re.findall(ipv4_pattern, line)
    if not ipv4:
        print(f"No IPv4 address found for {line}")
        return None
    
    extracted_data["ipv4"] = ipv4[0]
    port_index = part.index("port")

    extracted_data["port"] = part[port_index + 1]

    for_index = part.index("for")

    if part[for_index + 1] == "invalid":
        extracted_data["username"] = part[for_index + 3]
    else:
        extracted_data["username"] = part[for_index + 1]
    

    return extracted_data