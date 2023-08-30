from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("it's me django")
def firstpage(request):
    template = loader.get_template("para.html")
    return HttpResponse(template.render())

# Create your views here.
