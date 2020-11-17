# FinancialMarkets_Price_Volume

A data analysis and presentation based program using ranges (derived from price/volume/volatility) and live closing price/volume metrics.

The purpose of the project was to clearly present up-to-date financial market information in conjunction with self-generated data (proprietary price ranges). The user can swiftly access a visual representation of the daily rate of change of price and volume.


# Technologies

- Language: Python 3.8.3

- Editor Used: PyCharm

- Libraries:
    > Yfinance
    > Datetime
    > MatPlotLib
    > Pandas


## Setup

The excel file containing the ranges is required to be stored on the user’s directory. This file has several tabs that are used outside the scope of this program as well. This is not attached, however a screenshot of the program outputs is included below.


## Walkthrough

Time Clamp:

A final time point is defined using ‘timedelta’ and ‘strftime’. This enables the user to access up-to-date data whenever the program is executed.


Dataframe:

Daily closing prices (in addition to trading volume) from several asset classes are extracted using yfinance and are placed into a dataframe. Pre-existing price ranges (based on price/volume/volatility of the asset) are accessed from an excel file using pandas. 
All data-frames are then joined so as to create a single data-frame with the following columns:
1.	Date (index)
2.	Low end range
3.	Live closing price
4.	Top end range

Instruments:

Six financial instruments are defined using the ‘riskranges’ function. Yfinance requires specific ticker codes which are used in the ‘ticker’ argument.

Volume Data:

Due to limited access with volume data, there are only 2 instruments that are used for this function (‘SV/DAV’ objects). Volume data is not always provided for certain futures/options based indices (i.e. VIX volatility index).

Plots:

The plots are derived using MatPlotLib (line charts). Two functions (‘graphwithvolume’ and ‘graph’) are used to display 6 figures, 4 of which are single plots and 2 of which are dual plots (including price and volume). 
The user is able to gain a visual insight into the rate of change of price movements and the relationship of this with the dynamic ranges provided. This is used to aid investing/trading decision making.


# Screenshot

![Plot Example](https://user-images.githubusercontent.com/72507931/99262415-dcdfa280-2815-11eb-8ab6-244a77a2d8f2.JPG)


## Status

Project completed.
