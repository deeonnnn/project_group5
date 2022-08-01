from read_file import processcoh, processovrhds, processproflos
from pathlib import Path
textfile=Path.cwd()/"deficit_report.txt"
# print(processproflos())

def writingfunc():
    actualcoh=processcoh()
    with textfile.open(mode="w", encoding="UTF-8", newline="")as file:
        file.writelines(actualcoh)
        actualovr=processovrhds()
        file.writelines(actualovr)
        actualpl=processproflos()
        file.writelines(actualpl)

print(writingfunc())

