from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.mail import send_mail, BadHeaderError

    
def mail(usere, user, userp):
    subject = "Cadastre sua senha"
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
    
    

    