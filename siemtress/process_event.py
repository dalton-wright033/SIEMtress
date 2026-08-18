from .validate_ip import validate_ip
# Validates IPv4 address
def process_event(event):
    if event["ipv4"]:
        event["ipv4"] = validate_ip(event["ipv4"]) 
        event["ip_status"] = "Valid"
        if event["ipv4"] is None:
            event["ip_status"] = "Invalid"  
    else:    
        event["ip_status"] = "Missing"
    return event

