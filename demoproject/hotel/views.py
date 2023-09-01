from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import mysql.connector

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="girija",
#     password="girima",
#     database="author",
# )
# mycursor = mydb.cursor()


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


def testTable(request):
    template = loader.get_template("table.html")
    companyList = [
        {"company": "xyz", "contact": 999999, "country": "india"},
        {"company": "Abc", "contact": 88888, "country": "Chaina"},
        {"company": "Abc", "contact": 88888, "country": "Chaina"},
    ]
    context = {"companyData": companyList}
    # mycursor.execute("SELECT * from author.details")
    # myresult = mycursor.fetchall()
    return HttpResponse(template.render(context, request))


# Create your views here.
