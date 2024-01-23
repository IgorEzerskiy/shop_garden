from django.template.loader import get_template
import pdfkit
from shop_garden.settings import WKHTMLTOPDF_PATH


def render_from_html_to_pdf(context, template_path):
    """https://wkhtmltopdf.org/downloads.html"""
    config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_PATH)
    template = get_template(template_path)

    html = template.render(context)

    # PDF options (you can customize these as needed)
    pdf_options = {
        'page-size': 'A4',
        'encoding': 'utf-8',
    }

    # Generate PDF
    pdf_data = pdfkit.from_string(html, False, options=pdf_options, configuration=config)

    return pdf_data
