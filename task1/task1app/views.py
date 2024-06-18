
from django.shortcuts import render
import requests
import csv
import io

def fetch_yahoo_data(ticker, timeframe, start_date, end_date):
    url = "http://127.0.0.1:8001/fetch-data/"  
    payload = {
        "ticker": ticker,
        "timeframe": timeframe,
        "start_date": start_date,
        "end_date": end_date
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json().get("data", "")
        csv_reader = csv.reader(io.StringIO(data))
        return list(csv_reader)
    return []

def index(request):
    data = None
    if request.method == "POST":
        ticker = request.POST.get("ticker")
        timeframe = request.POST.get("timeframe")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        
        print(f"Form Data: Ticker={ticker}, Time Frame={timeframe}, Start Date={start_date}, End Date={end_date}")
        data = fetch_yahoo_data(ticker, timeframe, start_date, end_date)
        
        print(f"Fetched Data: {data}")

    return render(request, 'task1app/index.html', {'data': data})
