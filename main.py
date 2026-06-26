#new_log = input().lower()
file = "sample.txt"
alert_word = "failed"

# Opens, reads, looks for specific alert word and closes file
with open(file, "r") as f:
        for line in f:
                if alert_word.lower() in f:
                    print(f"Found {alert_word} in sample.txt")