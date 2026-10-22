import csv
import yfinance as yf

csv_file = "Task2/constituents.csv"
write_csv_file = "Task2/portfolio_summary.csv"

def ticker_valid_or_not(user_stocks):
    tickers_in_file = []

    pass_or_not_list = []
    pass_or_not =[]

    with open(csv_file, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            tickers_in_file.append(row["Symbol"])

    for i in range(0, len(user_stocks)):
        if user_stocks[i]["stock_ticker"] in tickers_in_file:
            pass_or_not_list.append({"stock": user_stocks[i]["stock_ticker"], "found": True})
        else:
            pass_or_not_list.append({"stock": user_stocks[i]["stock_ticker"], "found": False})

    for stock in pass_or_not_list:
        pass_or_not.append(stock["found"])

    if False in pass_or_not and len(pass_or_not) == 1:
        print("Invalid Ticker.")
        print("\nEnter valid informations\n")
        main()

    elif False in pass_or_not:

        print("\nyour ticker list have an invalid ticker")
        y_or_n = input("Do you want to continue without that invalid ticker? (yes/no) ").lower()

        if y_or_n == "yes" or y_or_n =="y":

            invalid_stock = []

            for i in pass_or_not_list:
                if i["found"] == False:
                    invalid_stock.append(i["stock_ticker"])

            for stock in user_stocks:
                if stock["stock_ticker"] in invalid_stock:
                    user_stocks.remove(stock)

            fatch_data_from_yf_and_computes(user_stocks)

        else:
            print("\nEnter valid informations\n")
            main()

def fatch_data_from_yf_and_computes(user_stocks):
    current_stock_data = []
    
    for stock in user_stocks:
        stock_data= yf.Ticker(stock["stock_ticker"])

        current_price = stock_data.fast_info["lastPrice"]
        invested_capital = stock_data["buy_price"] * stock["share_quantity"]
        market_value = current_price * stock["share_quantity"]
        profit_or_loss = market_value - invested_capital

        if profit_or_loss>0:
            gain_or_loss = (profit_or_loss/ invested_capital)*100
        elif profit_or_loss<0:
            gain_or_loss = (abs(profit_or_loss)/invested_capital)*100
        else:
            gain_or_loss = 0

        data = {
            "ticker": stock["stock_ticker"],
            "buy_price": stock["buy_price"],
            "quantity": stock["share_quantity"],
            "current_price": invested_capital,
            "market_value": market_value,
            "profit_or_loss": profit_or_loss,
            "gain_or_loss": gain_or_loss,
        }
        current_stock_data.append(data)

def write_csv(stock_data):
    pass
           
def main():
    user_stocks = []

    total_stocks = int(input("Enter number of stocks: "))

    i=0

    while i<total_stocks:
        ticker = input("\nEnter stock ticker: ").upper().strip()
        price = int(input("Enter but price: "))
        share = int(input("Enter share quantity: "))


        user_stocks.append({"stock_ticker": ticker, "buy_price": price, "share_quantity": share})

        i+=1

    ticker_valid_or_not(user_stocks)
    
if __name__ == "__main__":
    main()
