from pathlib import Path
import csv
def overhead_function(exchange_rate):
    """
        The program will find the highest
        overhead category and its value.
        It will do so by running a forloop that compares all the expenses
        and will only return the largest one.
    """
    
    filepath2=Path.cwd()/"csv_reports"/"Overheads.csv"
    
    with filepath2.open(mode="r", encoding="UTF-8", newline="")as file:
        reader2=csv.reader(file)
        next(reader2)

        # expense will update to column 1 (the expense) and eventually contain the largest number.
        # expese_type will update to column 0 (the expense type) 
        # and will contain the type of expense of with the largest expense.
        expense=0
        expense_type=""
        
        # this forloop checks if the current row's expense is higher than the previous row's
        # if condition is met, it saves the row columns to expense variable and expense type
        for row in reader2:
            if expense<float(row[1]):
                expense=float(row[1])
                expense_type=row[0].upper()
        
        # expense after the forloop would have been larger than the all rows before and after it
        # multiply cash deficit by exchange rate to convert from usd to sgd
        Highest_Overheads=f"[HIGHEST OVERHEADS] {expense_type}: SGD{round((expense*exchange_rate),1)}\n"
        return Highest_Overheads
