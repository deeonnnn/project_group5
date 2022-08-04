from pathlib import Path
import csv
def coh_function(exchange_rate):
    """
        The program will compute
        the difference in Cash-on-Hand between each
        day. If Cash-on-Hand is not consecutively higher
        each day, the program will highlight the day
        where Cash-on-Hand is lower than the previous
        day and the value difference.
    """
    
    filepath1=Path.cwd()/"csv_reports"/"Cash On Hand.csv"
   
    with filepath1.open(mode="r", encoding="UTF-8", newline="")as file:
        reader=csv.reader(file)
        next(reader)

        # day will update to column 0 (the date) corresponding to the row the forloop is on
        # coh will update to column 1 (the cash on hand) corresponding to the row the forloop is on
        # listofcashdeficit is the empty list that the function will apppend the formatted cash deficit
        day=0
        coh=0
        listofcashdeficit=[]

        # cashsurplus will turn False if conditional is ran otherwise it remains as true
        cashsurplus=True

        for row in reader:           
            if day==0:
                day=int(row[0])+1
                coh=int(row[1])
            
            elif day<int(row[0])+1:
                
                if coh>int(row[1]):
                    cohdiff=coh-int(row[1])
                # multiply cash deficit by exchange rate to convert from usd to sgd
                    listofcashdeficit.append(f"[CASH DEFICIT]  DAY: {day}, AMOUNT: SGD{round((cohdiff*exchange_rate),1)}\n")
                    day=int(row[0])+1
                    coh=int(row[1])
                # cashsurplus turns false as cash deficit is present
                    cashsurplus=False
                
                elif coh<int(row[1]):
                    coh=int(row[1])
                    day=int(row[0])+1
                # updates the coh and day variable but skips appending to the list as there is no cash deficit

    if cashsurplus:
        Cashsurplus="[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n"
        return Cashsurplus
    
    else:
        return listofcashdeficit
