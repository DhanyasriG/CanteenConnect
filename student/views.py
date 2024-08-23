import stripe
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Student, Addaitems, Naturalsitems, RaSitems, Usitems



def login(request):
    return render(request, "login.html")

def index(request):
    return render(request, "index.html")

def checklogin(request):
    email = request.POST.get("semail")
    pwd = request.POST.get("spwd")

    student = Student.objects.filter(Q(email=email) & Q(password=pwd)).first()

    if student:
        request.session["sid"] = student.id
        request.session["semail"] = student.email
        return redirect('home')
    else:
        msg = "Login Failed"
        return render(request, "login.html", {"msg": msg})

def home(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    context = {
        "id": request.session["sid"],
        "email": request.session["semail"]
    }
    return render(request, "home.html", context)

def resetpwd(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    context = {
        "id": request.session["sid"],
        "email": request.session["semail"]
    }
    return render(request, "resetpwd.html", context)

def updatepwd(request):
    semail = request.POST.get("semail")
    opwd = request.POST.get("op")
    npwd = request.POST.get("np")

    if Student.objects.filter(Q(email=semail) & Q(password=opwd)).exists():
        Student.objects.filter(email=semail).update(password=npwd)
        msg = "Password Updated Successfully"
        return render(request, "login.html", {"email": semail, "msg": msg})
    else:
        msg = "Email or Old Password is Incorrect"
        return render(request, "resetpwd.html", {"email": semail, "msg": msg})

def addaitems(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    context = {
        "id": request.session["sid"],
        "email": request.session["semail"]
    }
    return render(request, "addaitems.html", context)

def adda_list(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    products = Addaitems.objects.all()
    context = {
        'products': products,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'addaitems.html', context)

def add_to_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    item = get_object_or_404(Addaitems, id=item_id)
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
        item.stock -= 1
    else:
        cart[str(item_id)] = {
            'name': item.name,
            'price': item.price,
            'img': item.img,
            'quantity': 1,
            'stock': item.stock - 1
        }
        item.stock -= 1

    item.save()
    request.session['cart'] = cart
    return redirect('adda_list')

def adda_update_quantity(request, item_id, action):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    item = get_object_or_404(Addaitems, id=item_id)
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if action == 'increase':
            if item.stock > 0:
                cart[str(item_id)]['quantity'] += 1
                item.stock -= 1
            else:
                messages.error(request, "Out of Stock")
        elif action == 'decrease':
            if cart[str(item_id)]['quantity'] > 1:
                cart[str(item_id)]['quantity'] -= 1
                item.stock += 1

        request.session['cart'] = cart
        item.save()

    return redirect('view_cart')

def view_cart(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    cart = request.session.get('cart', {})
    cart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'img': item['img'],
            'quantity': item['quantity'],
            'stock': item['stock']
        }
        for item_id, item in cart.items()
    ]
    total_cost = sum(item['price'] * item['quantity'] for item in cart.values())

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'cart.html', context)

def remove_from_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    item = get_object_or_404(Addaitems, id=item_id)
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        item.stock += cart[str(item_id)]['quantity']
        del cart[str(item_id)]
        request.session['cart'] = cart

    item.save()
    return redirect('view_cart')

def search(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    query = request.GET.get('q')
    products = Addaitems.objects.filter(name__icontains=query) if query else Addaitems.objects.all()

    context = {
        'products': products,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'addaitems.html', context)






def naturalsitems(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    context = {
        "id": request.session["sid"],
        "email": request.session["semail"]
    }
    return render(request,"naturalsitems.html",context)

def naturals_list(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    nproducts = Naturalsitems.objects.all()
    context = {
        'nproducts': nproducts,
        "id": request.session["sid"],
        "email": request.session["semail"]
    }

    return render(request, 'naturalsitems.html', context)


def naturals_add_to_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(Naturalsitems, id=item_id)
    ncart = request.session.get('ncart', {})

    if str(item_id) in ncart:
        ncart[str(item_id)]['quantity'] += 1
        item.stock = item.stock - 1
    else:
        ncart[str(item_id)] = {
            'name': item.name,
            'price': item.price,
            'img': item.img,
            'quantity': 1,
            'stock':item.stock-1
        }
        item.stock -= 1
    item.save()
    request.session['ncart'] = ncart
    return redirect('naturals_list')

def naturals_update_quantity(request, item_id, action):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    item = get_object_or_404(Naturalsitems, id=item_id)
    ncart = request.session.get('ncart', {})

    if str(item_id) in ncart:
        if action == 'increase':
            if item.stock > 0:
                ncart[str(item_id)]['quantity'] += 1
                ncart[str(item_id)]['stock'] = item.stock - 1
                item.stock -= 1
            else:
                messages.error(request, "Out of Stock")
        elif action == 'decrease':
            if ncart[str(item_id)]['quantity'] > 1:
                ncart[str(item_id)]['quantity'] -= 1
                ncart[str(item_id)]['stock'] = item.stock + 1
                item.stock += 1
        request.session['ncart'] = ncart
    item.save()

    return redirect('naturals_view_cart')

def naturals_view_cart(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    ncart = request.session.get('ncart', {})
    ncart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'img': item['img'],
            'quantity': item['quantity'],
            'stock': item.get('stock', 0)

        }
        for item_id, item in ncart.items()
    ]
    total_cost = sum(item['price'] * item['quantity'] for item in ncart.values())
    context = {
        'ncart_items': ncart_items,
        'total_cost': total_cost,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'naturalscart.html', context)


def naturals_remove_from_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(Naturalsitems, id=item_id)
    ncart = request.session.get('ncart', {})
    if str(item_id) in ncart:
        item.stock += ncart[str(item_id)]['quantity']
        del ncart[str(item_id)]
        request.session['cart'] = ncart
    item.save();
    return redirect('naturals_view_cart')

def nsearch(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    query = request.GET.get('q1')
    if query:
        products = Naturalsitems.objects.filter(name__icontains=query)
    else:
        products = Naturalsitems.objects.all()
    context = {
        'nproducts': products,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'naturalsitems.html', context)


def rasitems(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    context = {
        "id": request.session["sid"],
        "email": request.session["semail"]
    }
    return render(request,"rasitems.html",context)

def ras_list(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    rproducts =  RaSitems.objects.all()
    context = {
        'rproducts': rproducts,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'rasitems.html', context)



def ras_add_to_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')

    item = get_object_or_404(RaSitems, id=item_id)
    rcart = request.session.get('rcart', {})

    if str(item_id) in rcart:
        rcart[str(item_id)]['quantity'] += 1
        item.stock = item.stock - 1
    else:
        rcart[str(item_id)] = {
            'name': item.name,
            'price': item.price,
            'img': item.img,
            'quantity': 1,
            'stock':item.stock-1
        }
        item.stock -= 1
    item.save()
    request.session['rcart'] = rcart
    return redirect('ras_list')

def ras_update_quantity(request, item_id, action):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(RaSitems, id=item_id)
    rcart = request.session.get('rcart', {})

    if str(item_id) in rcart:
        if action == 'increase':
            if item.stock > 0:
                rcart[str(item_id)]['quantity'] += 1
                rcart[str(item_id)]['stock'] = item.stock - 1
                item.stock -= 1
            else:
                messages.error(request, "Out of Stock")
        elif action == 'decrease':
            if rcart[str(item_id)]['quantity'] > 1:
                rcart[str(item_id)]['quantity'] -= 1
                rcart[str(item_id)]['stock'] = item.stock + 1
                item.stock += 1
        request.session['rcart'] = rcart
    item.save()

    return redirect('ras_view_cart')

def ras_view_cart(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    rcart = request.session.get('rcart', {})
    ras_cart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'img': item['img'],
            'quantity': item['quantity'],
            'stock':item['stock']
        }
        for item_id, item in rcart.items()
    ]
    total_cost = sum(item['price'] * item['quantity'] for item in rcart.values())
    context = {
        'ras_cart_items': ras_cart_items,
        'total_cost': total_cost,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'rascart.html', context)

def ras_remove_from_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(RaSitems, id=item_id)
    rcart = request.session.get('rcart', {})
    if str(item_id) in rcart:
        item.stock += rcart[str(item_id)]['quantity']
        del rcart[str(item_id)]
        request.session['rcart'] = rcart
    item.save();
    return redirect('ras_view_cart')

def rsearch(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    query = request.GET.get('q')
    if query:
        rproducts = RaSitems.objects.filter(name__icontains=query)
    else:
        rproducts = RaSitems.objects.all()
    context = {
        'rproducts': rproducts,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'rasitems.html', context)




def usitems(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    context = {
        "id": request.session["sid"],
        "email": request.session["semail"]
    }
    return render(request,"usitems.html",context)

def us_list(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    uproducts =  Usitems.objects.all()
    context = {
        'uproducts': uproducts,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'usitems.html', context)



def us_add_to_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(Usitems, id=item_id)
    ucart = request.session.get('ucart', {})

    if str(item_id) in ucart:
        ucart[str(item_id)]['quantity'] += 1
        item.stock = item.stock - 1
    else:
        ucart[str(item_id)] = {
            'name': item.name,
            'price': item.price,
            'img': item.img,
            'quantity': 1,
            'stock': item.stock-1
        }
        item.stock -= 1
    item.save()

    request.session['ucart'] = ucart
    return redirect('us_list')

def us_update_quantity(request, item_id, action):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(Usitems, id=item_id)
    ucart = request.session.get('ucart', {})

    if str(item_id) in ucart:
        if action == 'increase':
            if item.stock > 0:
                ucart[str(item_id)]['quantity'] += 1
                ucart[str(item_id)]['stock'] = item.stock - 1
                item.stock -= 1
            else:
                messages.error(request, "Out of Stock")
        elif action == 'decrease':
            if ucart[str(item_id)]['quantity'] > 1:
                ucart[str(item_id)]['quantity'] -= 1
                ucart[str(item_id)]['stock'] = item.stock + 1
                item.stock += 1
        request.session['ucart'] = ucart
    item.save()

    return redirect('us_view_cart')

def us_view_cart(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    ucart = request.session.get('ucart', {})
    us_cart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'img': item['img'],
            'quantity': item['quantity'],
            'stock': item.get('stock', 0)
        }
        for item_id, item in ucart.items()
    ]
    total_cost = sum(item['price'] * item['quantity'] for item in ucart.values())
    context = {
        'us_cart_items': us_cart_items,
        'total_cost': total_cost,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'uscart.html', context)

def us_remove_from_cart(request, item_id):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    item = get_object_or_404(Usitems, id=item_id)
    ucart = request.session.get('ucart', {})
    if str(item_id) in ucart:
        item.stock += ucart[str(item_id)]['quantity']
        del ucart[str(item_id)]
        request.session['ucart'] = ucart
    item.save();
    return redirect('us_view_cart')

def usearch(request):
    if "sid" not in request.session or "semail" not in request.session:
        return redirect('login')
    query = request.GET.get('q')
    if query:
        uproducts = Usitems.objects.filter(name__icontains=query)
    else:
        uproducts = Usitems.objects.all()
    context = {
        'uproducts': uproducts,
        'query': query,
        'id': request.session["sid"],
        'email': request.session["semail"]
    }
    return render(request, 'usitems.html', context)

