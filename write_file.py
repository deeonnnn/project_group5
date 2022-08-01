from pathlib import Path
textfile=Path.cwd()/"deficit_report.txt"
# print(processproflos())

def deficit_report(api,overheads,cash_on_hand,profit_loss):
    with textfile.open(mode="w", encoding="UTF-8", newline="")as file:
        # file.writelines(processovrhds())
        # file.writelines(processcoh())
        # file.writelines(processproflos())
        # file.writelines(apifunction())
        file.writelines(api)
        file.writelines(overheads)
        file.writelines(cash_on_hand)
        file.writelines(profit_loss)
# print(writingfunc())

