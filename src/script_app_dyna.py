# Print the list of tiers for an application

import requests
import urllib
import sys

HOSTNAME = "https://tesla2018073118022510.saas.appdynamics.com"
USR = "tesla2018073118022510@tesla2018073118022510"
PWD = "ap5sj8coz5ld"

PARAM_DEFAULT = {"duration-in-mins":"43200", "time-range-type":"BEFORE_NOW", "output":"json", "rollup":"false"}
PARAM_BT_AVG_TIME = {"metric-path":"Business Transaction Performance|Business Transactions|{tierName}|{internalName}|Average Wait Time (ms)"}
PARAM_BT_CAL_MIN = {"metric-path":"Business Transaction Performance|Business Transactions|{tierName}|{internalName}|Calls per Minute"}

URL_APP_BT_LIST = "https://tesla2018073118022510.saas.appdynamics.com/controller/rest/applications/{id}/business-transactions?output=json"
URL_METRIC_DATA = "https://tesla2018073118022510.saas.appdynamics.com/controller/rest/applications/MyApp/metric-data"
URL_APPLICATION = "https://tesla2018073118022510.saas.appdynamics.com/controller/rest/applications?output=json"

####################################################################################################################################
def collect():
    for app in requests.get(URL_APPLICATION, auth=(USR, PWD)).json():
        for bt in requests.get(URL_APP_BT_LIST.format_map(app), auth=(USR, PWD)).json():

            param = {k: v.format_map(bt) for k, v in PARAM_BT_AVG_TIME.items()}
            
            param.update(PARAM_DEFAULT)

            response = requests.get(URL_METRIC_DATA, auth=(USR, PWD), params=param)

            json = response.json()
            
            for result in json:
                
                if result['metricValues']:
                    try:
                        for value in result['metricValues']:
                            yield result['metricPath'], result['frequency'], value['value'], value['current'], value['min'], value['max'], value['count']
                    except KeyError:
                        sys.stderr.write('Error test:'+result['metricPath'])  
                        pass

####################################################################################################################################

import csv
with open('test.csv', 'w', newline='\n') as csvfile:
    wrt = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for row in collect():
        wrt.writerow(row)