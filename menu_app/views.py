from django.shortcuts import render

def home(request):
    return render(request, 'menu_app/home.html')

def page1(request):
    return render(request, 'menu_app/page1.html')

def page2(request):
    return render(request, 'menu_app/page2.html')

def page3(request):
    return render(request, 'menu_app/page3.html')

def page4(request):
    return render(request, 'menu_app/page4.html')