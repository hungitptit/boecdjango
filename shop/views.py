from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from app.models import Product, Productofsupplier, Supplier
from .cartview import CartView
from .forms import CartAddProductForm


@require_POST
def CartAdd(request, product_id):
    cart = CartView(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])
    return redirect('cart:CartProduct')

def CartRemove(request, product_id):
    cart = CartView(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartProduct')

def CartProduct(request):
    cart = CartView(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
                                        initial={
                                            'quantity': item['quantity'],
                                            'update': True
                                        })

    return render(request, 'cart.html',
                 {'cart': cart})

def shopping_list(request):
    product_list = Product.objects.all()
    if product_list != None:
        return render(request, 'products.html', {'items': product_list})
    else:
        return render(request, 'products.html', {'items': []})

def supplier_of_product_list(request):
    supplier_list = Supplier.objects.select_related("productofsupplier", "product").filter("productId=" + request.product_id)
    if supplier_list != None:
        return render(request, 'supplier-list.html', {'items': supplier_list})
    else:
        return render(request, 'supplier-list.html', {'items': []})