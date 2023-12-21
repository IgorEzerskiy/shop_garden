from django.template.loader import get_template
import pdfkit


def render_from_html_to_pdf(context, template_path):
    """https://wkhtmltopdf.org/downloads.html"""
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

    return pdf_data
