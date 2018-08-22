from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pyvirtualdisplay import Display

from datetime import date
import time
from dateutil.relativedelta import relativedelta

import logging
import pprint
import lxml
import json

display = Display(visible=0, size=(1024, 768))

display.start()

datasets = []
CPF = '02653207710'
PASSWORD = '168481'
exc = {'Primeira','Anterior','Próxima','Última'}

def savedata(data):
    current_time = datetime.now()

    filename = "./json/"
    filename = filename + CPF + '-{:%Y-%m-%d-%H:%M:%S}'.format(current_time) + '.json'
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    return

def save_recibo(html,numero):
    filename = "./recibos/"+CPF+'-'+numero+'.html'
    f=open(filename,'w')
    f.write(html)
    f.close()
    return

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def processtable(elem):
    global datasets
    global exc
    html = elem.get_attribute('innerHTML')
    soup = BeautifulSoup(html, "lxml")

    # The first tr contains the field names.
    #headings = [th.get_text() for th in soup.find("tr").find_all("th")]
    #print(headings)
    for row in soup.find_all("tr")[1:]:
        dataset = [td.get_text() for td in row.find_all("td")]
        if is_number(dataset[0]):
            datasets.append(dataset)
    return;

def get_all_receipts(drive,page):
    elem_receipts = driver.find_elements_by_xpath("//a[contains(@href,'CONSULTA')]")

    total_receipts = len(elem_receipts)
    print("Total Receipts =", total_receipts)
    for a in range(total_receipts):
        elem_receipts = driver.find_elements_by_xpath("//a[contains(@href,'CONSULTA')]")
        i = elem_receipts[a]
#        print (a+1, " de ", total_receipts)
        receipt = i.get_attribute('innerHTML')
#        print(receipt)
        if i.get_attribute('innerHTML') not in exc:
            if (i.get_attribute('href')):
                #print(i.location, i.size)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                action = ActionChains(driver).move_to_element(i)
                #            action.perform()
                #            passElement = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "gdvConsulta")))
                action.click(i)
                # action.click()
                action.perform()
                try:
                    recibo = driver.find_element_by_class_name('CupomFiscal')
                except:
                    print("Cannot open receipt")
                else:
                    save_recibo(recibo.get_attribute('innerHTML'), receipt)
                    #print(i)
                driver.execute_script("window.history.go(-1)")

    return

driver = webdriver.Chrome()

driver.get('https://www.nfp.fazenda.sp.gov.br/login.aspx')

#driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.HTMLUNITWITHJS)
#print(driver.desired_capabilities)

elem = driver.find_element_by_name('ctl00$ConteudoPagina$Login1$UserName')
elem.clear()
elem.send_keys(CPF)

#elem = driver.find_element_by_name('ctl00$ConteudoPagina$Login1$Password')
#elem.clear()
#elem.send_keys(PASSWORD)

#elem = driver.find_element_by_name('ctl00$ConteudoPagina$Login1$Login')
#elem.click()

#logging.basicConfig(level=logging.DEBUG)

dt_begin_r = date(2010,1,1)
dt_end_r = dt_begin_r + relativedelta(months=+3)
dt_end_r = dt_end_r + relativedelta(days=-1)

dt_begin = dt_begin_r.strftime('%d/%m/%Y')
dt_end = dt_end_r.strftime('%d/%m/%Y')
now = datetime.now()

while (dt_begin_r <= now.date()):
    print( dt_begin, dt_end)

    #second_driver = webdriver.Chrome()
    #second_driver.maximize_window()

    driver.get('https://www.nfp.fazenda.sp.gov.br/Inicio.aspx')

    elem = driver.find_element_by_name('ctl00$ConteudoPagina$btnConsultaAvancada')
    elem.click()

    elem = driver.find_element_by_name('ctl00$ConteudoPagina$txtDataIni')
    elem.clear()
    elem.send_keys(dt_begin)

    elem = driver.find_element_by_name('ctl00$ConteudoPagina$txtDataFim')
    elem.clear()
    elem.send_keys(dt_end)

    elem = driver.find_element_by_name('ctl00$ConteudoPagina$btnConsultaNF')
    elem.click()

    try:
        numberofpages = int(driver.find_element_by_id('lblPageCount').text)
    except:
        numberofpages = 1


    for i in range(1,numberofpages):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        elem = Select(driver.find_element_by_name('ctl00$ConteudoPagina$gdvConsulta$ctl23$ddlPages'))
        elem.select_by_value(str(i))
        elem = driver.find_element_by_id('gdvConsulta')
        processtable(elem)
        get_all_receipts(driver,i)

    dt_begin_r = dt_end_r + relativedelta(days=+1)
    dt_end_r = dt_begin_r + relativedelta(months=+3)
    dt_end_r = dt_end_r + relativedelta(days=-1)

    dt_begin = dt_begin_r.strftime('%d/%m/%Y')
    dt_end = dt_end_r.strftime('%d/%m/%Y')