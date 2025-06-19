# Welcome to backlogic!
The file strategy.py is where your logic for your strategy will go. To backtest it, simply import ../Backtester/main * to be able to use the function `backtest`. The only argument required is the position you wish to use (either `'long'`,  `None`, or  `'short'`. To print the results of your backtest run `printSummary()`.
indicators.py already has two indicators prebuilt for you (RSI and MA). Both need historical prices as the first argument, and length as the second. Historical prices must be ordered under the following structure: `[a, b, c, d]`.

You will not be able to use an interval less than or equal to 15m for backtesting (to resolve this, switch any references to "max" when collecting price data, and instead make them any period below 60)
