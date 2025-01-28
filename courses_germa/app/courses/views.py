from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.

def getIndex(request):
    return render(request, 'courses/index.html')
