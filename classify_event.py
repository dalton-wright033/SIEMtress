def classify_event(line):
    line = line.lower()

    if "failed password" in line:
        return "Failed Logins"

    if "accepted password" in line:
        return "Successful Logins"

    if "accepted publickey" in line:
        return "Successful Public Key Logins"

    return None