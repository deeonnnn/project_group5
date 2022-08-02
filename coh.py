from pathlib import Path
import csv
def coh_function(exchange_rate):
    filepath1=Path.cwd()/"csv_reports"/"Cash On Hand.csv"
    with filepath1.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)
        day=0
        coh=0
        cashsurplus=True
        listofcashdeficit=[]
        for row in reader:
            if day==0:
                day=int(row[0])+1
                coh=int(row[1])
            elif day<int(row[0])+1:
                if coh>int(row[1]):
                    cohdiff=coh-int(row[1])
                    listofcashdeficit.append(f"[CASH DEFICIT]  DAY: {day}, AMOUNT: SGD{round((cohdiff*exchange_rate),1)}\n")
                    day=int(row[0])+1
                    coh=int(row[1])
                    cashsurplus=False
                elif coh<int(row[1]):
                    coh=int(row[1])
                    day=int(row[0])+1
    if cashsurplus:
        Cashsurplus="[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        return Cashsurplus
    else:
        return listofcashdeficit


