import requests,bs4
from bs4 import BeautifulSoup

def death_search(name,pren):
    try:
        url = f"https://www.avis-de-deces.net/avis-de-deces/?nomprenomdefunt={name}"
        r = requests.get(url)
        page = r.content
        features = "html.parser"
        soup = BeautifulSoup(page, features)

        names   = soup.find_all('h2')
        villes  = soup.find_all('span',{'class':'ville'})

        profile_list = []

        for i in range(len(names)):
            name = names[i].text.strip()
            loc  = villes[i].text.strip()
            profile_list.append({'Name':name,'Loc':loc.replace('- ','')})

        return profile_list or None
    except:
        return None
