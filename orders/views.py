from django.shortcuts import render
from customer.models import Order

def orderList(request):
    context = {
        'orders': Order.objects.all()
    }
    return render(request, 'orders/orderList.html', context)


