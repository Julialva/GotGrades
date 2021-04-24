from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import os
import smtplib, ssl
class MauaScrapper(object):
    user = '18.00522-5@maua.br'
    password = str(os.getenv('RG'))

    payload= {
        'maua_email': user,
        'maua_senha': password,
     }
     
    #create session
    session = requests.session()

    #navigate to page
    response = session.post('https://www2.maua.br/mauanet.2.0', data = payload)
    report_card_page = session.get('https://www2.maua.br/mauanet.2.0/boletim-escolar')

    # reading table
    table = pd.read_html(report_card_page.text)
    report_card = table[1]
    report_card['Timestamp'] = datetime.datetime.now(datetime.timezone.utc)

    #creating output file
    path_file = user + "_report_card.csv"
    path_folder = './report_cards'
    if not os.path.exists(path_folder):
        os.mkdir(path_folder)
    path = os.path.join(path_folder,path_file)
    report_card.to_csv(path,mode='w') 
    if not os.path.exists('./report_cards/'+ user + '@standard.csv'):
        standard_file = report_card.to_csv('./report_cards/'+ user + '_standard.csv',mode='w')
    
    def compare(self,user):
        standard = pd.read_csv('./report_cards/' + user + '_standard.csv')
        new_data = pd.read_csv('./report_cards/' + user + '_report_card.csv')
        new_data_ = new_data.drop(columns='Timestamp')
        standard_ = standard.drop(columns='Timestamp')
        diff = (new_data_ != standard_).any(1)
        diff_list = diff.to_list()
        if False in diff_list:
            standard = new_data
            os.remove('./report_cards/' + user + '_standard.csv')
            port = 465
            smtp_server = 'smtp.gmail.com'
            sender_email = 'hunterpayer@gmail.com'
            receiver_email = 'julio-gris@hotmail.com'
            password = str(os.getenv('password'))
            message = """\
            Subject: Hi there

            Your grades have been updated."""
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server,port,context=context) as server:
                server.login(sender_email,password)
                server.sendmail(sender_email,receiver_email,message)
