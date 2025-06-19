from indicators import *
import yfinance as yf
import sys, os, time
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Backtester.main import *

# Config
position = "long"
prices = []
interval = user_tf
ticker = user_ticker 
entriesToPrint = 5
backtestMode = True

def currentPrice(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d", interval=interval)
    if not data.empty:
        return data['Close'].iloc[-1]
    else:
        return None

# Main logic
def logic(prices, rsi=None, ma1=None, ma2=None, ma3=None, longInterest=7, shortInterest=7):
    rsi = calculateRSI(prices, 14)
    ma1 = calculateMA(prices, 20)
    ma2 = calculateMA(prices, 50)
    ma3 = calculateMA(prices, 200)

    # RSI logic
    if rsi < 35:
        shortInterest -= 0.5
    elif rsi > 65:
        longInterest -= 0.5
    else:
        if longInterest > 0:
            longInterest = 0
        if shortInterest > 0:
            shortInterest = 0

    # Bullish crossovers
    if ma1 > ma2:
        longInterest += 0.5
        shortInterest -= 1
    if ma2 > ma3:
        longInterest += 0.5
        shortInterest -= 1
    if ma1 > ma3:
        longInterest += 1
        shortInterest -= 2

    # Bearish crossovers
    if ma1 < ma2:
        shortInterest += 0.5
        longInterest -= 1
    if ma2 < ma3:
        shortInterest += 0.5
        longInterest -= 1
    if ma1 < ma3:
        shortInterest += 1
        longInterest -= 2

    if longInterest > shortInterest:
        pos = 'long'
    elif longInterest < shortInterest:
        pos = 'short'
    else:
        pos = None

    return pos, longInterest, shortInterest

# Backtest Mode
if backtestMode:
    historical_data = yf.Ticker(ticker).history(period="max")['Close'].tolist()
    for i in range(0, len(historical_data)):
        try: 
            prices = historical_data[:i]  # simulate data arriving one candle at a time
            position, longInt, shortInt = logic(prices)
            backtest(position)
        except Exception:
            pass

        if i == len(historical_data) - 1:
            printSummary()

    input("Press ENTER to exit...")
# Live Mode
if __name__ == "__main__" and not backtestMode:
    initialPrint = False
    prices.extend(yf.Ticker(ticker).history(period="max")['Close'].tolist())

    while True:
        if not initialPrint:
            printBoldYellow(f"Last {entriesToPrint} prices: {prices[-entriesToPrint:]}")
            printBoldGreen(f"20 MA: {calculateMA(prices, 20)}")
            printBoldGreen(f"50 MA: {calculateMA(prices, 50)}")
            printBoldGreen(f"200 MA: {calculateMA(prices, 200)}")
            printBoldGreen(f"RSI: {calculateRSI(prices, 14)}")
            initialPrint = True

        latest_price = currentPrice(ticker)
        if latest_price is not None and prices[-1] != latest_price:
            prices.append(latest_price)
            print(prices[-entriesToPrint:])
            position, _, _ = logic(prices)
            printBoldCyan(f"Signal: {position}")

        time.sleep(60)  # Adjust interval to your data granularity
