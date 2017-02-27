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

def check_headers_nice(r, headers_to_be_checked):
    """""module for checking some headers dependencies in loop for created list of headers"""

    for header in headers_to_be_checked:
        ad_hoc_headers_instance = r.headers(header)
        print "{0} header has value {1}".format( header, ad_hoc_headers_instance)
    print r.headers
    return r.headers

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
    try:
        r.headers['Status']
        print "['Status']", r.headers['Status']
    except Exception:
        print "Status error"
    try:
        r.headers['x-response-time']
        print "['x-response-time']", r.headers['x-response-time']
    except Exception:
        print "'x-response-time' error"
    try:
        r.headers['X-CDN']
        print "['X-CDN']", r.headers['X-CDN']
    except Exception:
        print "'X-CDN' error"


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

headers_to_be_checked = {

    'content-type'
    'cache-control',
    'Connection',
    'Cache-Control',
    'date',
    'Date',
    'Content-Type',
    'x-response-time',
    'X-CDN'
    'X-XSS-Protection'
    'strict-transport-security'
    'x-twitter-response-tags',
    'x-transaction',
    'x-content-type-options',
    'content-encoding',
    'transfer-encoding',
    'set-cookie',
    'expires',
    'server',
    'last-modified',
    'x-xss-protection',
    'x-connection-hash',
    'x-ua-compatible',
    'pragma',
    'x-frame-options',
    'X-Served-By',
    'Server',

    }

lista_adresow = {

'SG WP' : 'http://www.wp.pl/',
'SG WP epty redir' : 'http://www.wp.pl/?_adv_=emptyrmredir',
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
'Ebay' : 'http://www.ebay.com',
'Amazon' : 'http://www.amazon.com',
'Wybrzeze24' : 'http://www.wybrzeze24.pl',
'Youtube' : 'http://www.youtube.com',
'OLX' : 'http://www.olx.pl',
'Pracuj' : 'http://www.pracuj.pl'
}

lista_adresow_wp = {

'SG WP' : 'http://www.wp.pl/',
'SF WP' : 'http://www.sportowefakty.wp.pl/',
'SFWP' : 'http://www.sportowefaktywp.pl/',
'opinie' : 'http://www.opinie.wp.pl/',
'Facet WP' : 'http://www.facet.wp.pl/',
'SG WP empty redir' : 'http://www.wp.pl/?_adv_=emptyrmredir',
'SG WP adstream' : 'http://adv.wp.pl/RM/ads/adstream_lx.ads/komorkomania.pl/index.html/L26/1222531184/x03/OasDefault/WP_GoogleADX_Blomedia_bill/rectangle_DFP_async674732.html/54372f383656695575576f414469796e?pvid=efd0531e716f8de85d21&pc=&cid=/&PWA_adbd=0&_RM_EMPTY_',

}

lista_adresow_banki = {

'MBANK' : 'http://www.mbank.pl/',
'WBK' : 'http://www.centrum24.pl/',
'ING' : 'http://www.ing.pl/',

}

sgwp = {

'SG WP' : 'http://www.wp.pl/'

}

# ===================== poczatek logiki programu

# greet user

print "\t\t\t\t\t\t\tWitaj w programie traffic_analyzer drogi użytkowniku.\n"
print "Oto lista urli do wyboru:\n"
show_urls(lista_adresow)
print "Oto lista urli WP\n"
show_urls(lista_adresow_wp)
print "banki\n"
show_urls(lista_adresow_banki)
print "Wybierz nr z listy url (numeracja zaczyna sie od 0):\n"

# zaloguj uruchomienie

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s')
logging.warning('= = = = = = = = = = = = = = = = = = Program run man.')

# wczytaj dane
list_in_use = lista_adresow
for adres in list_in_use.items():
    print adres[1]
    hard_input = adres[1]

    try:
        r = requests.get(hard_input)
        t = r.text
        try:
            headers_instance = check_headers(r)
            logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s')
            logging.debug("list of links to be tested")
            logging.debug(list_in_use)
            logging.debug("testing....")
            time_tick()
            logging.warning("========= = = = = = = new testcase")
            # logging.warning(list_in_use[0])
            logging.warning("checking address")
            time_tick()
            logging.warning(hard_input)
            logging.warning("checking headers...")
            time_tick()
            logging.warning(headers_instance)
            logging.warning("zalogowano nagloweczki ^^")
        except:
            print "conenction failed"
            logging.warning("cconnection faiulileds = = = = = =  fakap here = = = = = = ")
    except:
        print "nie ma co testować..."

print "A teraz pokaze 150 pierwszych znakow z treści:\n"
show_150(hard_input)

headers_instance = headers()

time.sleep(1)
show_headers(hard_input)
time.sleep(1)

