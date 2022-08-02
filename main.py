import api,coh,overheads,profit_loss
from pathlib import Path
def main():
    forex=api.api_function()
    textfile=Path.cwd()/"summary_report.txt"
    textfile.touch()
    with textfile.open(mode="w", encoding="UTF-8", newline="")as file:
        
        file.writelines(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n")

        file.writelines(overheads.overhead_function(forex))

        file.writelines(coh.coh_function(forex))

        file.writelines(profit_loss.profitloss_function(forex))
main()





