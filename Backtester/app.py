import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.colorEngine import *

def getBacktestLength():
    printBoldBlue("Backtest Length: ", end='')
    backtestLength = input()
    return backtestLength

def getPeriod():
    while True:
        backtestLength = getBacktestLength()  # read input fresh every loop
        try:
            days = int(backtestLength)
            return days
        except Exception:
            printBoldRed("⚠️   Error: Invalid input for backtestLength. Please enter a valid integer.")

# Get validated input
days = getPeriod()

# Determine period based on days
period = (
    days if days <= 30 else
    90 if days <= 90 else
    180 if days <= 180 else
    365 if days <= 365 else
    730 if days <= 730 else
    1825 if days <= 1825 else
    99999
)

periodStr = (
    f"{int(days)}d" if days <= 30 else
    "3mo" if days <= 90 else
    "6mo" if days <= 180 else
    "1y" if days <= 365 else
    "2y" if days <= 730 else
    "5y" if days <= 1825 else
    "max"
    )


