stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 135,
    "AMZN": 145
}

portfolio = {}
total_value = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()
    if stock_name == "DONE":
        break
    if stock_name not in stock_prices:
        print("⚠ Stock not found in list, try again.")
        continue

    quantity = input("Enter quantity: ")
    if not quantity.isdigit():
        print("⚠ Please enter a valid number.")
        continue
    quantity = int(quantity)

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_value += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")

print("\n💰 Total Investment Value:", total_value)

save_choice = input("\nDo you want to save portfolio to 'portfolio.txt'? (y/n): ").lower()
if save_choice == "y":
    with open("portfolio.txt", "w") as file:
        file.write("Stock Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("✅ Portfolio saved to 'portfolio.txt'")
