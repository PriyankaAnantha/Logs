from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import aiohttp
import datetime
import time

app = FastAPI()

class YahooFinanceRequest(BaseModel):
    ticker: str
    timeframe: str
    start_date: str
    end_date: str

@app.post("/fetch-data/")
async def fetch_data(request: YahooFinanceRequest):
    start_timestamp = int(time.mktime(datetime.datetime.strptime(request.start_date, "%Y-%m-%d").timetuple()))
    end_timestamp = int(time.mktime(datetime.datetime.strptime(request.end_date, "%Y-%m-%d").timetuple()))
    
    url = f"https://query1.finance.yahoo.com/v7/finance/download/{request.ticker}"
    params = {
        'period1': start_timestamp,
        'period2': end_timestamp,
        'interval': request.timeframe,
        'events': 'history',
        'includeAdjustedClose': 'true'
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                raise HTTPException(status_code=response.status, detail="Failed to fetch data")
            data = await response.text()
            return {"data": data}
