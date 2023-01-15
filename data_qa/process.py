import yfinance as yf
from data import SYM_500
import pandas

str_SYM_500 = ""
for sym in SYM_500:
    if sym == "BRK.B" or sym == "BF.B":
        continue
    else:
        str_SYM_500 += sym + " "

data = yf.download(str_SYM_500, start="2022-01-01", end="2023-01-01")
data.to_csv("data.csv")