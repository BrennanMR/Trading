## STRATEGY FILE HAS TO BE strategy.py

from indicators import *
import yfinance as yf
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Backtester.main import *

backtestMode = False 

# Backtest Mode
if backtestMode:
    pass 

# Live mode
if not backtestMode:
    pass