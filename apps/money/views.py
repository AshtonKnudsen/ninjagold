from django.shortcuts import render, redirect
from random import random, randint

def index(request):
    if "count" in request.session:
        request.session["count"] += 1
    if not "count" in request.session:
        request.session["count"] = 0
    if not "money" in request.session:
        request.session["money"] = 0 
    if not "history" in request.session:
        request.session["history"] = []
    return render(request, "money/Ngold.html")

def makemoney(request, name):
    context = {
        "cave" : request.session["money"] + randint(50,100),
        "casino" : request.session["money"] + randint(-500,250),
        "house" : request.session["money"] + randint(5,20),
        "farm" : request.session["money"] + randint(10,25)
    }
    request.session["money"] = context[name]

    if name == "cave":
        request.session["history"].append('You found a cave and you now have ' + str(context[name]) + ' GOLD!!')
    if name == "casino":
        request.session["history"].append('Gabling huh? now you have ' + str(context[name]) + ' gold')
    if name == "house":
        request.session["history"].append('You found some coins under the couch and now have ' + str(context[name]) + ' gold')
    if name == "farm":
        request.session["history"].append('You farmed some products and sold them ' + str(context[name]))
    return redirect("/", context)

def reset(request):
    request.session.clear()
    return redirect("/")
# Create your views here.
