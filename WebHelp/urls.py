from django.contrib import admin
from django.urls import path, include
from orders import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('customer.urls')),
    path('orderList/', order_views.orderList, name='order-list')
]
