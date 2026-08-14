### Welcome to SIEMtress!

## SIEMtress is a Linux Syslog parser created in python

- SIEMtress has the ability to be customized to search and flag lines of Syslog files in linux for security alerts

- Its out-of-the-box functions include alerting for:
    - Failed Password Attempts
    - Successful Logins
    - Successful SSH Public Key Authentication
- Alerting for these three parameters can help a security researcher quickly identify malicious activity

- SIEMtress is also customizable. The ```alert_words``` variable is a dictionary that can be customized to find any keyword
    - To update this, add keywords to the ```alert_words``` variable as needed
    - Additonally, SIEMtress includes an event counter for faster review:
    - It is recomended to also add your ```alert_words``` variable to ```classify_event.py```
        - Such that it matches the format of:
```python
    if "failed password" in line:
        return "Failed Logins"
    ```
- It is encouraged to make changes to SIEMtress to fit your need and feel free to submit a PR to contribute to this project!
