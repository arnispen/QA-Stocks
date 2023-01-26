import yfinance as yf
from datetime import date, timedelta


stock = input("Please enter ticker of stock: ")

start_date = str(date.today() - timedelta(weeks=1))

end_date = str(date.today())

print(start_date, end_date)
data = yf.download(stock, start=start_date, end=end_date)

data.to_csv(f"{stock}.csv")