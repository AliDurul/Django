
""" from django.http import HttpResponse

 def homepage(request):
    return HttpResponse('Home page')

def about(request):
    return HttpResponse('About page') """


from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')