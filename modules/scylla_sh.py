import requests

def scylla_search(email):
    try:
        r = requests.get(f'https://scylla.so/search?q=email:{email}')
        if r.status_code in [500, 502]:
            return None
        try:
            response = r.json()
            if len(response) == 0:
                return None
            total = []
            for i in response[:10]:
                leak_name = i['fields']['domain']
                try:
                    password = i['fields']['password']
                except:
                    password = i['fields']['passhash']
                text = {
                    'Name':leak_name,
                    'Password':password
                }
                total.append(text)
            return total
        except:
            return None
    except requests.exceptions.ConnectionError:
        return None

# By Lui#6166 from Prism Intelligence Group
