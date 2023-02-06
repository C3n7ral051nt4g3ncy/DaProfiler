import requests, bs4
from bs4 import BeautifulSoup

def twitter_search(name,pren):
    try:
        url = f"https://www.twuko.com/search?term={pren}+{name}&type=user"

        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        full_name = soup.find_all('div',{'class':'flex items-center'})
        username  = soup.find_all('a',{'class':'text-sm'})

        final_accounts = []

        for i in range(len(full_name)):
            usernamee = username[i].text
            fullname  = full_name[i].text
            final_accounts.append(f'{usernamee}\t|{fullname}')
        return final_accounts or None
    except:
        return None
