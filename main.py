# TODO: Make functions modular and call within main.py
import re
import sys
import ipaddress

# get file path directly from command line.
file = sys.argv[1]
ipv4_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

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

                            month = part[0]
                            day = part[1]
                            time = part[2]
                            host = part[3]

                            port_index = part.index("port")

                            port = part[port_index + 1]

                            for_index = part.index("for")

                            if part[for_index + 1] == "invalid":
                                username = part[for_index + 3]
                            else:
                                username = part[for_index + 1]
                            IPv4 = re.findall(ipv4_pattern, line)
                            #Handles ValueError if IPv4 is invalid
                            if IPv4:
                                try:
                                    valid_IP = ipaddress.ip_address(IPv4[0])
                                except ValueError:
                                    print(f"Found invalid IP on {line}: {IPv4[0]}\n")
                                    continue
                            if not IPv4:
                                print(f"No IPv4 address found on line: {line}")
                                continue
                            # Prints Alert info in clean rows
                            print(f"Alert: {alert_failed_password.title()}")
                            print(f"Date: {month} {day}")
                            print(f"Time: {time}")
                            print(f"Host: {host}")
                            print(f"User: {username}")
                            print(f"IP: {valid_IP}:{port}\n")
                                
        print(f"** {count} failed login attempts **\n")
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")

    except:
        print("An error occurred when parsing failed login attempts: {e}")

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

                            month = part[0]
                            day = part[1]
                            time = part[2]
                            host = part[3]

                            port_index = part.index("port")

                            port = part[port_index + 1]

                            for_index = part.index("for")

                            if part[for_index + 1] == "invalid":
                                username = part[for_index + 3]
                            else:
                                username = part[for_index + 1]
                            IPv4 = re.findall(ipv4_pattern, line)
                            #Handles ValueError if IPv4 is invalid
                            if IPv4:
                                try:
                                    valid_IP = ipaddress.ip_address(IPv4[0])
                                except ValueError:
                                    print(f"Found invalid IP on {line}: {IPv4[0]}\n")
                                    continue
                            if not IPv4:
                                print(f"No IPv4 address found on line: {line}")
                                continue
                            # Prints Alert info in clean rows
                            print(f"Alert: {alert_login.title()}")
                            print(f"Date: {month} {day}")
                            print(f"Time: {time}")
                            print(f"Host: {host}")
                            print(f"User: {username}")
                            print(f"IP: {valid_IP}:{port}\n")
                            
        print(f"** {count} successful login(s) **\n")
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")

    except:
         print("An error occurred when parsing successful logins: {e}")


#Find opened SSH sessions
def SSH_session(file):
    try:
        alert_SSH = "accepted publickey"
        with open(file, "r") as f:
                count = 0               
                for line in f:
                        if alert_SSH.lower() in line.lower():
                            count += 1
                            # TODO: Refactor line information into single function
                            part = line.split()

                            month = part[0]
                            day = part[1]
                            time = part[2]
                            host = part[3]

                            port_index = part.index("port")

                            port = part[port_index + 1]

                            for_index = part.index("for")

                            if part[for_index + 1] == "invalid":
                                username = part[for_index + 3]
                            else:
                                username = part[for_index + 1]
                            IPv4 = re.findall(ipv4_pattern, line)
                            #Handles ValueError if IPv4 is invalid
                            if IPv4:
                                try:
                                    valid_IP = ipaddress.ip_address(IPv4[0])
                                except ValueError:
                                    print(f"Found invalid IP on {line}: {IPv4[0]}\n")
                                    continue
                            if not IPv4:
                                print(f"No IPv4 address found on line: {line}")
                                continue
                            # Prints Alert info in clean rows
                            print(f"Alert: {alert_SSH.title()}")
                            print(f"Date: {month} {day}")
                            print(f"Time: {time}")
                            print(f"Host: {host}")
                            print(f"User: {username}")
                            print(f"IP: {valid_IP}:{port}\n")
                            
                print(f"** { count} SSH sessions started **\n")
    except FileNotFoundError:
        print(f"Could not open file: {file} - Please besure file path is correct or user has privelege to access file.")
    # TODO: Improve error handling
    except:
         print("An error occurred when parsing SSH logins: {e}")

SSH_session(file)
successful_logins(file)
failed_logins(file)