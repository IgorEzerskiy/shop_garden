import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Environment, FileSystemLoader
from celery import shared_task

from django.conf import settings


templates_names = {
    'order': 'email_notification.html',
    'sign up': 'registration_notification.html'
}


class EmailMessage:
    def __init__(self, from_email, to_email, subject, context, mode):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.context = context
        self.mode = mode

    def build_message(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        template_directory = os.path.join(current_directory, 'templates')
        env = Environment(loader=FileSystemLoader(template_directory))
        template_name = templates_names[self.mode]
        template = env.get_template(template_name)
        context = self.context
        email_content = template.render(context)

        msg = MIMEMultipart()
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg['Subject'] = self.subject
        msg.attach(MIMEText(email_content, 'html'))
        return msg


class SMTPServer:

    def __init__(self):
        self.smtp_server = settings.SMTP_SERVER
        self.smtp_port = settings.SMTP_PORT
        self.username = settings.SMTP_EMAIL_USERNAME
        self.password = settings.SMTP_EMAIL_PASSWORD
        self.server = self.__connect()

    def __connect(self):
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.username, self.password)
        return server

    def disconnect(self):
        self.server.quit()


class EmailSender(SMTPServer):

    def send_email(self, email_message):
        try:
            self.server.sendmail(email_message.from_email, email_message.to_email,
                                 email_message.build_message().as_string())
            # print(f"Email успешно отправлен!")
        except Exception as e:
            print(f"Ошибка при отправке email: {e}")
        finally:
            self.disconnect()


@shared_task
def email_notific(message_info: dict, email_to: str, mode: str) -> None:
    sender = EmailSender()

    message = EmailMessage(settings.SMTP_EMAIL_USERNAME, email_to, 'Ваше замовлення', message_info, mode=mode)
    sender.send_email(message)

# # Пример использования
# if __name__ == "__main__":
#     email_notific()
