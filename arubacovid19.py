#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
import requests
import json

def getcovid():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.arubacovid19.org/'
    source = requests.get(url, headers=headers)
    soup = bs(source.content, 'lxml')
    positivo = soup.find(id='comp-k7yvjsdj').span.text
    recupera = soup.find(id='comp-k8bojc5u').span.text
    morto = soup.find(id='comp-k8bojw0s').span.text
    data = {}
    data['positivo'] = positivo
    data['morto'] = morto
    data['recupera'] = recupera
    json_data = json.dumps(data)
    print(json_data)
    return;

getcovid()
