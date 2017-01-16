#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ ="pslupczewski"

import urllib2
import requests
import re




def show_urls():

    # lista urli - sparametryzowac to ASAP
    print"\
    'http://www.sportowefakty.wp.pl/'\n \
    'http://www.kobieta.wp.pl/'\n \
    'http://www.opinie.wp.pl/'\n \
    'http://www.sportowefakty.wp.pl/'\n \
    'http://www.allegro.pl/'\n \
    'http://www.ad.nl'\n \
    'http://www.wyborcza.pl'\n \
    'http://www.gratka.pl'\n \
    'http://www.stooq.pl'\n \
    'http://www.interia.pl'\n"

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

def show_headers(input2):
    print "pokazuje naglowki:"
    resp = requests.head(input2)
    print (resp.status_code, resp.text, resp.headers)  # to pokazuje kompletne headersy dla urla

def show_150(input2):
    opener = urllib2.urlopen(input2)
    print (opener.read(150)) # printnij 150 pierwszych znakow odpowiedzi

# ZMIENNEEEEEEEEEEE!!!!!!!!!!!!!1111111111
input2 = 'http://www.trojmiasto.pl'
r = requests.get(input2)
t = r.text
print "Witaj drogi użytkowniku."
print "Oto lista urli do wyboru:"
show_urls()
print "Teraz sprawdzam taki url:"
print (input2)
print "A teraz pokaze 150 pierwszych znakow z tresci html"
show_150(input2)
print "Teraz kolej czas na nagłówki:"
show_headers(input2)
print "a na deser ciasteczka:"
show_cookies(r)
print "KONIEC"