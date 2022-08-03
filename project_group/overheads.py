from pathlib import Path
import csv
def overhead_function(exchange_rate):
    """
        The program will find the highest
        overhead category and its value.
    """
    filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
    
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader2=csv.reader(file)
        next(reader2)
        expense=0
        expense_type=""
        for row in reader2:
            if expense<float(row[1]):
                expense=float(row[1])
                expense_type=row[0].upper()
        Highest_Overheads=f"[HIGHEST OVERHEADS] {expense_type}: SGD{round((expense*exchange_rate),1)}\n"
        return Highest_Overheads
