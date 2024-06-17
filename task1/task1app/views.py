from django.shortcuts import render

# Creating views here.

import requests

def index(request):
    data = {}
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        interval = request.POST.get('interval')
        response = requests.get(f'http://localhost:8000/stocks/?ticker={ticker}&start_date={start_date}&end_date={end_date}&interval={interval}')
        data = response.json()
    return render(request, 'finance_app/index.html', {'data': data})
