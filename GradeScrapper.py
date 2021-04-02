from bs4 import BeautifulSoup
import requests
import pandas as pd
import datetime
import os
class MauaScrapper(object):
    user = '18.00522-5@maua.br'
    password = '393530140'

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
    if not  os.path.exists(path_folder):
        os.mkdir(path_folder)
    path = os.path.join(path_folder,path_file)
    report_card.to_csv(path,mode='w') 
