import requests

APIKEY = '011d892e19d82635af74f10ed45ae6b7'
cities = [{'city':'Boston','contry':'us'},{'city':'Beijing','contry':'cn'},{'city':'Chongqing','contry':'cn'}]
for item in cities:
    resp = requests.get('http://api.openweathermap.org/data/2.5/weather?q={0},{1}&APPID={2}'.format(item['city'], item['contry'], APIKEY))
    if resp.status_code == requests.codes.ok:
        print(item['city'], item['contry'])
        print(resp.json())
