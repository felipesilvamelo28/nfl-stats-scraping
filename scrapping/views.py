import time
from decimal import Decimal
import logging
import requests

from django.http import JsonResponse
from rest_framework import viewsets
from urllib.request import urlopen
from bs4 import BeautifulSoup

from rest_framework.renderers import JSONRenderer


from .serializer import *
from scrapping.models import *

logger = logging.getLogger(__name__)
passing_url = "https://www.nfl.com/stats/player-stats/category/passing/2020/REG/all/passingyards/desc"
rushing_url = "https://www.nfl.com/stats/player-stats/category/rushing/2020/REG/all/rushingyards/desc"
receiving_url = "https://www.nfl.com/stats/player-stats/category/receiving/2020/REG/all/receivingreceptions/desc"
fumbles_url = "https://www.nfl.com/stats/player-stats/category/fumbles/2020/REG/all/defensiveforcedfumble/desc"
tackles_url = "https://www.nfl.com/stats/player-stats/category/tackles/2020/REG/all/defensivecombinetackles/desc"


class PassingsViewSet(viewsets.ModelViewSet):
    """buscando dados, salvando no banco e acessando os dados salvos"""
    queryset = Passing.objects.all()
    serializer_class = PassingSerializer


class RushingsViewSet(viewsets.ModelViewSet):
    """buscando dados, salvando no banco e acessando os dados salvos"""
    queryset = Rushing.objects.all()
    serializer_class = RushingSerializer


class ReceivingsViewSet(viewsets.ModelViewSet):
    """buscando dados, salvando no banco e acessando os dados salvos"""
    queryset = Receiving.objects.all()
    serializer_class = ReceivingSerializer


class FumblesViewSet(viewsets.ModelViewSet):
    """buscando dados, salvando no banco e acessando os dados salvos"""
    queryset = Fumbles.objects.all()
    serializer_class = FumblesSerializer


class TacklesViewSet(viewsets.ModelViewSet):
    """buscando dados, salvando no banco e acessando os dados salvos"""
    queryset = Tackles.objects.all()
    serializer_class = TacklesSerializer


def extrair(next, urls, home):
    url_complement = next[0].a['href']
    urls.append(home + url_complement)


def get_next(endereco):
    response = urlopen(endereco)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    return soup.findAll('div', {'class': "nfl-o-table-pagination__buttons"})


def get_urls(url_inicial):
    urls = []
    home = "https://www.nfl.com"
    endereco = url_inicial
    urls.append(endereco)

    contador = 0

    while contador < len(urls):
        url = urls[contador]
        next = get_next(url)
        if len(next) != 0:
            extrair(next, urls, home)
        contador += 1

    return urls


def get_passing_players(url):
    urls = get_urls(url)

    for url in urls:

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("tbody")
        itens = body.findAll("tr")
        players = []

        for item in itens:
            attributes = item.findAll("td")
            attibutes_clean = []
            for c in attributes:
                attibutes_clean.append(c.get_text().strip("\n").strip(" ").replace("\n", ""))
            players.append(attibutes_clean)

        for player in players:
            player_temp = Passing()
            player_temp.year = 2020
            player_temp.name = player[0]
            player_temp.pass_yds = Decimal(player[1])
            player_temp.yds_att = Decimal(player[2])
            player_temp.att = Decimal(player[3])
            player_temp.cmp = Decimal(player[4])
            player_temp.cmp_percent = Decimal(player[5])
            player_temp.td = Decimal(player[6])
            player_temp.int = Decimal(player[7])
            player_temp.rate = Decimal(player[8])
            player_temp.one_st = Decimal(player[9])
            player_temp.one_st_percent = Decimal(player[10])
            player_temp.twentyplus = Decimal(player[11])
            player_temp.fourtyplus = Decimal(player[12])
            player_temp.lng = Decimal(player[13])
            player_temp.sck = Decimal(player[14])
            player_temp.scky = Decimal(player[15])

            logger.info("salvando player: " + player_temp.name)
            #time.sleep(1/2)
            #player_temp.save()


