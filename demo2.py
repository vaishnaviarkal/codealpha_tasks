def stock_portfolio_tracker():
    # 1. Hardcoded dictionary of stock prices
    stock_prices = {
        "AAPL": 180.0,
        "GOOGL": 140.0,
        "MSFT": 400.0,
        "AMZN": 175.0,
        "TSLA": 185.0
    }

    print("--- Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}\n")

    total_investment = 0
    portfolio_summary = []

    # 2. User Input loop
    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                
                # 3. Basic Arithmetic
                price = stock_prices[symbol]
                subtotal = price * quantity
                total_investment += subtotal
                
                portfolio_summary.append(f"{symbol}: {quantity} shares @ ${price} = ${subtotal:.2f}")
                print(f"Added {symbol} to calculation.")
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")
        else:
            print("Stock symbol not found in our price list. Try again.")

    # 4. Display Results
    print("\n--- Portfolio Summary ---")
    for item in portfolio_summary:
        print(item)
    
    final_total = f"Total Investment Value: ${total_investment:.2f}"
    print("-" * 25)
    print(final_total)

    # 5. File I/O (Optional Task)
    save = input("\nWould you like to save this to a file? (y/n): ").lower()
    if save == 'y':
        with open("portfolio_report.txt", "w") as f:
            f.write("Stock Portfolio Report\n")
            f.write("=" * 22 + "\n")
            for item in portfolio_summary:
                f.write(item + "\n")
            f.write("-" * 22 + "\n")
            f.write(final_total)
        print("Report saved to 'portfolio_report.txt'")

if __name__ == "__main__":
    stock_portfolio_tracker()