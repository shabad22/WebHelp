from django.shortcuts import render
# from django.views.generic import ListView
from .models import Service, Order
from django.contrib import messages

def home(request):
    context = {
        'services': Service.objects.all()
    }
    return render(request, 'customer/home.html', context)

# class OrderDetail(ListView):
#     model = Service
#     template_name = 'customer/service_detail.html'
#     context_object_name = 'service'

def orderDetail(request):
    context = {
        'services': Service.objects.all()
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        desc = request.POST['desc']
        job = request.POST['job']
        # print(name, email, address, city, desc, job)
        if len(name)<5 or len(desc)<5 or len(address)<15 or len(city)<10 or len(job)<5:
            messages.error(request, "There is an error in you order. Please fill it correctly")
        else:
            order = Order(name=name, email=email, address=address, city=city, desc=desc, job=job)
            order.save()
            messages.success(request, "Thank you for trusting us! You will recieve a callback soon from one of our workers")

    return render(request, 'customer/order.html', context)
