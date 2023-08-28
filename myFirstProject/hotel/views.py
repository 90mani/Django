from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("It's me django")


def firstTemplate(request):
    template = loader.get_template("test.html")
    return HttpResponse(template.render())


# Create your views here.
