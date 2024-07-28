from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def entrance(request):
    return render(request, "main/entrance.html")

def profile(request):
    return render(request, "main/profile.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def shop(request):
    return render(request, "main/shop.html")

