import ipaddress


def validate_ip(ip):
    try:
        valid_IP = ipaddress.ip_address(ip)
    except ValueError:
        return None
    return str(valid_IP)
