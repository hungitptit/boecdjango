from django.conf.urls import url
from shop import views


urlpatterns = [
    url(r'^$', views.CartProduct, name='CartProduct'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    url("product/", views.shopping_list, name="product"),
    url(r'^supplierofproduct/(?P<product_id>\d+)/$', views.supplier_of_product_list, name="SupplierOfProduct")
]
