#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="pslupczewski"

import urllib2
import requests
import re
import time
import logging



# /////////// moduly do wywyolywania na wczytanych danych
def show_urls(lista_adresow):

    for k, v in lista_adresow.iteritems():
        print k, v


def headers():

    dict_headers = {
    'X-Served-By',
    'Server',
    'Connection',
    'Cache-Control',
    'Date',
    'Content-Type'
    }

def check_headers(r):
    """""module for checking some headers dependencies"""
    try:
        r.headers['X-Served-By']
        print "['X-Served-By']", r.headers['X-Served-By']
    except Exception:
        print "x-served-by error"
    try:
        r.headers['Server']
        print "['Server']", r.headers['Server']
    except Exception:
        print "server error"
    try:
        r.headers['Connection']
        print "['Connection']", r.headers['Connection']
    except Exception:
        print "server error"
    try:
        r.headers['Cache-Control']
        print "['Cache-Control']", r.headers['Cache-Control']
    except Exception:
        print "cache-control error"
    try:
        r.headers['Date']
        print "['Date']", r.headers['Date']
    except Exception:
        print "date error"
    try:
        r.headers['Content-Type']
        print "['Content-Type']", r.headers['Content-Type']
    except Exception:
        print "content-typer error"

    print r.headers
    return r.headers

def show_cookies(r):
    """"module for preview of cookies set by request"""
    print r.cookies


def display_content_of_source(r):
    """module for displaying source of content"""
    print t


def search_for_polish_adjectives(t):
    """"module for searching polish adjectives in content
    effect is displayed with byte postion """
    for m in re.finditer(r"\w+owy", t):
        # print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))
        a = '%s' % (m.group(0))
        print a

def show_headers(input):
    print "Probuje odczytac naglowki..."
    try:
        resp = requests.head(input)
        print (resp.status_code, resp.text, resp.headers)
    except Exception:
        print "Niestety nie udało się odczytać nagłówków"


def show_150(input):
    try:
        opener = urllib2.urlopen(input)
        print (opener.read(150))
    except: # except na error urlliba
        "cos sie popsulo"


def time_tick():
    time.sleep(1)

# koniec modułów


lista_adresow = {

'SG WP' : 'http://www.wp.pl/',
'ALLEGRO' : 'http://www.allegro.pl/',
'AD' : 'http://www.ad.nl',
'Reuters' : 'http://www.reuters.com',
'Gratka' : 'http://www.gratka.pl',
'Stooq' : 'http://www.stooq.pl',
'Interia' : 'http://www.interia.pl',
'Trójmiasto' : 'http://www.trojmiasto.pl',
'Facebook' : 'http://www.facebook.com',
'Onet' : 'http://www.onet.pl',
'Twitter' : 'http://www.twitter.com',
'Google' : 'http://www.google.com',
'Moja PG' : 'http://moja.pg.gda.pl/',
'Reddit' : 'http://www.reddit.com',
'Baidu' : 'http://www.baidu.com',

}


# ===================== poczatek logiki programu

# greet user

print "\t\t\t\t\t\t\tWitaj w programie traffic_analyzer drogi użytkowniku.\n"
print "Oto lista urli do wyboru:\n"
show_urls(lista_adresow)
print "Wybierz nr z listy url (numeracja zaczyna sie od 0):\n"

# zaloguj uruchomienie

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s')
logging.warning('= = = = = = Program run man.')

# wczytaj dane

for adres in lista_adresow.items():
    print adres[1]
    hard_input = adres[1]

    try:
        r = requests.get(hard_input)
        t = r.text
    except:
        print "requests nie dziala"
    print "Stestujmy je:\n"
    try:
        headers_instance = check_headers(r)
        logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s')
        logging.warning("checking")
        logging.warning(hard_input)
        logging.warning(headers_instance)
        log_time(tak)
    except:
        print "nie ma co testować..."

print "A teraz pokaze 150 pierwszych znakow z treści:\n"
show_150(hard_input)

headers_instance = headers()

time.sleep(1)
show_headers(hard_input)
time.sleep(1)

