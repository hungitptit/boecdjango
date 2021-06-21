# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, productlist, supplier_of_product_list, get_to_payment, categories
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('product/', productlist, name="product"),
    path('productdetail', supplier_of_product_list, name="productdetail"),
    path('payment', get_to_payment, name="payment"),
	path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('product/<slug:categoryName>/', views.searchProductByCategory, name='searchProductByCategory'),
    path('category/', categories, name="categories"),
    path('product/addcomment/<int:id>', views.addcomment, name='addcomment'),
    path('staff/', views.staff, name="staff"),
    path('staff/comments-analysis/', views.commentsAnalysis, name="comments-analysis"),
    path('staff/comments-analysis/detail/<int:id>/', views.comments_analysis_detail_product, name='comments-analysis-detail-product'),
]
