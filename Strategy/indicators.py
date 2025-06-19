import yfinance as yf
import pandas as pd

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.colorEngine import *

def calculateRSI(prices, period=14):
    if len(prices) < period + 1:
        raise ValueError("Not enough data to calculate RSI")

    gains = []
    losses = []

    # Step 1: Calculate changes between consecutive closes
    for i in range(1, period + 1):
        delta = prices[i] - prices[i - 1]
        if delta > 0:
            gains.append(delta)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(delta))

    # Step 2: Calculate average gain and loss
    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    # Step 3: Avoid division by zero
    if avg_loss == 0:
        return 100  # RSI is 100 when there's no loss

    rs = avg_gain / avg_loss

    # Step 4: Final RSI calculation
    rsi = 100 - (100 / (1 + rs))
    return rsi



def calculateMA(prices, length):
    if len(prices) < length:
        print("ERROR: Not enough data for MAs")
        return None
    return sum(prices[-length:]) / length

volatilityAverageIndex = []

volatilityAverageIndex = []

def volatility(high, low, vma=20): # VMA = Volatility Moving Average
    v = (high - low) / 100
    volatilityAverageIndex.append(v)
    recent = volatilityAverageIndex[-vma:]
    vmaCalculated = sum(recent) / len(recent)
    return vmaCalculated, v
