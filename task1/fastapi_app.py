from fastapi import FastAPI
import yfinance as yf

app = FastAPI()

@app.get("/stocks/")
def read_stock(ticker: str, start_date: str, end_date: str, interval: str):
    data = yf.download(ticker, start=start_date, end=end_date, interval=interval)
    return data.to_dict()