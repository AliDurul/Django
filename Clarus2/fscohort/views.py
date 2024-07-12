from django.shortcuts import render
from django.http import HttpResponse


def fscohort(request):
    return HttpResponse('fscohort/index.html')

