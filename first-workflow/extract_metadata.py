import sys
import re
import csv

if __name__ == "__main__":
    PATH = sys.argv[1]
    pattern = "(\d:\d\d)-(\d:\d\d) (.*\n)"

    with open(PATH+'metadata.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["start_hour","end_hour","activity"])
        
        txt = open(PATH+"extracted_text.txt", "r", encoding="ISO-8859-1").read()
        extracted_data = re.findall(pattern,txt)
        for data in extracted_data:
            moment = [data[0].strip(),data[1].strip(),data[2].strip()]
            writer.writerow(moment)
