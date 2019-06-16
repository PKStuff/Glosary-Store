from django.shortcuts import render, redirect
from .forms import Store_form
from .models import Store, Purchase
from django.http import HttpResponse
from django.db.models import Sum
from .serializer import Rest_Purchase, Rest_Store
from rest_framework.decorators import api_view

@api_view(['GET'])
def index(request):

    items = Store.objects.all()
    serializer = Rest_Store(items, many=True)
    return render(request,'webapp/index.html',{'item':serializer.data})

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
                pur.item_number = item.id
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

@api_view(['DELETE','GET'])
def Start_Shop(request):

    Purchase.objects.all().delete()
    return redirect('index')

@api_view(['GET'])
def End_Shop(request):

    msg = None
    all_data = Purchase.objects.all()
    serialzer = Rest_Purchase(all_data, many=True)
    total = 0
    tatol = 0
    if not all_data:
        msg = "Cart Empty."
    else:
        tatol = Purchase.objects.aggregate(sum=Sum('total_price'))['sum']
        total = float("%0.2f" % (tatol))
    return render(request,'webapp/bill.html',{'all_data':serialzer.data,'total':total,'msg':msg})

@api_view(['GET','DELETE'])
def delete_item(request, item_id):

    data = Purchase.objects.get(item_number=item_id)
    original_quantity = Store.objects.get(pk=item_id)
    Purchase.objects.filter(item_number=item_id).delete()
    resulted_quantity = original_quantity.quantity + data.quantity
    Store.objects.filter(pk=item_id).update(quantity=resulted_quantity)
    return redirect('End_Shopping')

@api_view(['GET','PUT'])
def update_item(request, item_id):
    data = Purchase.objects.get(item_number=item_id)
    original_quantity = Store.objects.get(pk=item_id)
    Purchase.objects.filter(item_number=item_id).delete()
    resulted_quantity = original_quantity.quantity + data.quantity
    Store.objects.filter(pk=item_id).update(quantity=resulted_quantity)

    items = Store.objects.filter(pk=item_id)

    serializer = Rest_Store(items,many=True)

    return render(request, 'webapp/index.html', {'item': serializer.data})










