
def email():
    server = smtplib.SMTP('SMTPCORP.PRODAM', 25)
    msg = MIMEText(f'tetsteeeeee')
    sender = 'smsdtic@prefeitura.sp.gov.br'
    recipients = ['giovanifranco@prefeitura.sp.gov.br','evairbd@prefeitura.sp.gov.br']
    msg['Subject'] = "Teste de SMTP PYTHON"
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    server.sendmail(sender, recipients, msg.as_string())

    server.quit()
    
    
    
