IMPORTANT: This project is for educations and research purposes only. It is not investment advice. 

# portfolio-correlation-analyzer
A Python tool that analyzes stock return correlations across multiple timeframes to evaluate portfolio diversification risk.

## Purpose
This tool's purpose is to provide correlation data on an investor's portfolio, which can be used to evaluate the level of diversification and risk.

## Features
- Retrieves historical stock price data from yfinance
- Calculates daily returns
- Computes Pearson correlation values between stocks by grouping stocks in pairs
- Compares correlation values across a given timeframe
- Summarizes correlation ranges
- Generates final output, charts, for correlation analysis

## Limitations
Correlation does NOT imply or prove causation.
Correlation levels can rise during market stress, meaning that a portfolio that may appear diversified in normal periods may become less diversified during crises.

## Example Research Question
Are the historic performances of the stocks in my portfolio correlated or not? And by how much?
### Example Interpretation of Results
Historic correlation of stocks VERY HIGH --> high possibility that the stocks could rise or fall in value together in the future.

## Future Improvements
- Add portfolio risk scoring
- Build web app version

#### Developed with assistance from ChatGPT
