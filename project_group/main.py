import api,coh,overheads,profit_loss
from pathlib import Path
def main():
    """
        This function checks if there is an error in the api request, if so,
        the program will print API REQUEST ERROR FOUND and end the function.
        If there is no error, the function will input the exchange rate extracted into
        the csv functions and will create a summary report text file and write the data
    """
    
    forex=api.api_function()
    
    # api_function returns string: API REQUEST ERROR FOUND if response was not successful
    # this condition prevents the program fom crashing and maintains the flow by ending the program there
    if forex == "API REQUEST ERROR FOUND":
        print(forex)
    
    else:
        textfile=Path.cwd()/"summary_report.txt"
        textfile.touch()
        
        #this part writes the returned formatted data from the functions into the text file we created
        #it also formats the exchange rate returned from api_function
        with textfile.open(mode="w", encoding="UTF-8", newline="")as file:
            
            file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n")

            file.writelines(overheads.overhead_function(forex))

            file.writelines(coh.coh_function(forex))

            file.writelines(profit_loss.profitloss_function(forex))

main()
