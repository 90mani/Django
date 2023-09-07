from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector
import json
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    port="3307",
    database="student-mgnt",
  ) 
mycursor = mydb.cursor()
def index(request):
    return HttpResponse("it's my project")

def firstpage(request):
    template =loader.get_template("test1.html")
    return HttpResponse(template.render())

def secondpage(request):
    template = loader.get_template("namevar.html")
    name = "bhuvana"
    context = {"firstname": name, "saraname": "charu","lastname": "anathan"}
    return HttpResponse(template.render(context, request))


def mark(request):
    template = loader.get_template("nextpage.html")
    context = {"name": "bhuvana", "mark": 65}
    return HttpResponse(template.render(context, request))

def tablecre(request):
    template = loader.get_template("tablecre.html")
    #studentList = [
        #{"name": "bhuvi", "id": 1, "course": "ba","sem":3,"attendance":99},
        #{"name": "anand", "id": 2, "course": "bsc","sem":4,"attendance":93},
        #{"name": "charu", "id": 3, "course": "bsc","sem":6,"attendance":94},
        #{"name": "saro", "id": 4, "course": "bsc","sem":2,"attendance":95},
        #{"name": "reva", "id": 5, "course": "ba","sem":1,"attendance":96}, 
    

    #]
    #context = {"studentData": studentList}
    studentlist=[]

mycursor.execute("SELECT * from student")
myresult = mycursor.fetchall()
for record in myresult:
    row = {"name": record[1],"id":record[0], "course":record[2], "sem":record[3], "attendance":record[4]}
    studentlist.append(row)
context = {"studentdata": studentlist}   
print(context) 
return HttpResponse(template.render(context, request))

       
def logepage(request):
    template = loader.get_template("log.html")
    context = {"username": "bhuvananand", "pswd": "bhuvi123"}
    return HttpResponse(template.render(context, request))

       
    
   
 #Create your views here.
