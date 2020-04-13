#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
import requests
import json


def get_covid19_data():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://epidemic-stats.com/coronavirus/aruba'
    source = requests.get(url, headers=headers)
    soup = bs(source.content, 'lxml')

    positivo = soup.find("div", class_="card-body").span
    morto = positivo.find_next("div", class_="card-body").span
    recupera = morto.find_next("div", class_="card-body").span

    positivo = int(positivo.text)
    morto = int(morto.text.split()[0])
    recupera = int(recupera.text.split()[0])
    activo = positivo - morto - recupera

    data = {}
    data['positivo'] = positivo
    data['morto'] = morto
    data['recupera'] = recupera
    data['activo'] = activo
    return json.dumps(data)


print(get_covid19_data())
