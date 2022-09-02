import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# read data from json file
with open('../pages/testdata.json') as data_file:
    # dt=data_file.read()
    data = json.load(data_file)


class OpenBrowser():
    def __init__(self):
        self.service = Service(executable_path=data["chrome_driver_path"])
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(data["website_link"])
