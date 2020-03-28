import requests 
from bs4 import BeautifulSoup 
import csv
import urllib.request
import time 
  
URL = "https://google.org/crisisresponse/covid19-map"
r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')
soup.findAll('a')
  
 
   
  





