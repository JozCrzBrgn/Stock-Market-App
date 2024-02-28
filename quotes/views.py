from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    # pk_56410da2968a4043bd55c65f7465ee84
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_56410da2968a4043bd55c65f7465ee84")
    try:
        api = json.loads(api_request.content)
    except:
        api = "Error... "

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})