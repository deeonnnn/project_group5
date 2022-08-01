from api import conversion_rate 
from read_file import process_csv
from write_file import deficit_report
def main():
    conv_rate=conversion_rate()
    overheads,cash,profit,=process_csv()
    deficit_report(conv_rate,overheads,cash,profit)

main()

