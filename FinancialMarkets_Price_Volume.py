import pandas as pd
import yfinance as yf
from matplotlib import pyplot as plt
from datetime import timedelta, date

#-----------------------------------------------------------------------------------------------------------------------
# TIME CLAMP

Final_Time_Point = date.today() + timedelta(2)
Final_Time_Point.strftime('%Y-%m-%d')

#-----------------------------------------------------------------------------------------------------------------------
# COMPLETE DATA-FRAME WITH PRICE AND RANGES

def riskranges(ticker, sheet_name):
    Price = pd.DataFrame(yf.download(ticker, start='2020-04-01', end=Final_Time_Point)['Adj Close'])
    Volume = pd.DataFrame(yf.download(ticker, start='2020-04-01', end=Final_Time_Point)['Volume'])
    Cropped = Price.tail(24)
    Extract = pd.read_excel('RANGE DATA.xlsx', sheet_name=sheet_name)
    LE = Extract.iloc[0]
    TE = Extract.iloc[1]
    LE_Crop = LE.head(24)
    TE_Crop = TE.head(24)
    Date = Cropped.index
    LE_To_DF = pd.DataFrame(LE_Crop)
    TE_To_DF = pd.DataFrame(TE_Crop)
    JoinThem = LE_To_DF.join(TE_To_DF)
    JoinThem.set_index(Date, inplace=True)
    AllJoin = Cropped.join(JoinThem)                                              #COMBINED PRICE DATA WITH THE 2 RANGES
    riskranges.FINAL = AllJoin.tail(23)
    return riskranges.FINAL

#-----------------------------------------------------------------------------------------------------------------------
# ALL INSTRUMENTS FOR INPUT

S = riskranges('^GSPC', 'SPX')                                                                      #CONTAIN VOLUME DATA
DA = riskranges('^GDAXI', 'DAX')                                                                    #CONTAIN VOLUME DATA
U = riskranges('^TNX', 'US10')
G = riskranges('GC=F', 'GOLD')
DY = riskranges('DX=F', 'DXY')
V = riskranges('^VIX', 'VIX')

#-----------------------------------------------------------------------------------------------------------------------
# VOLUME DATA

def volume(ticker):
    Volume = pd.DataFrame(yf.download(ticker, start='2020-04-01', end=Final_Time_Point)['Volume'])
    LastMonth = Volume.tail(24)
    return LastMonth

SV = volume('^GSPC')
DAV = volume('^GDAXI')

#-----------------------------------------------------------------------------------------------------------------------
#DUAL PLOTS

def graphwithvolume(figure, plot1, plot2, yLow, yHigh, instrument, volume, heading, rows, cols):
    figure, (plot1, plot2) = plt.subplots(nrows=rows, ncols=cols)
    plt.style.use('seaborn')
    plot1.set_title(heading, fontsize=14)
    plot1.plot(instrument['Adj Close'], color='aliceblue', linewidth=4)
    plot1.plot(instrument[0], color='green', linestyle='--', linewidth=1.5)
    plot1.plot(instrument[1], color='red', linestyle='--', linewidth=1.5)
    plt.ylim(yLow, yHigh)
    plot1.set_facecolor("black")
    plot1.set_ylabel("Price ($)")
    plot1.set_xticklabels([])
    plot1.grid(False)

    plot2.set_title('VOLUME', fontsize=14)
    plot2.plot(volume, color="green", linewidth=3)
    plot2.set_facecolor("grey")
    plot2.set_ylabel('Millions')
    plot2.set_xticklabels([])
    plot2.grid(False)
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#SINGLE PLOTS

def graph(heading, instrument, low, high):
    ax = plt.subplot()
    plt.title(heading, fontsize=16)
    plt.plot(instrument['Adj Close'], color='white', linewidth=3)
    plt.plot(instrument[0], color='green')
    plt.plot(instrument[1], color='red')
    plt.ylim(low, high)
    plt.grid(False, color='black')
    ax.set_xticklabels([])
    ax.set_facecolor("black")
    plt.show()

#-----------------------------------------------------------------------------------------------------------------------
#FINALISE

print(graphwithvolume('fig1', 'ax1', 'ax2', 2000000000, 7000000000, S, SV, 'SPX', 2, 1))
print(graphwithvolume('fig2', 'ax3', 'ax4', 4000000, 190000000, DA, DAV, 'DAX', 2, 1))
print(graph('US10', U, 0.55, 0.95))
print(graph('GOLD', G, 1810, 2020))
print(graph('US DOLLAR', DY, 92, 96))
print(graph('VIX', V, 20, 42))

#-----------------------------------------------------------------------------------------------------------------------