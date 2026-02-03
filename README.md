# 📈 Stock Market Tycoon - Portfolio Simulator

A strategic investment game where you attempt to grow a $1,000 starting balance into $5,000 within 15 days. Unlike simpler trading games, this simulator features multiple assets with independent volatility, requiring you to diversify your holdings and time the market cycles to succeed.

This project focuses on teaching:
* **Parallel Data Structures:** Synchronizing a "Market" dictionary with a "Player" dictionary.
* **Percentage-Based Math:** Using floating-point multipliers to simulate realistic price fluctuations.
* **Dictionary Iteration:** Dynamically updating a global market state every turn.
* **Capital Management:** Tracking liquid cash versus illiquid assets (stocks).

---

## ✨ Features

* **Dynamic Market Engine:** Prices for Tech, Gold, and Crypto fluctuate between -20% and +30% every day.
* **Portfolio Tracking:** View your total shares and cash balance in a single dashboard.
* **Price Floors:** Built-in logic ensures stocks never drop below $10, preventing "division by zero" errors or total market collapse.
* **Time-Bound Strategy:** A strict 15-day limit adds pressure to make high-impact trades.

---

## 🚀 How to Run the Game

### 1. Prerequisites
You need **Python 3** installed.

### 2. Setup and Execution
1.  **Save the Code:** Save the script as `market_tycoon.py`.
2.  **Open Terminal:** Navigate to your project folder.
3.  **Run the Script:**
    ```bash
    python market_tycoon.py
    ```

### 3. Gameplay Instructions
1.  **Analyze the Market:** Check which stocks are currently "dipping" (low price).
2.  **[B]uy:** Enter the ticker name (TECH, GOLD, or COIN) and the quantity to buy.
3.  **[S]ell:** Liquidate your shares when the price hits a peak.
4.  **[W]ait:** If the market is down, skip a day to see if prices recover.



---

## 🧠 Code Structure Highlights

### Parallel Dictionary Syncing
This is the core "Engine." The `prices` dictionary determines the cost, while the `portfolio` dictionary determines ownership. We use the **Key** (e.g., "TECH") to link the two together.

```python
# To calculate value, we pull the quantity from one and price from the other
cost = amount * prices[ticker]
portfolio[ticker] += amount

