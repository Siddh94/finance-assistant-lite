# agents/api_agent.py

import yfinance as yf
from typing import List, Dict

def get_stock_data(symbols: List[str]) -> Dict[str, dict]:
    results = {}
    for symbol in symbols:
        stock = yf.Ticker(symbol)
        hist = stock.history(period="2d")  # Get 2 days for AUM comparison
        try:
            results[symbol] = {
                "latest_close": hist['Close'].iloc[-1],
                "previous_close": hist['Close'].iloc[-2],
                "percent_change": ((hist['Close'].iloc[-1] - hist['Close'].iloc[-2]) / hist['Close'].iloc[-2]) * 100
            }
        except Exception as e:
            results[symbol] = {"error": str(e)}
    return results

# Test example
if __name__ == "__main__":
    symbols = ["TSM", "005930.KQ"]  # TSMC, Samsung (Korean Exchange code)
    data = get_stock_data(symbols)
    print(data)
