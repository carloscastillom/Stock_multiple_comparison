from yahooquery import Ticker
import csv

# Create a list of tickers to compare
tickers = ["MSFT", "AAPL", "ABNB"]

# Create an empty list to store the fundamental data for each ticker
fundamentals = []

# Loop through each ticker and retrieve the fundamental data
for ticker in tickers:
    # Retrieve the stock information using the yahooquery library
    stock_info = Ticker(ticker)

    # Extract the fundamental data
    fundamental_data = stock_info.summary_detail[ticker]

    print("=========")
    print(ticker)
    print("=========")
    print(fundamental_data)

    # Add the fundamental data to the list
    fundamentals.append(fundamental_data)

print("all fundamentals")
print(fundamentals)

# Open a CSV file for writing
"""with open('fundamental_data.csv', 'w', newline='') as csvfile:
    # Define the header row
    fieldnames = ['Ticker', 'Market Cap', 'Trailing P/E', 'Forward P/E', 'Price/Book', 'Enterprise Value/Revenue', 'Enterprise Value/EBITDA']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header row
    writer.writeheader()

    # Write the fundamental data for each ticker
    for data in fundamentals:
        writer.writerow({'Ticker': data['symbol'], 'Market Cap': data['marketCap'], 'Trailing P/E': data['trailingPE'], 'Forward P/E': data['forwardPE'], 'Price/Book': data['priceToBook'], 'Enterprise Value/Revenue': data['enterpriseToRevenue'], 'Enterprise Value/EBITDA': data['enterpriseToEbitda']})
"""