from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def post_list(request):
    return render(request, 'coffeeshop/post_list.html', {})   