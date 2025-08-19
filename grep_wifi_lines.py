# grep_wifi_lines.py
with open("wifi_paragraph.txt", "r") as file:
    for line in file:
        if "Wi-Fi" in line:
            print(line.strip())
