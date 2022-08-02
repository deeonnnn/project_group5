from pathlib import Path
import csv
def overhead_function(exchange_rate):
    filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader2=csv.reader(file)
        next(reader2)
        expense=0
        for row in reader2:
            if expense<float(row[1]):
                expense=float(row[1])
                Highest_Overheads=f"[HIGHEST OVERHEADS] {row[0].upper()}: SGD{round((float(row[1])*exchange_rate),1)}\n"
        return Highest_Overheads

    
