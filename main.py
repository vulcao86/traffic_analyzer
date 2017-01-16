#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="pslupczewski"

import urllib2
import requests
import re

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
        print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))

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
    except:
        "cos sie popsulo"



lista_adresow = {

'0 SG WP' : 'http://www.wp.pl/',
'1 ALLEGRO' : 'http://www.allegro.pl/',
'2 AD' : 'http://www.ad.nl',
'3 Wyborcza' : 'http://www.wyborcza.pl',
'4 Gratka' : 'http://www.gratka.pl',
'5 Stooq' : 'http://www.stooq.pl',
'6 Interia' : 'http://www.interia.pl',
'7 Trójmiasto' : 'http://www.trojmiasto.pl',
'8 Facebook' : 'http://www.facebook.com',
'9 Wakacje' : 'http://www.wakacje.pl',

}

print "\nWitaj w programie traffic_analyzer drogi użytkowniku.\n"
print "Oto lista urli do wyboru:\n"
show_urls(lista_adresow)
print "Wybierz nr z listy url:\n"

user_choice = raw_input()
user_choice = int(user_choice)
list = lista_adresow.values()
input = list[user_choice]
r = requests.get(input)
t = r.text

print "Wybrałeś nr:"
print user_choice
print (input)
print "Wciśnij enter"
confirm = raw_input()
print "A teraz pokaze 150 pierwszych znakow z treści:\n"
show_150(input)
print "Teraz kolej czas na nagłówki:"
show_headers(input)
print "Stestujmy je:"
check_headers(r)
print "Wyszukajmy przymiotnikow w tresci."
search_for_polish_adjectives(t)
print "a na deser ciasteczka:"
show_cookies(r)
print "KONIEC"