def get_rushing_players(url):
    urls = get_urls(url)

    for url in urls:

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("tbody")
        itens = body.findAll("tr")
        players = []

        for item in itens:
            attributes = item.findAll("td")
            attibutes_clean = []
            for c in attributes:
                attibutes_clean.append(c.get_text().strip("\n").strip(" ").replace("\n", ""))
            players.append(attibutes_clean)

        for player in players:
            player_temp = Rushing()
            player_temp.year = 2020
            player_temp.name = player[0]
            player_temp.rush_yds = Decimal(player[1])
            player_temp.att = Decimal(player[2])
            player_temp.td = Decimal(player[3])
            player_temp.twentyplus = Decimal(player[4])
            player_temp.fourtyplus = Decimal(player[5])
            player_temp.rush_one_st = Decimal(player[6])
            player_temp.rush_one_st_percent = Decimal(player[7])
            player_temp.rush_fum = Decimal(player[8])

            logger.info("salvando player: " + player_temp.name)
            #time.sleep(1/2)
            player_temp.save()


def get_receiving_players(url):
    urls = get_urls(url)

    for url in urls:

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("tbody")
        itens = body.findAll("tr")
        players = []

        for item in itens:
            attributes = item.findAll("td")
            attibutes_clean = []
            for c in attributes:
                attibutes_clean.append(c.get_text().strip("\n").strip(" ").replace("\n", ""))
            players.append(attibutes_clean)

        for player in players:
            player_temp = Receiving()
            player_temp.year = 2020
            player_temp.name = player[0]
            player_temp.rec = Decimal(player[1])
            player_temp.yds = Decimal(player[2])
            player_temp.td = Decimal(player[3])
            player_temp.twentyplus = Decimal(player[4])
            player_temp.fourtyplus = Decimal(player[5])
            player_temp.lng = Decimal(player[6])
            player_temp.rec_1st = Decimal(player[7])
            player_temp.one_st_percent = Decimal(player[8])
            player_temp.rec_fum = Decimal(player[9])
            player_temp.rec_yac_r = Decimal(player[10])
            player_temp.tgts = Decimal(player[11])

            logger.info("salvando player: " + player_temp.name)
            #time.sleep(1/2)
            player_temp.save()


def get_fumbles_players(url):
    urls = get_urls(url)

    for url in urls:

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("tbody")
        itens = body.findAll("tr")
        players = []

        for item in itens:
            attributes = item.findAll("td")
            attibutes_clean = []
            for c in attributes:
                attibutes_clean.append(c.get_text().strip("\n").strip(" ").replace("\n", ""))
            players.append(attibutes_clean)

        for player in players:
            player_temp = Fumbles()
            player_temp.year = 2020
            player_temp.name = player[0]
            player_temp.ff = player[1]
            player_temp.fr = player[2]
            player_temp.fr_td = player[3]

            logger.info("salvando player: " + player_temp.name)
            time.sleep(1)
            #player_temp.save()
            serializer = FumblesSerializer(player_temp)
            content = JSONRenderer().render(serializer.data)
            payload = content.decode("utf-8")
            print(payload)
            headers = {'content-type': 'application/json'}
            r = requests.post("http://localhost:8080/fumble", data=payload, headers = headers)

def get_tackles_players(url):
    urls = get_urls(url)

    for url in urls:

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, "html.parser")
        body = soup.find("tbody")
        itens = body.findAll("tr")
        players = []

        for item in itens:
            attributes = item.findAll("td")
            attibutes_clean = []
            for c in attributes:
                attibutes_clean.append(c.get_text().strip("\n").strip(" ").replace("\n", ""))
            players.append(attibutes_clean)

        for player in players:
            player_temp = Tackles()
            player_temp.year = 2020
            player_temp.name = player[0]
            player_temp.comb = Decimal(player[1])
            player_temp.asst = Decimal(player[2])
            player_temp.solo = Decimal(player[3])
            player_temp.sck = Decimal(player[4])

            logger.info("salvando player: " + player_temp.name)
            #time.sleep(1/2)
            player_temp.save()


def import_data(request):
    if request.method == 'GET':

        #get_passing_players(passing_url)
        #get_rushing_players(rushing_url)
        #get_receiving_players(receiving_url)
        get_fumbles_players(fumbles_url)
        #get_tackles_players(tackles_url)

        return JsonResponse({"status": "import ok"})


