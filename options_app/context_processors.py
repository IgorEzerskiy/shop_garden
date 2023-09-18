from options_app.models import Footer


def footer_info(request):
    return {'footer_info': Footer.objects.all().first()}
