from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   text = """<h1>welcome to my app !</h1>"""
   return render(request, "assessment/index.html", {})
