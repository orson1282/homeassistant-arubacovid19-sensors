#!/usr/bin/python3
from bs4 import BeautifulSoup as bs
import requests
import json


def get_covid19_data():
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://epidemic-stats.com/coronavirus/aruba'
    source = requests.get(url, headers=headers)
    soup = bs(source.content, 'lxml')

    infected = soup.find("div", class_="card-body").span
    deaths = infected.find_next("div", class_="card-body").span
    recovered = deaths.find_next("div", class_="card-body").span

    infected = int(infected.text)
    deaths = int(deaths.text.split()[0])
    recovered = int(recovered.text.split()[0])
    active = infected - deaths - recovered

    data = {}
    data['infected'] = infected
    data['deaths'] = deaths
    data['recovered'] = recovered
    data['active'] = active
    return json.dumps(data)


print(get_covid19_data())
