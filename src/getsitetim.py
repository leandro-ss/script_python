from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import pandas as pd
import datetime
import subprocess
import time
from pyzabbix import ZabbixMetric, ZabbixSender
import json


timeout = 60
elapsed = timeout
success = 0
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_page_load_timeout(timeout)

tc = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')

try:
    driver.get('http://www.tim.com.br')
    time.sleep(10)
    driver.save_screenshot('/home/inmetrics/getsitetim/image/'+tc+'.png')
    timings = driver.execute_script("return window.performance.getEntries();")
except:
    success = 0
else:
    success = 1

driver.quit()

#print(timings)

if success:
    try:
        elapsed = timings[0]['duration']
    except:
        elapsed = timeout
        success = 0
    else:
        f = open('/home/inmetrics/getsitetim/json/'+tc+'.json','w')
        f.write(json.dumps(timings))
        f.close()

        df = pd.read_json(json.dumps(timings))
        df2 = df.loc[:,['name','duration']]
        df2 = df2.sort_values('duration', ascending=0)
        df2.index.names = ['Index']

        df2.to_csv('/home/inmetrics/getsitetim/csv/'+tc+".csv")

        #print(df2)

result_str = tc + "," + str(elapsed) + "," + str(success)+"\n"

with open("/home/inmetrics/getsitetim/results.csv", "a") as myfile:
    myfile.write(result_str)

packet = [
    ZabbixMetric('Site TIM Selenium', 'response_selenium', elapsed),
    ZabbixMetric('Site TIM Selenium', 'success_selenium', success)
]

sender = ZabbixSender(use_config='/home/inmetrics/getsitetim/zabbix_agentd.conf')
sender.send(packet)

