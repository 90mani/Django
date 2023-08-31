from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return HttpResponse("it's me django")


def firstpage(request):
    template = loader.get_template("para.html")
    name = "Manikandan"
    context = {"firstname": name, "lastname": "Chinnasamy"}
    return HttpResponse(template.render(context, request))


def testColorPage(request):
    template = loader.get_template("colour.html")
    context = {"name": "Manikandan", "age": 10}
    return HttpResponse(template.render(context, request))


# Create your views here.
