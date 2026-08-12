import re
import sys

# get file path directly from command line.
file = sys.argv[1]

# TODO: Clean up magic numbers (e.g. part[8])
# TODO: Consider: Can I eliminate duplicate .split() calls?; Can I make the output prettier?; Can I avoid hardcoded indexes where possible?;
        # Can I gracefully handle a malformed line instead of crashing?

# Looks for failed login attempts in log file and counts instances.
def failed_logins(file):
    try:
        alert_failed_password = "failed password"
        with open(file, "r") as f:
                count = 0
                for line in f:
                        if alert_failed_password.lower() in line.lower():
                            count += 1
                            part = line.split()
                            IP = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
                            port = line.split('from')[1].split()[2]
                            # Prints Alert info in clean rows
                            print(f"Alert: {part[5]} {part[6]}")
                            print(f"Date: {part[0]} {part[1]}")
                            print(f"Time: {part[2]}")
                            print(f"Host: {part[3]}")
                            print(f"User: {part[8]}")
                            print(f"IP: {IP}:{port}\n")
                            
                print(f"** {count} failed login attempts **\n")
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")

    except:
        print("An error occurred. Please review file permissions and/or spelling")

#Find Successful Logins
def successful_logins(file):
    try:
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
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")

    except:
         print("An error occurred. Please review file permissions and/or spelling")


#Find opened SSH sessions
def SSH_session(file):
    try:
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
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")

    except:
         print("An error occurred. Please review file permissions and/or spelling")

SSH_session(file)
successful_logins(file)
failed_logins(file)