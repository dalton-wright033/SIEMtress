# import re

alert_word_login = "failed password"
# TODO: add function that will update the final count according to the activity observed. Perhaps a new function for each?
# TODO: modify parser to extract information like: (Use RegEx)
#Time: 08:22:11
#Host: webserver01
#Service: sshd
#IP: 203.0.113.55

# Looks for failed login attempts in log file and counts instances.
def failed__login_attempts(file):
    with open(file, "r") as f:
            count = 0
            for line in f:
                    if alert_word_login.lower() in line.lower():
                        count += 1
                        print(f"Found '{alert_word_login.lower()}' in {line}")
            print(f"{count} failed login attempts.")

failed__login_attempts("sample.txt")