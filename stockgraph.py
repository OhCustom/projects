import datetime as dt
from matplotlib import pyplot as plt
from matplotlib import style
from pandas_datareader import data as pdr

import yfinance as yf

yf.pdr_override()

start = dt.datetime(2019, 1, 1)
end = dt.datetime(2023, 3, 29)


while True:
    question = input("What stock would you like the price of? ")

    if question == "q":
        break
    else:
        try:
            stock = pdr.get_data_yahoo(question, start, end)

            style.use('ggplot')
            stock['Close'].plot(figsize=(8,8), label="Google")
            plt.show()

            break
        except:
            print("invalid stock") 