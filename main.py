from api import apifunction
from read_file import processcoh, processovrhds, processproflos
from write_file import deficit_report, deficit_report
def main():
    deficit_report(processovrhds(), processcoh(), processproflos(), apifunction())

main()

