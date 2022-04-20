"""
Aidan Stout
lab13.py
Problem: series of problems to help us better understand searching algorithms
I certify that this is entirely my work
"""


def trade_alert(file_name):
    seconds = 1
    file = open(file_name, 'r')
    line = file.readline()
    # line = eval(line)
    trades = line.split()  # Gets a list of all the trades
    for i in trades:
        if eval(i) > 830:
            print("WARNING: More than 830 trades were made at {} second(s)".format(seconds))
        elif eval(i) == 500:
            print("ALERT: Exactly 500 trades were made at {} second(s)".format(seconds))
        seconds += 1
    file.close()


if __name__ == '__main__':
    trade_alert('trades.txt')
