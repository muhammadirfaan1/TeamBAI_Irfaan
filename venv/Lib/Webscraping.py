import requests
from bs4 import BeautifulSoup as bs
import json


class Scanning:
    print("---Header Response---")
    headers = {
        'User-Agent': 'Mobile'     #header spoofing
    }

    url = 'http://172.18.58.238/headers.php'
    r = requests.get(url, headers=headers)

    print("Status Code: ", r.status_code)
    print("Header: " + r.text)
    print(" ")

class Webscraping:
    totalimages = 0
    print("---WebScraping---")
    print("List of Images: ")
    Domain = "http://172.18.58.238/index.php"
    url = "http://172.18.58.238/multi/img/"
    filetype = ".jpg"

    def get_soup(url):
        return bs(requests.get(url).text, "html.parser")    #extracts the html text

    for link in get_soup(url).find_all("a"):    #finds for all hyperlinks
        file_link = link.get('href')    #extracts only the links in the href tag
        if filetype in file_link:
            if not 'tn.jpg' in file_link:   #filters out the duplicated images
                totalimages = totalimages + 1   #Total image
                print(json.dumps([url + file_link]))
    print("Total number of images found:" ,totalimages)
