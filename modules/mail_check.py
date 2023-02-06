#trouvé sur "https://docs.isitarealemail.com/how-to-validate-email-addresses-in-python"
# modifié (un peu) par eupone
import requests

def verify(mail):
    response = requests.get(
        f"https://isitarealemail.com/api/email/validate?email={mail}",
        params={'Authorization': 'fa86a707-750e-485c-8ec3-86eddd7ec4d0'},
        headers={
            'Authorization': "Bearer fa86a707-750e-485c-8ec3-86eddd7ec4d0"
        },
    )
    try:
        data = response.json()
        status = data['status']
        return True if status == "valid" else None
    except:
        return None
