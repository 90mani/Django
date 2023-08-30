from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    return HttpResponse("Hello world!")

def firstpage(request):
    template=loader.get_template("test2.html")
    return HttpResponse(template.render())