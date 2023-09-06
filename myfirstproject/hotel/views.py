
from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector
import json



mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="2810",
    database="studend",
)
mycursor = mydb.cursor()


def homepage(request):
     return HttpResponse("It me django")

def firstpage(request):
  template=loader.get_template("first.html")
  return HttpResponse(template.render())

def colour(request):
  template=loader.get_template("test1.html")
  return HttpResponse(template.render())


def lastpage(request):
  template=loader.get_template("name.html")
  name = "kamalam"
  context = {"firstname": name, "lastname": "doss"}
  return HttpResponse(template.render(context, request))

def mark(request):
  template=loader.get_template("ifelse.html")
  context = {"firstname": "kamalam", "mark":50}
  return HttpResponse(template.render(context, request))

def tablecreate(request):
   template = loader.get_template("table.html")
  #  studentlist=[
  #       {"name": "kamalam","id":1221, "mark":65, "grade":3},
  #       {"name":"jeeva", "id":1223, "mark":80, "grade":2},
  #       {"name":"mani", "id":1224, "mark":70, "grade":1},
  #              ]
   
  #  context = {"studentdata": studentlist}
   studentlist=[]

   mycursor.execute("SELECT * from marksheet")
   myresult = mycursor.fetchall()
   for record in myresult:
       row = {"name": record[1],"id":record[0], "mark":record[2], "grade":record[3]}
       studentlist.append(row)
   context = {"studentdata": studentlist}   
   print(context)
   return HttpResponse(template.render(context, request))


def logicfile(request):
  template=loader.get_template("logic.html")
  return HttpResponse(template.render())


# Create your views here.





