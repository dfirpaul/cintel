import sys
import requests

urls = {
    'facebook' : 'https://facebook.com/{}',
    'twitter' : 'https://twitter.com/{}',
    'instagram' : 'http://instagram.com/{}',
}

username = sys.argv[1]

for site,url in urls.items():
    r = requests.get(url.format(username))
    print(site, r.status_code)
