from django.shortcuts import render, redirect
from django.contrib import messages
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart_app.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            if not len(cart) == 0:
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                cart.clear()
                messages.success(request, f"Ваше замовлення успішно створено. Номер вашого замовлення {order.id}")
                return redirect('/')
            else:
                messages.error(request, f"Ваше замовлення не може бути сформовано, оскільки кошик порожній.")
                return redirect('/cart/')
        else:
            messages.error(request, f"Помилка в оформленні замовлення. "
                                    f"Будьласка, перевірте правильність вказанних Вами даних.")
            return redirect('/cart/')
