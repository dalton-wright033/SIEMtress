import re
import os
from dotenv import load_dotenv

load_dotenv()
file = os.getenv("FILE")

alert_word_login = "failed password"

# TODO: modify parser to extract information like: (Use string methods or RegEx?)
#Time: 08:22:11
#Host: webserver01
#Service: sshd
#IP: 203.0.113.55
#TODO: Add other event alerts (i.e. )

# Looks for failed login attempts in log file and counts instances.
def failed__login_attempts(file):
    with open(file, "r") as f:
            count = 0
            for line in f:
                    if alert_word_login.lower() in line.lower():
                        count += 1
                        part = line.split()
                        # Prints Alert info in clean rows
                        print(f"Alert: {part[5]} {part[6]}")
                        print(f"Date: {part[0]} {part[1]}")
                        print(f"Time: {part[2]}")
                        print(f"Host: {part[3]}")
                        print(f"User: {part[8]}")
                        print(f"IP: {line.split('from')[1].split()[0]}:{line.split('from')[1].split()[2]}\n")
                        
            print(f"{count} failed login attempts.")
                

failed__login_attempts(file)