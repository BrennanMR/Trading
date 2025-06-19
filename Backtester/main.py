import sys
import os
import pandas as pd
import yfinance as yf

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config.colorEngine import * 

def fetch_historical_data(ticker: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist

printBoldCyan("Enter a stock ticker (e.g., AAPL): ", end='')
user_ticker = input("").upper()
user_tf = str(input("Timeframe (format: 1m, 1h, 1d, 1mo): "))

df = fetch_historical_data(user_ticker, period="max", interval=user_tf)
df = df.reset_index()  

# === Initialization ===
pl = 0
entryprice = 0
exitprice = 0
historicalData = []
equity_curve = []
trades = []

# === Trade & Stat Tracking ===
total_trades = 0
wins = 0
losses = 0
max_drawdown = 0
peak_equity = 0
largest_win = float('-inf')
largest_loss = float('inf')


# === Main Backtest Logic ===
def backtest(position, i=0):
    global pl, entryprice, exitprice, historicalData
    global total_trades, wins, losses, max_drawdown, peak_equity
    global largest_win, largest_loss, trades, equity_curve

    i += 1
    if i >= len(df):
        return  # Prevent out-of-bounds error

    price = df['Close'].iloc[i]
    historicalData.append(price)

    # Track equity value
    equity_curve.append(pl)
    peak_equity = max(peak_equity, pl)
    drawdown = peak_equity - pl
    max_drawdown = max(max_drawdown, drawdown)

    if position is None:
        return

    exitprice = price
    trade_pl = 0

    if position == 'long':
        trade_pl = exitprice - entryprice
    elif position == 'short':
        trade_pl = entryprice - exitprice

    pl += trade_pl
    equity_curve.append(pl)
    trades.append(trade_pl)

    # Win/loss tracking
    total_trades += 1
    if trade_pl > 0:
        wins += 1
    else:
        losses += 1

    largest_win = max(largest_win, trade_pl)
    largest_loss = min(largest_loss, trade_pl)

# === Final Stats Summary ===
def printSummary():
    printCyan("\n========== 📊 BACKTEST SUMMARY ==========")
    printBoldGreen(f"🏁 Final Total P&L: ${pl:.2f}")
    printBoldRed(f"📉 Max Drawdown: ${max_drawdown:.2f}")
    printBoldYellow(f"🧮 Total Trades: {total_trades}")
    printBoldGreen(f"✅ Wins: {wins}")
    printBoldRed(f"❌ Losses: {losses}")
    winrate = (wins / total_trades * 100) if total_trades else 0
    printBoldGreen(f"🥇 Win Rate: {winrate:.2f}%")
    avg_pl = (pl / total_trades) if total_trades else 0
    printBoldYellow(f"📈 Avg P&L per trade: ${avg_pl:.2f}")
    printBoldGreen(f"💰 Largest Win: ${largest_win:.2f}")
    printBoldRed(f"📉 Largest Loss: ${largest_loss:.2f}")
    printCyan("=========================================\n")

