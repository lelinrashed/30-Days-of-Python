import sys
import requests
from formatting import format_msg
from send_mail import send_mail


def send(name, website=None, to_email=None, verbose=False):
    assert to_email != None

    msg = format_msg(name=name, website=website)
    r = requests.get("http://httpbin.org/json")

    if verbose:
        print(name, website, to_email)

    if r.status_code == 200:
        print(r.json())
    else:
        return "There was an error"

    try:
        send_mail(text=msg, to_emails=[to_email], html=None)
        sent = True
    except:
        sent = False
        
    return sent    


if __name__ == "__main__":
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]

    email = None
    if len(sys.argv) > 2:
        email = sys.argv[2]
    response = send(name, 'lelin', verbose=True, to_email=email)
    print(response)
