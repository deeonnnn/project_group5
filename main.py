import api, cash_on_hand, overheads, profit_loss

print("Hello World! This is our Team's solution!")

def add():
    print("This is function add")
    return

def delete():
    print("This is function delete")
    return

def multiply():
    print("This is function multiply")
    return
add()
delete()
multiply()

from api import mean_forex_closing_price
from read_file import process_csv_file
from write_file import report_deficit


def main():
    avg_cp = mean_forex_closing_price()
    