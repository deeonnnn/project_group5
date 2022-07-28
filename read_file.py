from pathlib import Path
import csv
from pickle import TRUE
filepath1=Path.cwd()/"csv_reports"/"Cash On Hand.csv"
print(filepath1.exists())
def process_csv_file():
    #cashonhand
    with filepath1.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        coh=0
        for row in reader:
            if day==0:
                day=int(row[0])
                coh=int(row[1])
            elif day<int(row[0]):
                if coh>int(row[1]):
                    cohdiff=int(row[1])-coh
                    day=int(row[0])
                    print(f"{day-1}-{day}")
                    print(cohdiff)





print(process_csv_file())