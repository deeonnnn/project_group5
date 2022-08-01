from api import apifunction
from read_file import processcoh, processovrhds, processproflos
from pathlib import Path
textfile=Path.cwd()/"deficit_report.txt"
# print(processproflos())

def writingfunc():
    with textfile.open(mode="w", encoding="UTF-8", newline="")as file:
        file.writelines(processovrhds())
        file.writelines(processcoh())
        file.writelines(processproflos())
        file.writelines(apifunction())

print(writingfunc())

