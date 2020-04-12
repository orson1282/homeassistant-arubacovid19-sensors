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
    activo = soup.find(id='comp-k8q4vxzi').span.span.span.span.text
    data = {}
    data['positivo'] = int(positivo)
    data['morto'] = int(morto)
    data['recupera'] = int(recupera)
    data['activo'] = int(activo)
    json_data = json.dumps(data)
    print(json_data)
    return;

getcovid()
