import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# %matplotlib inline
import warnings
warnings.filterwarnings('ignore')


url ="https://www.google.co.in/travel/explore?g2lb=202152%2C2502548%2C4258168%2C4260007%2C4270442%2C4274032%2C4291318%2C4305595%2C4306835%2C4308227%2C4317915%2C4322822%2C4326765%2C4328159%2C4329288%2C4366684%2C4367952%2C4372337%2C4373848%2C4385383%2C4386655%2C4386665%2C4386795%2C4387290%2C4388508%2C4270859%2C4284970%2C4291517%2C4316256%2C4356900&hl=pl&gl=pl&un=1&tfs=CBsQAxodagwIAhIIL20vMDgxbV9yDQgEEgkvbS8wY2hnaHkaHWoNCAQSCS9tLzBjaGdoeXIMCAISCC9tLzA4MW1fcAKCAQ0I____________ARACQAFIAZgBAQ#explore;f=JFK,EWR,LGA;t=r-Europe-0x46ed8886cfadda85%253A0x72ef99e6b3fcf079;li=8;lx=12;d=2016-11-29"
driver = webdriver.PhantomJS()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36")
driver = webdriver.PhantomJS(desired_capabilities=dcap,service_args=['--ignore-ssl-errors=true'])
driver.implicitly_wait(20)
driver.get(url)

driver.save_screenshot(r'flight_explorer.png')