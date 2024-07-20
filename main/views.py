from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def pricing(request):
    return render(request, 'main/pricing.html')

def features(request):
    return render(request, 'main/features.html')