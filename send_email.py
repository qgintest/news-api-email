import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "aeendale@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "aeendale@gmail.com"
    context = ssl.create_default_context()
    # message = """\
    #             Subject: Hi!
    #             Sample Email
    #             Bye
    #           """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))


