from read_file import processcoh, processovrhds, processproflos
from pathlib import Path
textfile=Path.cwd()/"deficit_report.txt"
# print(processovrhds())

def writingfunc():
    actualcoh=str(processcoh())
    actualcoh=actualcoh.strip("[""]")
    with textfile.open(mode="w", encoding="UTF-8", newline="")as file:
        file.write(actualcoh)
    pass

print(writingfunc())

