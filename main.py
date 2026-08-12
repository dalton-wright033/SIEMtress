import re
import sys
import ipaddress

# get file path directly from command line.
file = sys.argv[1]

# TODO: Clean up magic numbers (e.g. part[8])
# TODO: Consider: Can I eliminate duplicate .split() calls?; Can I make the output prettier?; Can I avoid hardcoded indexes where possible?;
        # Can I gracefully handle a malformed line instead of crashing?
# TODO: Make functions modular and call within main.py

# Looks for failed login attempts in log file and counts instances.
def failed_logins(file):
    try:
        alert_failed_password = "failed password"
        with open(file, "r") as f:
                count = 0
                #looks for IPv4 address in log and only displays valid IPv4 addresses
                #ipv4_pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b'
                ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

                for line in f:
                        if alert_failed_password.lower() in line.lower():
                            count += 1
                            part = line.split()
                            IPv4 = re.findall(ipv4_pattern, line)
                            #Handles ValueError if IPv4 is invalid
                            if IPv4:
                                try:
                                    valid_IP = ipaddress.ip_address(IPv4[0])
                                except ValueError:
                                    print(f"Found invalid IP on {line}: {IPv4[0]}\n")
                                    continue
                            
                            port = line.split('from')[1].split()[2]
                            # Prints Alert info in clean rows
                            print(f"Alert: {part[5]} {part[6]}")
                            print(f"Date: {part[0]} {part[1]}")
                            print(f"Time: {part[2]}")
                            print(f"Host: {part[3]}")
                            print(f"User: {part[8]}")
                            print(f"IP: {valid_IP}:{port}\n")
                            
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
                ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
                for line in f:
                        if alert_login.lower() in line.lower():
                            count += 1
                            part = line.split()
                            IPv4 = re.findall(ipv4_pattern, line)
                            #Handles ValueError if IPv4 is invalid
                            if IPv4:
                                try:
                                    valid_IP = ipaddress.ip_address(IPv4[0])
                                except ValueError:
                                    print(f"Found invalid IP on {line}: {IPv4[0]}\n")
                                    continue
                            valid_IP = ipaddress.ip_address(IPv4[0])
                            port = line.split('from')[1].split()[2]
                            # Prints Alert info in clean rows
                            print(f"Alert: {part[5]} {part[6]}")
                            print(f"Date: {part[0]} {part[1]}")
                            print(f"Time: {part[2]}")
                            print(f"Host: {part[3]}")
                            print(f"User: {part[8]}")
                            print(f"IP: {valid_IP}:{port}\n")
                            
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
                ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
                for line in f:
                        if alert_SSH.lower() in line.lower():
                            count += 1
                            part = line.split()
                            IPv4 = re.findall(ipv4_pattern, line)
                            #Handles ValueError if IPv4 is invalid
                            if IPv4:
                                try:
                                    valid_IP = ipaddress.ip_address(IPv4[0])
                                except ValueError:
                                    print(f"Found invalid IP on {line}: {IPv4[0]}\n")
                                    continue
                            valid_IP = ipaddress.ip_address(IPv4[0])
                            port = line.split('from')[1].split()[2]
                            # Prints Alert info in clean rows
                            print(f"Alert: {part[5]} {part[6]}")
                            print(f"Date: {part[0]} {part[1]}")
                            print(f"Time: {part[2]}")
                            print(f"Host: {part[3]}")
                            print(f"User: {part[8]}")
                            print(f"IP: {valid_IP}:{port}\n")
                            
                print(f"** { count} SSH sessions started **\n")
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")

    except:
         print("An error occurred. Please review file permissions and/or spelling")

SSH_session(file)
successful_logins(file)
failed_logins(file)