import yfinance as yf

# Create a list of tickers to compare
tickers = ["MSFT", "AAPL", "ABNB"]

# Create an empty dictionary to store the fundamental data for each ticker
fundamentals = {}

# Loop through each ticker and retrieve the fundamental data
for ticker in tickers:
    # Retrieve the stock information using the yfinance library
    stock_info = yf.Ticker(ticker)
    

    # Extract the fundamental data
    # print(stock_info.info)
    print(stock_info.fast_info['marketCap'])
    fundamental_data = stock_info.info

    # Add the fundamental data to the dictionary
    fundamentals[ticker] = fundamental_data

# Print the fundamental data for each ticker
for ticker, data in fundamentals.items():
    print(f"Fundamental data for {ticker}:")
    print(f"Market Cap: {data['marketCap']}")
    print(f"Trailing P/E: {data['trailingPE']}")
    print(f"Forward P/E: {data['forwardPE']}")
    print(f"Price/Book: {data['priceToBook']}")
    print(f"Enterprise Value/Revenue: {data['enterpriseToRevenue']}")
    print(f"Enterprise Value/EBITDA: {data['enterpriseToEbitda']}")
    print("------------------------------")
