import sys
import requests

from pprint import pprint

url = "https://api.shodan.io/shodan/host/{ip}?key={apikey}"

r = requests.get(url.format(apikey=sys.argv[1], ip=sys.argv[2]))

if r.status_code != 200:
    print("error ({})".format(r.status_code))
    sys.exit(1)

pprint(r.json())
