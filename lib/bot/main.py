import re
import json
import urllib.request

def urlCheck():

    url = 'http://ipinfo.io/json'
    response = urllib.request.urlopen(url)
    data = json.load(response)

    IP=data['ip']
    org=data['org']
    city = data['city']
    country=data['country']
    region=data['region']

    #print('Your IP detail\n ')
    #print('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP))
    print(f"IP {country}")

