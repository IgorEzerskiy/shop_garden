from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_POST

from orders.forms import OrderCreateForm
from shop_main_app.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        if not product.quantity < cd['quantity']:
            cart.add(product=product,
                     quantity=cd['quantity'],
                     override_quantity=cd['override'])
        else:
            messages.error(request, f"Ви вказали кількість({cd['quantity']}) товару більшу ніж є на складі.")
            form.add_error('quantity', 'error')
            return redirect(f'/product/{product.slug}')
        return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True})

    if request.user.is_authenticated:
        user_info = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone': request.user.phone,
        }
        order_form = OrderCreateForm(initial=user_info)
    else:
        order_form = OrderCreateForm()

    if cart.cart.values():
        total_price = cart.get_total_price()
    else:
        total_price = 0

    return render(request, 'cart_details.html', {'total_price': total_price,
                                                 'cart': cart,
                                                 'order_form': order_form}
                  )
