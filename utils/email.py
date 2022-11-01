from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError
#def email():
#    server = smtplib.SMTP('SMTPCORP.PRODAM', 25)
#    msg = MIMEText(f'tetsteeeeee')
#    sender = 'smsdtic@prefeitura.sp.gov.br'
#    recipients = ['giovanifranco@prefeitura.sp.gov.br','evairbd@prefeitura.sp.gov.br']
#    msg['Subject'] = "Teste de SMTP PYTHON"
#    msg['From'] = sender
#    msg['To'] = ", ".join(recipients)
#    server.sendmail(sender, recipients, msg.as_string())
#
#    server.quit()
#    
    
def mail(usere, user, userp):
    subject = "Redefinição de senha solicitada"
    email_template_name = "password/password.txt"
    c = {
    "email":usere,
    'domain':'127.0.0.1:8000',
    'site_name': 'Website',
    "uid": urlsafe_base64_encode(force_bytes(userp)),
    "user": user,
    'token': default_token_generator.make_token(user),
    'protocol': 'http',
    }

    email = render_to_string(email_template_name, c)    
    send_mail(subject, email, 'oci@smsprefeiturasp.org' , [usere], fail_silently=False)