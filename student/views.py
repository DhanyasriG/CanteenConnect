from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .models import Student


def login(request):
    return render(request,"index.html")

def checklogin(request):
    email = request.POST["semail"]
    pwd = request.POST["spwd"]

    flag = Student.objects.filter(Q(email=email) & Q(password=pwd))

    print(flag)

    if flag:
        s = Student.objects.get(email=email)
        print(s)
        request.session["sid"] = s.id
        request.session["semail"] = s.email
        return render(request, "home.html", {"sid": s.id, "email": s.email})
    else:
        msg = "Login Failed"
        return render(request, "index.html", {"msg": msg})

def home(request):
    return render(request,"home.html")