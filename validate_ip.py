import extract_event as ee
import ipaddress


def validate_ip(ip):
    try:
        valid_IP = ipaddress.ip_address(ee.extracted_data["ipv4"])
    except ValueError:
        print(f"Found invalid IP on {ee.line}: {ee.extracted_data["ipv4"]}\n")
        return None
    return valid_IP
