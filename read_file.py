from os import sep
from pathlib import Path
import csv
from pickle import TRUE

filepath1=Path.cwd()/"csv_reports"/"Cash On Hand.csv"
def processcoh():
    with filepath1.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        coh=0
        anotherlist=[]
        for row in reader:
            if day==0:
                day=int(row[0])+1
                coh=int(row[1])
            elif day<int(row[0])+1:
                if coh>int(row[1]):
                    cohdiff=coh-int(row[1])
                    anotherlist.append(f"[CASH DEFICIT] US${cohdiff} on day {day}")
                    day=int(row[0])+1
                    coh=int(row[1])
                elif coh<int(row[1]):
                    coh=int(row[1])
                    day=int(row[0])+1
        return anotherlist



filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
def processovrhds():
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        expense=0
        for row in reader:
            if expense<float(row[1]):
                expense=float(row[1])
                return(f"[HIGHEST OVERHEADS] {row[0]}: US${row[1]}")



filepath3=Path.cwd()/"csv_reports"/"Profit and Loss.csv"
def processproflos():
    with filepath3.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        prof=0
        for row in reader:
            if day==0:
                day=int(row[0])
                prof=int(row[4])
            elif day<int(row[0]):
                if prof>int(row[4]):
                    profdiff=prof-int(row[4])
                    day=int(row[0])
                    return(f"[PROFIT DEFICIT] US${profdiff} on day {day}")
                elif prof<int(row[4]):
                    prof=int(row[4])
                    day=int(row[0])
