import csv
import yfinance as yf

csv_file = "Task2/constituents.csv"
write_csv_file = "portfolio_summary.csv"

def file_exist_or_not():
    try:
        with open(csv_file) as file:
            pass
    except FileNotFoundError:
        print("constituents.csv file does not exist")
        return False
        
    return True

def ticker_valid_or_not(user_stocks):
    tickers_in_file = []

    pass_or_not_list = []
    pass_or_not =[]


    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tickers_in_file.append(row["Symbol"])

    for data in user_stocks:
        if data["stock_ticker"] in tickers_in_file:
            pass_or_not_list.append({"stock": data["stock_ticker"], "found": True})
        else:
            pass_or_not_list.append({"stock": data["stock_ticker"], "found": False})
    
    for stock in pass_or_not_list:
        pass_or_not.append(stock["found"])

    if False in pass_or_not and len(pass_or_not) == 1:
        print("Invalid ticker.")
        print("\nPlease enter valid information.\n")

        return False

    elif False in pass_or_not:

        print("\nour ticker list contains an invalid ticker.")
        y_or_n = input("Do you want to continue without that invalid ticker? (yes/no) ").lower()

        if y_or_n == "yes" or y_or_n =="y":

            invalid_stock = []

            for i in pass_or_not_list:
                if i["found"] == False:
                    invalid_stock.append(i["stock"])

            user_stocks =[
                stock for stock in user_stocks if stock["stock_ticker"] not in invalid_stock
            ]

            fetch_stock_data_and_calculate(user_stocks)
            return True

        else:
            print("\nEnter valid informations\n")
            return False

    else:
        print("\nCalculating...\n")
        fetch_stock_data_and_calculate(user_stocks)
        return True

def fetch_stock_data_and_calculate(user_stocks):
    current_stock_data = []
    
    for stock in user_stocks:
        try:
            stock_data= yf.Ticker(stock["stock_ticker"])

            current_price = stock_data.fast_info["lastPrice"]
            if current_price is None:
                print(f"Price unvaliable for {stock['stock_ticker']}")
                continue
        except Exception as e:
            print(f"Error fetching stock data: {e}")
            continue

        invested_capital = stock["buy_price"] * stock["share_quantity"]
        market_value = current_price * stock["share_quantity"]
        profit_or_loss = market_value - invested_capital
        try:
            gain_or_loss = (profit_or_loss/ invested_capital)*100
        except ZeroDivisionError:
            gain_or_loss = float("inf")

        data = {
            "ticker": stock["stock_ticker"],
            "buy_price": stock["buy_price"],
            "quantity": stock["share_quantity"],
            "current_price": f"{current_price:.2f}",
            "invested_capital": invested_capital,
            "market_value": f"{market_value:.2f}",
            "profit_or_loss": f"{profit_or_loss:.2f}",
            "gain_or_loss": f"{gain_or_loss:.2f}",
        }
        current_stock_data.append(data)

    write_csv(current_stock_data)

def write_csv(stock_data):
    with open(write_csv_file, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Ticker",
                "Buy Price",
                "Quantity",
                "Current Price",
                "Invested Capital",
                "Market Value",
                "Profit/Loss",
                "Gain/Loss %"
            ]
        )

        writer.writeheader()
        for data in stock_data:
            writer.writerow({
                "Ticker": data["ticker"],
                "Buy Price": data["buy_price"],
                "Quantity": data["quantity"],
                "Current Price": data["current_price"],
                "Invested Capital": data["invested_capital"],
                "Market Value": data["market_value"],
                "Profit/Loss": data["profit_or_loss"],
                "Gain/Loss %": data["gain_or_loss"]
            })

    print(f"{write_csv_file} File created successfully!")

def user_stock_data():
    user_stocks = []

    while True:
        try:    
            total_stocks = int(input("Enter number of stocks: "))
            if total_stocks <= 0:
                print("Please enter a number grater then zero.")
                continue
            break
        except ValueError:
            print("\nPlease enter a number, not text.")

    i=0

    while i<total_stocks:
        while True:
            try:
                ticker = input("\nEnter stock ticker: ").upper().strip()
                price = float(input("Enter buy price: "))
                share = int(input("Enter share quantity: "))
                if price <= 0 or share <= 0:
                    print("Buy price and share quantity must be positive.")
                    continue

                break
            except ValueError:
                print("Please enter the data in the correct format.")


        user_stocks.append({"stock_ticker": ticker, "buy_price": price, "share_quantity": share})

        i+=1

    return user_stocks

def main():
    file_found = file_exist_or_not()

    if file_found:
        user_stocks = user_stock_data()

        true_stock = ticker_valid_or_not(user_stocks)

        while not true_stock:
            user_stocks = user_stock_data()
            true_stock = ticker_valid_or_not(user_stocks)

if __name__ == "__main__":
    print("\n== Welcome to the Stock Portfolio Tracker ==\n")
    main()
