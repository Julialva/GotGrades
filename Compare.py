import pandas as pd
import os
import smtplib, ssl
def compare(user):
    standard = pd.read_csv('./report_cards/' + user + '_standard.csv')
    new_data = pd.read_csv('./report_cards/' + user + '@maua.br_report_card.csv')
    if new_data != standard:
        standard = new_data
        os.remove('./report_cards/' + user + '_standard.csv')
        port = 465
        smtp_server = 'smtp.gmail.com'
        sender_email = 'hunterpayer@gmail.com'
        receiver_email = 'julio-gris@hotmail.com'
        password = 'julios34'
        message = """\
        Subject: Hi there

        Your grades have been updated."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,receiver_email,message)