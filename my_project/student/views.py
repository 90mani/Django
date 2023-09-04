from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def members(request):
    return HttpResponse("This is django program!")
def index(request):
    template = loader.get_template('sample.html')
    return HttpResponse(template.render())

def colorpage(request):
    template = loader.get_template('color.html')
    return HttpResponse(template.render())

def firstpage(request):
  template=loader.get_template("para.html")
  name = "girija"
  context = {"firstname": name, "lastname": "sam"}
  return HttpResponse(template.render(context, request))

def mark(request):
  template=loader.get_template("ifelse.html")
  context = {"firstname": "girija", "mark":80}
  return HttpResponse(template.render(context, request))

def sampletable(request):
  template = loader.get_template("table.html")
  studentlist=[
        {"name": "jeevi","id":101, "mark":40, "grade":5},
        {"name":"kayal", "id":102, "mark":55, "grade":1},
        {"name":"ima", "id":103, "mark":76, "grade":4}]
   
  context = {"studentdata": studentlist}
  return HttpResponse(template.render(context, request))







    
    


