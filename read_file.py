from pathlib import Path
import csv
from pickle import TRUE

def process_csv():
    filepath1=Path.cwd()/"csv_reports"/"Cash On Hand.csv"
    with filepath1.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        coh=0
        CashSurplus=1
        listofcashdeficit=[]
        for row in reader:
            if day==0:
                day=int(row[0])+1
                coh=int(row[1])
            elif day<int(row[0])+1:
                if coh>int(row[1]):
                    cohdiff=coh-int(row[1])
                    listofcashdeficit.append(f"[CASH DEFICIT] US${cohdiff} on day {day}\n")
                    day=int(row[0])+1
                    coh=int(row[1])
                    CashSurplus=0
                elif coh<int(row[1]):
                    coh=int(row[1])
                    day=int(row[0])+1


    filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader2=csv.reader(file)
        next(reader2)
        expense=0
        for row in reader2:
            if expense<float(row[1]):
                expense=float(row[1])
                Highest_Overheads=f"[HIGHEST OVERHEADS] {row[0]}: US${row[1]}\n"

    filepath3=Path.cwd()/"csv_reports"/"Profit and Loss.csv"
    with filepath3.open(mode="r", encoding="UTF-8", newline="")as file:
        reader3=csv.reader(file)
        next(reader3)
        newday=0
        prof=0
        listofprofitdeficit=[]
        profitsurplus=1
        for row in reader3:
            if newday==0:
                newday=int(row[0])
                prof=int(row[4])
            elif newday<int(row[0]):
                if prof>int(row[4]):
                    profdiff=prof-int(row[4])
                    prof=int(row[4])
                    newday=int(row[0])
                    listofprofitdeficit.append(f"[PROFIT DEFICIT] US${profdiff} on day {newday}\n")
                    profitsurplus=0
                elif prof<int(row[4]):
                    prof=int (row[4])
                    newday=int(row[0])

    if CashSurplus==0 and profitsurplus==0:
        return Highest_Overheads,listofcashdeficit,listofprofitdeficit
    else:
        cashsurplus="[CASH SURPLUS] Cash on hand on each period is higher than the previous period.\n"
        profitsurplus="[PROFIT SURPLUS] Net profit on each period is higher than the previous period.\n"
        return Highest_Overheads,cashsurplus,profitsurplus

             

     
 
