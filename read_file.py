from pathlib import Path
import csv
from pickle import TRUE
filepath1=Path.cwd()/"csv_reports"/"Cash On Hand.csv"
# print(filepath1.exists())
def processcoh():
    #cashonhand
    with filepath1.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        coh=0
        anotherlist=[]
        for row in reader:
            if day==0:
                day=int(row[0])
                coh=int(row[1])
            elif day<int(row[0]):
                if coh>int(row[1]):
                    cohdiff=int(row[1])-coh
                    day=int(row[0])
                    anotherlist.append(f"[CASH DEFICIT] US${cohdiff} on day {day}")
        return anotherlist

print(processcoh())

filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
# print(filepath2.exists())
def processovrhds():
    #cashonhand
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        # for row in reader:
        #     print(row)
        expense=0
        for row in reader:
            if expense<float(row[1]):
                expense=float(row[1])
                return(f"[HIGHEST OVERHEADS] {row[0]}: US${row[1]}")

print(processovrhds())

filepath3=Path.cwd()/"csv_reports"/"Profit and Loss.csv"
def processproflos():
    with filepath3.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        prof=0
        for row in reader:
            # print(row)
            if day==0:
                day=int(row[0])
                prof=int(row[4])
            elif day<int(row[0]):
                if prof>int(row[4]):
                    profdiff=int(row[4])-prof
                    day=int(row[0])
                    return(f" [PROFIT DEFICIT]US${profdiff} on day {day}")

print(processproflos())