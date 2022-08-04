from pathlib import Path
import csv

def profitloss_function(exchange_rate):
    """
        The program will compute
        whether we made a profit of loss.
        If we made a profit, it is True
        If we made a loss, it would be false.
    """
    filepath3=Path.cwd()/"csv_reports"/"Profit and Loss.csv"
    with filepath3.open(mode="r", encoding="UTF-8", newline="")as file:
        reader3=csv.reader(file)
        next(reader3)

        # day will update to column 0 (the date) corresponding to the row the forloop is on
        # prof will update to column 4 (the net profit) corresponding to the row the forloop is on
        # listofprofitdeficit is the empty list that the function will apppend the formatted profit deficit        
        day=0
        prof=0
        listofprofitdeficit=[]

        # profitsurplus will turn False if conditional is ran otherwise it remains as true
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
                # cashsurplus turns false as cash deficit is present

                elif prof<int(row[4]):
                    prof=int (row[4])
                    day=int(row[0])
                # updates the prof and day variable but skips appending to the list as there is no profit deficit
    
    if profitsurplus:
        Profitsurplus="[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        return Profitsurplus
        
    else:
        return listofprofitdeficit
