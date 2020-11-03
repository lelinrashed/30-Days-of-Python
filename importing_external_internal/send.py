import sys
import requests
from formatting import format_msg


def send(name, website=None, verbose=False):
    msg = format_msg(name=name, website=website)
    r = requests.get("http://httpbin.org/json")

    if verbose:
        print(name, website)

    if r.status_code == 200:
        print(r.json())
    else:
        return "There was an error"


if __name__ == "__main__":
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    response = send(name, 'lelin', verbose=True)
    print(response)
