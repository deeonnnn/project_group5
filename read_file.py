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
        CashSurplus=1
        listofdeficit=[]
        for row in reader:
            if day==0:
                day=int(row[0])+1
                coh=int(row[1])
            elif day<int(row[0])+1:
                if coh>int(row[1]):
                    cohdiff=coh-int(row[1])
                    listofdeficit.append(f"[CASH DEFICIT] US${cohdiff} on day {day}\n")
                    day=int(row[0])+1
                    coh=int(row[1])
                    CashSurplus=0
                elif coh<int(row[1]):
                    coh=int(row[1])
                    day=int(row[0])+1
    if CashSurplus==0:
        return listofdeficit
    else:
        cashsurplus="[CASH SURPLUS] Cash on hand on each period is higher than the previous period.\n"
        return cashsurplus





filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
def processovrhds():
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        expense=0
        for row in reader:
            if expense<float(row[1]):
                expense=float(row[1])
                return(f"[HIGHEST OVERHEADS] {row[0]}: US${row[1]}\n")



filepath3=Path.cwd()/"csv_reports"/"Profit and Loss.csv"
def processproflos():
    with filepath3.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        prof=0
        listofdeficit=[]
        profitsurplus=1
        for row in reader:
            if day==0:
                day=int(row[0])
                prof=int(row[4])
            elif day<int(row[0]):
                if prof>int(row[4]):
                    profdiff=prof-int(row[4])
                    prof=int(row[4])
                    day=int(row[0])
                    listofdeficit.append(f"[PROFIT DEFICIT] US${profdiff} on day {day}\n")
                    profitsurplus=0
                elif prof<int(row[4]):
                    prof=int (row[4])
                    day=int(row[0])
    if profitsurplus==0:
        return listofdeficit
    else:
        profitsurplus="[PROFIT SURPLUS] Net profit on each period is higher than the previous period.\n"
        return profitsurplus   
             

     
 
