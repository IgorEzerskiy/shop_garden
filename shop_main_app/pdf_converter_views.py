from django.http import HttpResponse
from django.template.loader import get_template

from orders.models import Order
from options_app.models import Footer

import pdfkit


def render_pdf_view(request):
    """https://wkhtmltopdf.org/downloads.html"""
    order = None
    options = None

    try:
        order = Order.objects.get(id=request.GET.get('order'))
        options = Footer.objects.first()
    except Order.DoesNotExist as ex:
        pass

    if request.user.is_authenticated:
        if order.user == request.user:
            template_path = 'pdf/download_pdf.html'
            context = {'order': order,
                       'options': options}
            path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
            config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
            template = get_template(template_path)

            html = template.render(context)

            # PDF options (you can customize these as needed)
            pdf_options = {
                'page-size': 'A4',
                'encoding': 'utf-8',
            }

            # Generate PDF
            pdf_data = pdfkit.from_string(html, False, options=pdf_options, configuration=config)

            # Create an HTTP response with PDF content
            response = HttpResponse(pdf_data, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="order.pdf"'

            return response
