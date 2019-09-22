'''
message = MIMEMultipart()
message["from"]
message["to"]
message["subject"]
message.attach(MIMEText(content,'plain','utf-8'))
attac =
try:
    server = smtolib.SMTP_SSL(server,port)
    server.login()
    server.sendmail(sender,receiber,message.as_string())
    server.quit()
except smtplib.SMTPexception as e
     print(e)

'''