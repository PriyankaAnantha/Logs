from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests

@csrf_exempt
def fetch_stock_data(request):
    data = {}
    if request.method == "POST":
        ticker = request.POST.get('ticker')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        interval = request.POST.get('interval')
        
        # Replace this with your FastAPI endpoint
        api_url = f"http://localhost:8000/stocks/?ticker={ticker}&start_date={start_date}&end_date={end_date}&interval={interval}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
        else:
            data['error'] = 'Could not fetch data from API.'

    return render(request, 'index.html', {'data': data})
