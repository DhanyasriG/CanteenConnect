from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Student, Addaitems, Naturalsitems


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

def addaitems(request):
    return render(request,"addaitems.html")

def adda_list(request):
    print("HI")
    products = Addaitems.objects.all()
    print(products)
    context = {'products': products}
    return render(request, 'addaitems.html', context)



def add_to_cart(request, item_id):
    item = get_object_or_404(Addaitems, id=item_id)
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        cart[str(item_id)]['quantity'] += 1
    else:
        cart[str(item_id)] = {
            'name': item.name,
            'price': item.price,
            'img': item.img,
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('adda_list')

def adda_update_quantity(request, item_id, action):
    cart = request.session.get('cart', {})

    if str(item_id) in cart:
        if action == 'increase':
            cart[str(item_id)]['quantity'] += 1
        elif action == 'decrease' and cart[str(item_id)]['quantity'] > 1:
            cart[str(item_id)]['quantity'] -= 1
        elif action == 'decrease' and cart[str(item_id)]['quantity'] == 1:
            del cart[str(item_id)]
        request.session['cart'] = cart

    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'img': item['img'],
            'quantity': item['quantity']
        }
        for item_id, item in cart.items()
    ]
    total_cost = sum(item['price'] * item['quantity'] for item in cart.values())
    context = {
        'cart_items': cart_items,
        'total_cost': total_cost
    }
    return render(request, 'cart.html', context)



def remove_from_cart(request, item_id):
    cart = request.session.get('cart', {})
    if str(item_id) in cart:
        del cart[str(item_id)]
        request.session['cart'] = cart
    return redirect('view_cart')




def naturalsitems(request):
    return render(request,"naturalsitems.html")

def naturals_list(request):
    print("HI")
    nproducts = Naturalsitems.objects.all()
    print(nproducts)
    context = {'nproducts': nproducts}
    return render(request, 'naturalsitems.html', context)


def naturals_add_to_cart(request, item_id):
    item = get_object_or_404(Naturalsitems, id=item_id)
    ncart = request.session.get('ncart', {})

    if str(item_id) in ncart:
        ncart[str(item_id)]['quantity'] += 1
    else:
        ncart[str(item_id)] = {
            'name': item.name,
            'price': item.price,
            'img': item.img,
            'quantity': 1
        }

    request.session['ncart'] = ncart
    return redirect('naturals_list')

def naturals_update_quantity(request, item_id, action):
    ncart = request.session.get('ncart', {})

    if str(item_id) in ncart:
        if action == 'increase':
            ncart[str(item_id)]['quantity'] += 1
        elif action == 'decrease' and ncart[str(item_id)]['quantity'] > 1:
            ncart[str(item_id)]['quantity'] -= 1
        elif action == 'decrease' and ncart[str(item_id)]['quantity'] == 1:
            del ncart[str(item_id)]
        request.session['ncart'] = ncart

    return redirect('naturals_view_cart')

def naturals_view_cart(request):
    ncart = request.session.get('ncart', {})
    ncart_items = [
        {
            'id': item_id,
            'name': item['name'],
            'price': item['price'],
            'img': item['img'],
            'quantity': item['quantity']
        }
        for item_id, item in ncart.items()
    ]
    total_cost = sum(item['price'] * item['quantity'] for item in ncart.values())
    context = {
        'ncart_items': ncart_items,
        'total_cost': total_cost
    }
    return render(request, 'naturalscart.html', context)



def naturals_remove_from_cart(request, item_id):
    ncart = request.session.get('ncart', {})
    if str(item_id) in ncart:
        del ncart[str(item_id)]
        request.session['ncart'] = ncart
    return redirect('naturals_view_cart')