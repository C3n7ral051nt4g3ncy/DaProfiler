import threading, requests, bs4
from bs4 import BeautifulSoup
from modules import mail_check

def check(name,pren):
    results = [
        f"{name}.{pren}@gmail.com",
        f"{name}.{pren}@yahoo.com",
        f"{name}{pren}@yahoo.com",
        f"{name}{pren}@yahoo.fr",
        f"{name}.{pren}@aol.com",
        f"{name}{pren}@aol.com",
        f"{name}.{pren}@hotmail.com",
        f"{name}{pren}@hotmail.com",
        f"{name}{pren}@hotmail.fr",
        f"{name}{pren}@outlook.fr",
        f"{name}.{pren}@outlook.com",
        f"{name}{pren}@outlook.com",
    ]
    valid_mails = []
    for i in results:
        a = mail_check.verify(mail=i)
        if a is not None:
            valid_mails.append(i)
    return valid_mails

def skype2email(name,pren):
    url = f"https://www.skypli.com/search/{name} {pren}"
    r = requests.get(url)
    page = r.content
    features = "html.parser"
    soup = BeautifulSoup(page, features)

    profiles = soup.find_all(
        'span', {'class': 'search-results__block-info-username'}
    )[:5]

    profiless = [
        i.text.replace('live:', '').replace('_1', '')
        for i in profiles
        if "live:." not in i.text
    ]
    valid_emails = []

    for i in profiless:
        emails = [
            f"{i}@aol.com",
            f"{i}@yahoo.com",
            f"{i}@gmail.com",
            f"{i}@hotmail.com",
            f"{i}@hotmail.fr",
            f"{i}@outlook.fr",
            f"{i}@outlook.com",
        ]
        for i in emails:
            a = mail_check.verify(mail=i)
            if a is not None:
                valid_emails.append(i)
    return valid_emails
