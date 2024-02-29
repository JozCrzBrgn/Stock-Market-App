from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    if request.method == "POST":
        ticker = request.POST['ticker']
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token=pk_56410da2968a4043bd55c65f7465ee84")
        try:
            api = json.loads(api_request.content)
        except:
            api = "Error... "
        return render(request, 'home.html', {'api':api})
    else:
        return render(request, 'home.html', {'ticker':"Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    return render(request, 'add_stock.html', {})