import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

############################### Correlation Matrix ##################################

#Define what stocks to analyze
stock_list = ["NVDA","AAPL","MSFT","AMZN","GOOG","META","TSLA","JPM","WMT"]

#Define data span 
timeperiod = "10y"

#Bring stock data from yfiance
stock_data = yf.download(stock_list, period = timeperiod)

#Extract only closing prices
closing_prices = stock_data["Close"] 

#Calculate daily percentage change 
daily_returns_percentage = closing_prices.pct_change()

#delete first row
daily_returns_percentage = daily_returns_percentage.dropna()

# Calculate correlation matrix
correlation_matrix = daily_returns_percentage.corr()

# Rename the row and column labels so Pandas does not get confused
correlation_matrix.index.name = "Stock 1"
correlation_matrix.columns.name = "Stock 2"

# Convert the correlation matrix into a simpler list of stock pairs
correlation_pairs = correlation_matrix.unstack().reset_index(name="Correlation")

correlation_pairs.columns = ["Stock 1", "Stock 2", "Correlation"]

correlation_pairs = correlation_pairs[correlation_pairs["Stock 1"] != correlation_pairs["Stock 2"]]

correlation_pairs["Pair"] = correlation_pairs.apply(lambda row: tuple(sorted([row["Stock 1"], row["Stock 2"]])), axis=1)

correlation_pairs = correlation_pairs.drop_duplicates("Pair")
correlation_pairs = correlation_pairs.drop(columns=["Pair"])

def correlation_labels(correlation):
    if correlation >= 0.8:
        return "Very strong positive correlation"
    elif correlation >= 0.7:
        return "0.7 - 0.8"
    elif correlation >= 0.6:
        return "0.6 - 0.7"
    elif correlation >= 0.5:
        return "0.5 - 0.6"
    elif correlation >= 0.4:
        return "0.4 - 0.5"
    elif correlation >= 0.3:
        return "0.3 - 0.4"
    elif correlation >= 0.2:
        return "0.2 - 0.3"
    elif correlation >= 0.1:
        return "0.1 - 0.2"
    elif correlation >= 0:
        return "0.0 - 0.1"
    elif correlation >= -0.1:
        return "0.0 - (0.1)"
    elif correlation >= -0.2:
        return "(0.1) - (0.2)"
    elif correlation >= -0.3:
        return "(0.2) - (0.3)"
    elif correlation >= -0.4:
        return "(0.3) - (0.4)"
    elif correlation >= -0.5:
        return "(0.4) - (0.5)"
    elif correlation >= -0.6:
        return "(0.5) - (0.6)"
    elif correlation >= -0.7:
        return "(0.6) - (0.7)"
    elif correlation >= -0.8:
        return "(0.7) - (0.8)"
    else:
        return "Very strong negative correlation"

correlation_pairs["Relationship Level"] = correlation_pairs["Correlation"].apply(correlation_labels)

correlation_pairs = correlation_pairs.sort_values(by="Correlation")

# Print every pair without duplicates
print("FULL CORRELATION PAIR LIST")
print("Time period:", timeperiod)
#print(correlation_pairs.to_string(index=False))

# Create summary section
total_pairs = len(correlation_pairs)

category_order = [
    "Very high positive correlation",
    "0.7 - 0.8",
    "0.6 - 0.7",
    "0.5 - 0.6",
    "0.4 - 0.5",
    "0.3 - 0.4",
    "0.2 - 0.3",
    "0.1 - 0.2",
    "0.0 - 0.1",
    "0.0 - (0.1)",
    "(0.1) - (0.2)",
    "(0.2) - (0.3)",
    "(0.3) - (0.4)",
    "(0.4) - (0.5)",
    "(0.5) - (0.6)",
    "(0.6) - (0.7)",
    "(0.7) - (0.8)",
    "Very high negative correlation"
]

summary = correlation_pairs["Relationship Level"].value_counts()

summary = summary.reindex(category_order, fill_value=0)

summary = summary.reset_index()

summary.columns = ["Relationship Level", "Number of Pairs"]

summary["Percent of Total"] = (
    summary["Number of Pairs"] / total_pairs * 100
).round(2)

# Print summary section
print("\nSUMMARY")
print("Total unique stock pairs:", total_pairs)
print(summary.to_string(index=False))

####################################################################################


