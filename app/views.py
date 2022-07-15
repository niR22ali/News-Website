from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    return render(request,'index.html')

def entertainment(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=entertainment"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)
    # return render(request, 'sports.html', records)

def sports(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=sports"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def politics(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=politics"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)
    # return render(request,'politics.html', records)

def business(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=business"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def technology(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=technology"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def international(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=international"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def india(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=india"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)

def miscellaneous(request):
    records = {}
    url = "https://inshorts.deta.dev/news?category=miscellaneous"
    response = requests.get(url=url)
    inshorts_data = response.json()
    records['sportsdata'] = inshorts_data
    return render(request, 'sports.html', records)