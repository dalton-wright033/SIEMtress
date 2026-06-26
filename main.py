new_log = input().lower()
file = "sample.txt"

if new_log == "new entry":
    # Adds a new line to the log
    with open(file, "a") as f:
        f.write(f"\n{new_log}\n")

    # Opens, reads, and closes file
    with open(file, "r") as f:
            print(f.read())
else:
     with open("sample.txt", "r") as f:
            print(f.read())

