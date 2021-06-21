# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, CommentForm
from django.contrib.auth.decorators import login_required
from app.models import Address, Authuser, Comment, Product, Productcategory, Supplier, Productofsupplier, Payment,\
    Shipment, City, District, Ward, Paymenttype, User
from app.cart import Cart
import pickle
import os
from core import settings


def remove_stopwords(line, stopWords):
    words = []
    for word in line.strip().split():
        
        if word not in stopWords:
            words.append(word)
    return ' '.join(words)



def classify(comment,model):
    y_pred = model.predict([comment])
    return y_pred[0]


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })

def productlist(request):
    product_list = Product.objects.all()
    if product_list != None:
        return render(request, 'products.html', {'items': product_list, 'title':"Hot and New"})
    else:
        return render(request, 'products.html', {'items': []})


def supplier_of_product_list(request):
    product = Product.objects.filter(id=request.GET.get('product_id',''))
    price_list = Productofsupplier.objects.select_related("productid").filter(productid=request.GET.get('product_id', ''))
    supplier_list = []
    comments = Comment.objects.filter(product_id=request.GET.get('product_id',''))
    
    context = {'product': product,
                'comments': comments,
                'items': []
               }
    for price in price_list:
        supplier_list.append(Supplier.objects.all().get(id=price.supplierid.id))
    if price_list != None and supplier_list != None:
        return render(request, 'product-detail.html', {'prices': price_list, 'suppliers': supplier_list,'item':product[0],'comments': comments,'product': product})
    else:
        return render(request, 'product-detail.html', context)

def get_to_payment(request):
    shipment = Shipment.objects.all()
    cities = City.objects.all()
    districts = District.objects.all()
    wards = Ward.objects.all()
    paymentType = Paymenttype.objects.all()
    return render(request, 'payment-detail.html', {'shipment': shipment, 
        'cities': cities, 'districts': districts, 'wards': wards, 'types': paymentType})

#Moi luu dia chi va nguoi dung
def save_payment(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            phoneNumber = form.cleaned_data.get("phoneNumber")
            ward = Ward.objects.get(id=form.cleaned_data.get("ward"))
            address = Address(wardId=ward, detail=form.cleaned_data.get("address"))
            address.save()
            user = User(phoneNumber=phoneNumber, addressId=address)
            user.save()
            success = True
            
            return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg, "success" : success })

def searchProductByCategory(request, categoryName):
    #cart = Cart(request)
    
    product_list = Product.objects.raw("SELECT distinct Product.* from Product join ProductSubCategory on Product.ProductSubCategoryID = ProductSubCategory.ID join ProductCategory on ProductSubCategory.ProductCategoryID = ProductCategory.ID WHERE ProductCategory.name = %s or ProductSubCategory.name = %s", [categoryName,categoryName])
    print (product_list)
    if product_list != None:
        return render(request, 'products.html', {'items': product_list, 'title': categoryName})
    else:
        return render(request, 'products.html', {'items': []})


def categories(request):
    category_list = Productcategory.objects.all()
    if category_list != None:
        return render(request, 'category.html', {'items': category_list})
    else:
        return render(request, 'category.html', {'items': []})


@login_required(login_url="/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    productofsupplier = Productofsupplier.objects.get(productid=product.id,supplierid=1)
    cart.add(product=product,price=productofsupplier.price)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    productofsupplier = Productofsupplier.objects.get(productid=product.id,supplierid=1)
    cart.add(product=product,price=productofsupplier.price)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login/")
def cart_detail(request):
    cart = Cart(request)
    #print(cart.cart['2']['price'])
    totalPrice = 0
    for value in cart.cart.values():
        totalPrice+= int(value['price'])
    numberOfitems = len(cart.cart)
    #print(request.user.username)
    return render(request, 'cart.html', {'totalPrice':totalPrice, 'numberOfItems':numberOfitems})

    
def addcomment(request,id):
    
    model = pickle.load(open(os.path.join(settings.BASE_DIR,"naive_bayes1.pkl"), 'rb'))
    stopWords = []
    for line in open(os.path.join(settings.BASE_DIR,'stop.txt'), encoding='utf-8'):
        words = line.strip().split()
        stopWords.append(words[0])
    
    url = request.META.get('HTTP_REFERER')  # get last url
   #return HttpResponse(url)
    if request.method == 'POST':  # check post
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()  # create relation with model
            data.subject = form.cleaned_data['subject']
            data.detail = form.cleaned_data['detail']
            data.rate = form.cleaned_data['rate']
            #data.ip = request.META.get('REMOTE_ADDR')
            data.product=Product.objects.filter(id=id)[0]
            current_user= request.user
            data.authuser=current_user
            data.label=classify(remove_stopwords(data.detail,stopWords=stopWords),model)
            data.save()  # save data to table
            messages.success(request, "Your review has been sent. Thank you for your interest.")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)
def cmp(e):
  return e['satisfy']

@login_required(login_url="/login/")
def commentsAnalysis(request):
    obj = request.POST.get('object','Product')
    users = User.objects.all()
    products = Product.objects.all() 
    comments = Comment.objects.all()
    data = []
    for product in products:
        mapData = {}
        negative = 0
        positive = 0
        for comment in comments:
            if (product.id==comment.product.id ):
                if comment.label==0:
                    negative+=1
                else:
                    positive+=1
        mapData['product'] = product
        mapData['negative'] = negative
        mapData['positive'] = positive
        mapData['satisfy'] = float(positive/(negative+positive)*100)
        data.append(mapData)
    data.sort(reverse=True, key=cmp)
                
    context ={'data':data, 'object':obj}

    return render(request, 'comments-analysis.html',context)

@login_required(login_url="/login/")
def staff(request):
    return render(request, 'staff.html')

@login_required(login_url="/login/")
def comments_analysis_detail_product(request,id):
    product = Product.objects.filter(id=id)
    price_list = Productofsupplier.objects.select_related("productid").filter(productid=id)
    supplier_list = []
    comments = Comment.objects.filter(product_id=id)
    
    context = {'product': product,
                'comments': comments,
                'items': []
               }
    for price in price_list:
        supplier_list.append(Supplier.objects.all().get(id=price.supplierid.id))
    if price_list != None and supplier_list != None:
        return render(request, 'comments-analysis-detail-product.html', {'prices': price_list, 'suppliers': supplier_list,'item':product[0],'comments': comments,'product': product})
    else:
        return render(request, 'comments-analysis-detail-product.html', context)
  