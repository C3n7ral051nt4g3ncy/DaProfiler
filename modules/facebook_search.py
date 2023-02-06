import requests, bs4, re
from bs4 import BeautifulSoup

def facebook_search(name,pren):
    url = f"https://fr-fr.facebook.com/public/{pren}-{name}"
    page = requests.get(url).content.decode('utf-8')
    nameAccount = re.findall("width=\"72\" height=\"72\" alt=\"([a-zA-Z0-9_ é , ]+)\" />", page)
    total_accounts = [
        i
        for i in nameAccount
        if name.lower() in i.lower() and pren.lower() in i.lower()
    ]
    return total_accounts or None

'''
This code cand be found at : 
https://github.com/lulz3xploit/LittleBrother/blob/master/core/facebookSearchTool.py
'''
