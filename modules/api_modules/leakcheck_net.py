import leakcheck
from leakcheck import LeakCheckAPI

from colorama import Fore

def leak_check_api(mail):
    api = LeakCheckAPI()
    """
    GET YOUR KEY AT https://leakcheck.net/ 
    """
    keyy = "YOUR_KEY"
    if keyy == "YOUR_KEY":
        return None
    full_results = []
    try:
        api.set_key(keyy)
        api.set_type("email")
        api.set_query(mail)
        result = api.lookup(with_sources=1)[:10]
        for i in result:
            try:
                password  = i['line']
            except IndexError:
                password = None
            try:
                leak_name = i['sources']
            except IndexError:
                leak_name = None
            try:
                leak_date = i['last_breach']
            except IndexError:
                leak_date = None
            dict_res = {
                'password':password,
                'leak_name':str(leak_name).replace("'","").replace("[","").replace("]",""),
                'leak_date':leak_date
            }
            full_results.append(dict_res)
        return full_results or None
    except:
        return None
