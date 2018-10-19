import requests

APIKEY = '011d892e19d82635af74f10ed45ae6b7'
resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Boston,us&APPID={0}'.format(APIKEY))
if resp.status_code == requests.codes.ok:
    print(resp.json())
