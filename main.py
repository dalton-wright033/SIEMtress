
import os
from dotenv import load_dotenv

load_dotenv()
file = os.getenv("FILE")

# TODO: Consider using for  nested for loops to display output info in prettier form, such as a chart
# TODO: Add other event alerts (i.e. successful logins, )
# TODO: Create variable for IP/port line to clean up code
# TODO: Clean up magic numbers (e.g. part[8])
# TODO: Consider: Can I eliminate duplicate .split() calls?; Can I make the output prettier?; Can I avoid hardcoded indexes where possible?;
        # Can I gracefully handle a malformed line instead of crashing?
# TODO: Consider either adding an input to designate target file, or adding a command line argument for target file and **exception handling
        # file = sys.argv[1] (Example: python3 main.py sample.txt)
        #   if [error]:
                #print("Error: Please enter a file path")
# Looks for failed login attempts in log file and counts instances.
def failed_logins(file):
    alert_failed_password = "failed password"
    with open(file, "r") as f:
            count = 0
            for line in f:
                    if alert_failed_password.lower() in line.lower():
                        count += 1
                        part = line.split()
                        IP = line.split('from')[1].split()[0]
                        port = line.split('from')[1].split()[2]
                        # Prints Alert info in clean rows
                        print(f"Alert: {part[5]} {part[6]}")
                        print(f"Date: {part[0]} {part[1]}")
                        print(f"Time: {part[2]}")
                        print(f"Host: {part[3]}")
                        print(f"User: {part[8]}")
                        print(f"IP: {IP}:{port}\n")
                        
            print(f"** {count} failed login attempts **\n")

def successful_logins(file):
      alert_login = "accepted password"
      with open(file, "r") as f:
            count = 0
            for line in f:
                    if alert_login.lower() in line.lower():
                        count += 1
                        part = line.split()
                        IP = line.split('from')[1].split()[0]
                        port = line.split('from')[1].split()[2]
                        # Prints Alert info in clean rows
                        print(f"Alert: {part[5]} {part[6]}")
                        print(f"Date: {part[0]} {part[1]}")
                        print(f"Time: {part[2]}")
                        print(f"Host: {part[3]}")
                        print(f"User: {part[8]}")
                        print(f"IP: {IP}:{port}\n")
                        
            print(f"** {count} successful login(s) **\n")

def SSH_session(file):
      alert_SSH = "accepted publickey"
      with open(file, "r") as f:
            count = 0
            for line in f:
                    if alert_SSH.lower() in line.lower():
                        count += 1
                        part = line.split()
                        IP = line.split('from')[1].split()[0]
                        port = line.split('from')[1].split()[2]
                        # Prints Alert info in clean rows
                        print(f"Alert: {part[5]} {part[6]}")
                        print(f"Date: {part[0]} {part[1]}")
                        print(f"Time: {part[2]}")
                        print(f"Host: {part[3]}")
                        print(f"User: {part[8]}")
                        print(f"IP: {IP}:{port}\n")
                        
            print(f"** { count} SSH sessions started **\n")
      
SSH_session(file)
successful_logins(file)
failed_logins(file)