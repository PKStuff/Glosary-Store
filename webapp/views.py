from django.shortcuts import render, redirect
from .forms import Store_form
from .models import Store, Purchase
from django.http import HttpResponse
from django.db.models import Sum
from math import ceil

def index(request):

    items = Store.objects.all()

    return render(request,'webapp/index.html',{'item':items})

def sold_item(request, item_id):

    item = Store.objects.get(pk=item_id)
    item_quantity = item.quantity
    form = Store_form(request.POST,instance=item)
    pur = Purchase()
    if request.method == 'POST':
        if form.is_valid():
            form = form.save(commit=False)
            if item_quantity < form.quantity:
                return HttpResponse("<h4> Item quantity is less than requested only {{item_quantity }}remaining </h4>")
            else:
                pur.item_name = item.item_name
                pur.price = item.price
                pur.quantity = form.quantity
                pur.total_price = pur.price * pur.quantity
                form.quantity = item_quantity - form.quantity
                form.save()
                pur.save()
        return redirect('index')
    else:
        form = Store_form()
    return render(request,'webapp/register.html',{'form':form})

def Start_Shop(request):

    Purchase.objects.all().delete()
    return redirect('index')

def End_Shop(request):

    msg = None
    all_data = Purchase.objects.all()
    total = 0
    tatol = 0
    if not all_data:
        msg = "Cart Empty."
        print(msg)
    else:
        tatol = Purchase.objects.aggregate(sum=Sum('total_price'))['sum']
        total = float("%0.2f" % (tatol))
    return render(request,'webapp/bill.html',{'all_data':all_data,'total':total,'msg':msg})






