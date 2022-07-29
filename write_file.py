from read_file import processcoh, processovrhds, processproflos
from pathlib import Path
textfile=Path.cwd()/"deficit_report.txt"

def writingfunc():
    with textfile.open(mode="r", encoding="UTF-8", newline="")as file:
        pass