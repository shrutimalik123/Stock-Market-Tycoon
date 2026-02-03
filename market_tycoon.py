import random

def stock_market_game():
    # 1. Setup
    cash = 1000
    portfolio = {"TECH": 0, "GOLD": 0, "COIN": 0}
    prices = {"TECH": 100, "GOLD": 200, "COIN": 50}
    
    print("--- 📈 Stock Market Tycoon 📈 ---")
    print("Turn $1,000 into $5,000 to win!")

    day = 1
    while cash < 5000 and day <= 15:
        # 2. Market Volatility (Prices change every day)
        for stock in prices:
            change = random.uniform(0.8, 1.3) # Prices can drop 20% or rise 30%
            prices[stock] = int(prices[stock] * change)
            if prices[stock] < 10: prices[stock] = 10 # Prevent stocks from hitting $0

        print(f"\n--- DAY {day} ---")
        print(f"CASH: ${cash} | PORTFOLIO: {portfolio}")
        print("MARKET PRICES:")
        for s, p in prices.items():
            print(f" > {s}: ${p}")

        action = input("\n[B]uy, [S]ell, or [W]ait? ").lower().strip()

        if action == 'b':
            ticker = input("Which stock (TECH/GOLD/COIN)? ").upper()
            if ticker in prices:
                amount = int(input(f"How many units of {ticker}? "))
                cost = amount * prices[ticker]
                if cost <= cash:
                    cash -= cost
                    portfolio[ticker] += amount
                    print(f"✅ Bought {amount} of {ticker}!")
                else:
                    print("❌ Not enough cash!")
        
        elif action == 's':
            ticker = input("Which stock? ").upper()
            if ticker in portfolio and portfolio[ticker] > 0:
                amount = int(input(f"How many units to sell (Max {portfolio[ticker]})? "))
                if amount <= portfolio[ticker]:
                    earnings = amount * prices[ticker]
                    cash += earnings
                    portfolio[ticker] -= amount
                    print(f"💰 Sold for ${earnings}!")
                else:
                    print("❌ You don't own that many!")

        day += 1

    if cash >= 5000:
        print(f"\n🎊 VICTORY! You retired on day {day} with ${cash}!")
    else:
        print(f"\n💀 TIME UP! You failed to hit the goal. Final Wealth: ${cash}")

stock_market_game()
