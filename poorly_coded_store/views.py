from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(Product.objects.get(id= int(request.POST["price"])).price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    created_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    print(created_order)
    return redirect(f"/success/{created_order.id}")

def success(request, order_id):
    total_spent= 0
    total_quantity = 0
    for order in Order.objects.all():
        total_spent += order.total_price
        total_quantity += order.quantity_ordered
    context = {
        'order_price' : Order.objects.get(id=order_id).total_price,
        'total_spent': total_spent,
        'total_quantity': total_quantity
    }
    return render(request, "store/checkout.html", context)