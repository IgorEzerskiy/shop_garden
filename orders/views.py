import asyncio

from django.db.transaction import atomic
from django.shortcuts import redirect
from django.contrib import messages
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart_app.cart import Cart
from email_sender import email_notific
from shop_garden.settings import INFO_BOT


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            if not len(cart) == 0:
                with atomic():
                    order = form.save(commit=False)
                    if request.user.is_authenticated:
                        order.user = request.user
                    order.save()

                    order_info_for_email_notific = {'products': []}

                    for counter, item in enumerate(cart):
                        product_item = item['product']
                        product_item.quantity = product_item.quantity - item['quantity']
                        product_item.number_of_purchases += 1

                        if not product_item.quantity:
                            product_item.availability = False

                            # telegram notification

                            product_info_for_bot = {'product_name': product_item.title,
                                                    'product_slug': product_item.slug
                                                    }
                            asyncio.run(INFO_BOT.send_message_when_the_product_is_out_of_stock(
                                product_info=product_info_for_bot))

                        product_item.save()
                        OrderItem.objects.create(order=order,
                                                 product=product_item,
                                                 price=item['price'],
                                                 quantity=item['quantity'])
                        # email notification

                        order_info_for_email_notific['products'].append({
                                'name': product_item.title,
                                'quantity': item['quantity'],
                                'price': item['quantity'] * item['price']
                                })

                cart.clear()

                # telegram notification

                order_info_for_bot = {'order_id': order.id,
                                      'order_price': order.get_total_cost(),
                                      'buyer_email': order.email,
                                      'buyer_phone': order.phone,
                                      'buyer_f_l_name': order.first_name + ' ' + order.last_name,
                                      'buyer_delivery_city': order.city,
                                      'buyer_delivery_warehouse': order.warehouse
                                      }
                asyncio.run(INFO_BOT.send_message_that_order_created(report_info=order_info_for_bot))

                # email notification

                order_info_for_email_notific.update({
                    f'order_total_cost': order.get_total_cost(),
                    'order_id': order.id,
                    'buyer_phone': order.phone,
                    'buyer_f_l_name': order.first_name + ' ' + order.last_name,
                    'buyer_delivery_city': order.city,
                    'buyer_delivery_warehouse': order.warehouse,
                    'order_created': order.created
                })

                # email notification
                email_notific(message_info=order_info_for_email_notific, email_to=order.email)

                messages.success(request, f"Ваше замовлення успішно створено. Номер вашого замовлення {order.id}")
                return redirect('/')
            else:
                messages.error(request, f"Ваше замовлення не може бути сформовано, оскільки кошик порожній.")
                return redirect('/cart/')
        else:
            messages.error(request, f"Помилка в оформленні замовлення. "
                                    f"Будьласка, перевірте правильність вказанних Вами даних.")
            return redirect('/cart/')
