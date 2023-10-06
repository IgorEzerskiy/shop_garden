from django.shortcuts import render, redirect
from django.contrib import messages
from order_app.models import OrderItem
from order_app.forms import OrderCreateForm
from cart_app.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            messages.success(request, f"Ваше замовлення успішно створено. Номер вашого замовлення {order.id}")
            return redirect('/')
