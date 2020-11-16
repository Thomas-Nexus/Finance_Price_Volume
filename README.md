# FinancialMarkets_Price_Volume

> A pandas/matplotlib based programme using ranges (derived from price/volume/volatility) and live closing price/volume metrics.

> Manual inputs of proprietary price range data (upper/lower daily price bands) are inputted into an excel file. This file has several tabs that are used outside the scope of this programme as well.

> Daily closing prices (in addition to trading volume) from several cross-asset classes are extracted using yfinance and are placed into a dataframe.

> The price ranges (originally in the excel file) are placed into a dataframe where they are combined with the live price data. As a result, for each financial instrument the dataframes consists of:
1) Low end range
2) Live closing price
3) Top end range
4) In a seperate plot - Live closing volume for 2/6 instruments (volume data not provided for certain futures/options based indices).

> Matplotlib was then used to produce 6 figures to display this information.

> The programme is executed every morning (UK) where I can swiftly assess the daily rate of change of price and volume relative to proprietary ranges. This visual snapshot enables me to quickly add to or cover positions.

![Plot Example](https://user-images.githubusercontent.com/72507931/99262415-dcdfa280-2815-11eb-8ab6-244a77a2d8f2.JPG)


