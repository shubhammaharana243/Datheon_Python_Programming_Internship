# Stock Portfolio Performance Tracker 📈

A Python-based stock portfolio tracking application developed as **Task 2 of the Datheon Python Programming Internship**. It allows users to enter stock tickers, purchase prices, and share quantities, fetches the latest available stock prices using `yfinance`, calculates portfolio performance, and saves the results to a CSV file.

## 🚀 Features

- **Stock Ticker Validation:** Validates stock symbols using the S&P 500 company dataset.
- **Stock Price Fetching:** Retrieves the latest available price data using `yfinance`.
- **Portfolio Calculations:** Calculates invested capital, current market value, and profit or loss for each holding.
- **Percentage Returns:** Computes the percentage gain or loss for individual stock holdings.
- **CSV Export:** Saves portfolio performance reports to `portfolio_summary.csv`.
- **Input Validation:** Handles invalid numeric inputs and invalid stock tickers.

## 🛠️ Technologies Used

- Python 3
- `csv` — for reading and writing CSV files
- `yfinance` — for retrieving stock market data
- S&P 500 Constituents CSV — for ticker validation

## 📂 Project Structure

```text
Task2/
├── portfolio.py
├── constituents.csv
├── portfolio_summary.csv
└── README.md
```

- `portfolio.py` — Main application.
- `constituents.csv` — S&P 500 company dataset used for ticker validation.
- `portfolio_summary.csv` — Generated portfolio performance report.
- `README.md` — Project documentation.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shubhammaharana243/Datheon_Python_Programming_Internship.git
cd Task2
```

Replace the placeholders with your actual GitHub repository URL and folder name.

### 2. Install the required library

```bash
python -m pip install yfinance
```

The `csv` module is included with Python and does not require a separate installation.

### 3. Prepare the dataset

Download the S&P 500 constituents dataset from:

[Download S&P 500 Constituents CSV](https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv)

Save it as `constituents.csv` in the `Task2` folder.

### 4. Run the application

```bash
python Task2/portfolio.py
```

Adjust the command if you are already inside the `Task2` directory.

## 💻 How It Works

1. The user enters the number of stock holdings to track.
2. For each holding, the user enters the ticker symbol, purchase price, and share quantity.
3. The program checks ticker symbols against the S&P 500 dataset.
4. It retrieves the latest available price data using `yfinance`.
5. It calculates the invested capital, market value, profit or loss, and percentage return.
6. It writes the results to `portfolio_summary.csv`.

## 🧮 Financial Calculations

**Invested Capital**

`Buy Price × Share Quantity`

**Current Market Value**

`Current Price × Share Quantity`

**Profit or Loss**

`Market Value − Invested Capital`

**Percentage Gain or Loss**

`(Profit or Loss ÷ Invested Capital) × 100`

## 📊 Sample Output

Example values for illustration only:

| Ticker | Invested Capital | Market Value | Profit/Loss | Return |
|---|---:|---:|---:|---:|
| AAPL | $1,000.00 | $1,250.00 | +$250.00 | +25.00% |
| MSFT | $1,200.00 | $1,080.00 | -$120.00 | -10.00% |

Your actual results will depend on the prices returned by `yfinance` and the inputs you provide.

## 📄 Output File

The generated `portfolio_summary.csv` contains the following columns:

- Ticker
- Buy Price
- Quantity
- Current Price
- Invested Capital
- Market Value
- Profit/Loss
- Gain/Loss %

## ⚠️ Notes and Limitations

- The S&P 500 dataset is used for ticker validation; it does not contain current stock prices.
- The application depends on internet access to retrieve stock prices.
- `yfinance` provides market data that may be delayed or unavailable and is not guaranteed to be real-time.
- The current implementation validates tickers against the S&P 500 dataset, so stocks outside that dataset may be rejected.
- This project is for educational purposes only and does not provide investment advice.

## 🎯 Learning Outcomes

Through this project, I practiced:

- Python functions, loops, dictionaries, and input validation.
- Reading and writing CSV files with Python's built-in `csv` module.
- Fetching stock market data with an external Python library.
- Performing financial calculations.
- Handling invalid inputs and organizing a Python project.

## 👨‍💻 Author

**Shubham Maharana**

Python Programming Intern — Datheon

---

*Developed as part of the Datheon Python Programming Internship, Task 2: Stock Portfolio Performance Tracker.*
