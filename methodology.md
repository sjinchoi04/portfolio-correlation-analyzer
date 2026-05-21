# Methodology

## Data
The tool uses historical stock price data, preferably adjusted closing prices, to account for dividends and stock splits.

## Return Calculation
Daily returns are calculated as percentage changes in adjusted closing prices.

## Correlation Calculation
The tool calculates Pearson correlation coefficients between each pair of stocks.

A correlation close to 1 means two stocks tend to move in the same direction.  
A correlation close to 0 means the stocks have little linear relationship.  
A negative correlation means the stocks tend to move in opposite directions.

## Timeframe Comparison
The tool compares multiple timeframes, such as:
- 1 year
- 5 years
- 10 years

## Interpretation
The goal is not to predict returns. The goal is to diagnose whether a portfolio has hidden concentration risk.
