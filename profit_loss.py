from pathlib import Path
import csv
def profitloss_function(exchange_rate):
    filepath3=Path.cwd()/"csv_reports"/"Profit and Loss.csv"
    with filepath3.open(mode="r", encoding="UTF-8", newline="")as file:
        reader3=csv.reader(file)
        next(reader3)
        day=0
        prof=0
        listofprofitdeficit=[]
        profitsurplus=True
        
        for row in reader3:
            if day==0:
                day=int(row[0])
                prof=int(row[4])
            elif day<int(row[0]):
                if prof>int(row[4]):
                    profdiff=prof-int(row[4])
                    prof=int(row[4])
                    day=int(row[0])
                    listofprofitdeficit.append(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: SGD{round((profdiff*exchange_rate),1)}\n")
                    profitsurplus=False
                elif prof<int(row[4]):
                    prof=int (row[4])
                    day=int(row[0])
    if profitsurplus:
        Profitsurplus="[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        return Profitsurplus
        
    else:
        return listofprofitdeficit
    
    
  
