import sys
from .extract_event import extract_event
from .process_event import process_event
from .classify_event import classify_event

# Alert words mutable to find specific events in log. If adding or changing, update event type in classify.py
alert_words = {
     "failed password",
     "accepted password",
     "accepted publickey"
}
def main():
    # Checks for proper tool usage in command line
    if len(sys.argv) != 2:
          print("usage: python main.py <file/file path>")
          sys.exit(1)
    
    # Get file path directly from command line.
    file = sys.argv[1]
    try:
        # opens file and searches lines for keywords in alert_words
        with open(file, "r") as f:
            event_type_count = {"Failed Logins": 0,
                                "Successful Logins": 0,
                                "Successful Public Key Logins": 0}
            for line in f:
                for alert_word in alert_words:
                    if alert_word in line.lower():
                        event = extract_event(line)
                        event = process_event(event)
                        event_type = classify_event(line)
                        if event_type:
                            # Increment event types for a total count in output
                            event_type_count[event_type] += 1
                        # Neatly output flagged event info
                        print(f"""
Date: {event["month"]} {event["day"]}
Time: {event["time"]}
Host: {event["host"]}
IP Address: {event["ipv4"]}
IP Status: {event["ip_status"]}
Port: {event["port"]}
Username: {event["username"]}
Event Type: {event_type}
""")         
            # Give total amount of flag types for quick review                  
            print(f"Failed Logins: {event_type_count['Failed Logins']}, "
                  f"Successful Logins: {event_type_count['Successful Logins']}, "
                  f"Successful Public Key Logins: {event_type_count['Successful Public Key Logins']}")
    except FileNotFoundError:
        print(f"Could not open file: {file} - "
              "Please be sure file path is correct "
              "or user has privelege to access file.")
    except Exception as e:
        print(f"An error occurred when parsing failed login attempts: {e}")

     
if __name__ == "__main__":
     main()