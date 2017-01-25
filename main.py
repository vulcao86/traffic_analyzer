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


def check_headers(r):
    """""module fo r checking some headers dependencies"""
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
        print '%s' % (m.group(0))


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


def log_time(tak):
    logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s')
    logging.warning(tak)
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

print "\nWitaj w programie traffic_analyzer drogi użytkowniku.\n"
print "Oto lista urli do wyboru:\n"
show_urls(lista_adresow)
print "Wybierz nr z listy url (numeracja zaczyna sie od 0):\n"

# zaloguj uruchomienie

logging.basicConfig(filename='example.log', format='%(asctime)s %(message)s')
logging.warning('Program uruchomiono.')

# wczytaj dane

user_choice = raw_input()
user_choice = int(user_choice)
list = lista_adresow.values()
print list
# dokonaj wyobru elementu na liscie powstalej z wartosci zmiennej lista_adresów

input = list[user_choice]
# input na sztywno override
input = 'http://www.reuters.com'
r = requests.get(input)
# requesty na inpucie
# robimy z tego tekst
t = r.text

print "Wybrałeś nr:"
print user_choice
print (input)
print "Wciśnij enter"
print "A teraz pokaze 150 pierwszych znakow z treści:\n"
show_150(input)
print "Teraz kolej czas na nagłówki:"
time.sleep(1)
show_headers(input)
time.sleep(1)
print "Stestujmy je:"
check_headers(r)
time.sleep(1)
print "Wyszukajmy przymiotnikow w tresci."
time.sleep(1)
search_for_polish_adjectives(t)
print "a na deser ciasteczka:"
time.sleep(1)
show_cookies(r)
ciacha = show_cookies(r)
log_time(str(ciacha))
log_time("powinny byc ciacha...")
"ktore zalogowalem"
print "wiecej? ( wpisz tak )"

user_choice_yesno = raw_input()

if user_choice_yesno == "tak":
    print "ok, wyświetlam treść"
    time_tick()
    display_content_of_source(r)
    log_time("tak")
else:
    print "ok nie to nie"
print "KONIEC"
