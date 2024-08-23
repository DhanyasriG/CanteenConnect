from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from .forms import AddaForm,UsForm,RasForm,NaturalsForm

from .models import Restaurant
from student.models import Addaitems, Naturalsitems, Usitems, RaSitems
from django.shortcuts import redirect,get_object_or_404

def rlogin(request):
    return render(request,"rlogin.html")

def adda(request):
    email = request.POST.get("remail")
    products = Addaitems.objects.all()
    return render(request, "adda.html", {"remail": email, "products": products})


def naturals(request):
    email = request.POST.get("remail")
    products = Naturalsitems.objects.all()
    return render(request, "naturals.html", {"remail": email, "products": products})

def ras(request):
    email = request.POST.get("remail")
    products = RaSitems.objects.all()
    return render(request, "ras.html", {"remail": email, "products": products})

def us(request):
    email = request.POST.get("remail")
    products = Usitems.objects.all()
    return render(request, "us.html", {"remail": email, "products": products})

def rchecklogin(request):
    email = request.POST["remail"]
    pwd = request.POST["rpwd"]

    flag = Restaurant.objects.filter(Q(email=email) & Q(password=pwd))

    print(flag)

    if flag:
        r = Restaurant.objects.get(email=email)
        request.session["rid"] = r.id
        request.session["remail"] = r.email
        request.session["rname"]=r.rname
        if r.rname == "Adda":
            products = Addaitems.objects.all()
            return render(request, "adda.html", {"rid": r.id, "remail": r.email, "products": products})
        elif r.rname == "Naturals":
            products = Naturalsitems.objects.all()
            return render(request, "naturals.html", {"rid": r.id, "remail": r.email, "products":products})
        elif r.rname == "Us Pizza":
                products = Usitems.objects.all()  # Ensure you're querying the correct model
                return render(request, "us.html", {"rid": r.id, "remail": r.email, "products": products})
        else:
            products = RaSitems.objects.all()
            return render(request, "ras.html", {"rid": r.id, "remail": r.email,"products":products})

    else:
        msg = "Login Failed"
        return render(request, "rlogin.html", {"msg": msg})

def rhome(request):
    return render(request,"rhome.html")

def addaupdate(request,id):
    product = get_object_or_404(Addaitems, id=id)
    if request.method=="POST":
        form=AddaForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            msg = "Stock Updated Successfully"
            # Render the template with the success message directly after saving
            return render(request, "addaupdate.html", {"form": form, "msg": msg, "product": product})
    else:
        form = AddaForm(instance=product)
    msg = request.GET.get('msg', None)
    return render(request, "addaupdate.html",{"form":form,"msg":msg,'product':product})

def search(request):

    query = request.GET.get('q')
    products = Addaitems.objects.filter(name__icontains=query) if query else Addaitems.objects.all()

    context = {
        'products': products,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'adda.html', context)


def rasupdate(request,id):
    product = get_object_or_404(RaSitems, id=id)
    if request.method=="POST":
        form=RasForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            msg = "Stock Updated Successfully"
            # Render the template with the success message directly after saving
            return render(request, "rasupdate.html", {"form": form, "msg": msg, "product": product})
    else:
        form = RasForm(instance=product)
    msg = request.GET.get('msg', None)
    return render(request, "rasupdate.html",{"form":form,"msg":msg,'product':product})

def rassearch(request):

    query = request.GET.get('q')
    products = RaSitems.objects.filter(name__icontains=query) if query else RaSitems.objects.all()

    context = {
        'products': products,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'ras.html', context)


def usupdate(request,id):
    product = get_object_or_404(Usitems, id=id)
    if request.method=="POST":
        form=UsForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            msg = "Stock Updated Successfully"
            # Render the template with the success message directly after saving
            return render(request, "usupdate.html", {"form": form, "msg": msg, "product": product})
    else:
        form = UsForm(instance=product)
    msg = request.GET.get('msg', None)
    return render(request, "usupdate.html",{"form":form,"msg":msg,'product':product})

def ussearch(request):

    query = request.GET.get('q')
    products = Usitems.objects.filter(name__icontains=query) if query else Usitems.objects.all()

    context = {
        'products': products,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'us.html', context)



def naturalsupdate(request,id):
    product = get_object_or_404(Naturalsitems, id=id)
    if request.method=="POST":
        form=NaturalsForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            msg = "Stock Updated Successfully"
            # Render the template with the success message directly after saving
            return render(request, "naturalsupdate.html", {"form": form, "msg": msg, "product": product})
    else:
        form = NaturalsForm(instance=product)
    msg = request.GET.get('msg', None)
    return render(request, "naturalsupdate.html",{"form":form,"msg":msg,'product':product})

def nsearch(request):

    query = request.GET.get('q')
    products = Naturalsitems.objects.filter(name__icontains=query) if query else Naturalsitems.objects.all()

    context = {
        'products': products,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'naturals.html', context)