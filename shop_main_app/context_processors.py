from shop_main_app.models import Category, Product


def category_list(request):
    return {'category_list': Category.objects.all()}
