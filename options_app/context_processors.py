from options_app.models import Footer
from options_app.forms import ContactModelForm


def footer_info(request):
    return {'footer_info': Footer.objects.all().first(),
            'question_form': ContactModelForm()}
