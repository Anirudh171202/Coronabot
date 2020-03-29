import requests 
from bs4 import BeautifulSoup 
import csv
import urllib.request
import time 
  
def returnCases(country):
    URL = "https://google.org/crisisresponse/covid19-map"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
  
    return(dict(eval(soup.find( 'div',attrs={"class":'data_container'})['data-map-data'])))[country]






  
 
   
  





