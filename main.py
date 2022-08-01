from api import api_function
from read_file import process_cash_on_hand, process_profit_loss, process_over_heads
from write_file import deficit_report
def main():
    deficit_report(process_over_heads(), process_cash_on_hand(), process_profit_loss(), api_function())

main()

