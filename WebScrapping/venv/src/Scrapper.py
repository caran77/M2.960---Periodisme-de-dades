import time

from bs4 import BeautifulSoup

import utils, FileOperations, HTMLGetters, dataCleaningUtils

fileName = 'data/productData.csv'
sleepTime = 1
retries = 3
parser = 'html.parser'

def scraping():
    FileOperations.createFile(fileName)
    http = FileOperations.download(urlPage(), retries)
    print(urlPage())
    time.sleep(sleepTime)
    if not (http is None):
        print(http)
        soup = BeautifulSoup(http, parser)
        finaliza = FileOperations.eof(soup)
        all_a = soup.find_all('div', class_="destContainer")
        #treatDiv(all_a, searchConcept, 0)

def urlPage():
    return "https://www.idealista.com/inmueble/87748015/"

def treatDiv(all_a, searchConcept, page):
    for a in all_a:
        code = HTMLGetters.getCode(a)
        imgURL = HTMLGetters.getImageURL(a)
        imgAlt = HTMLGetters.getImageAlt(a)
        price = HTMLGetters.getPrice(a)
        puntuation = HTMLGetters.getPuntuation(a)
        description = HTMLGetters.getDescription(a)
        stock = HTMLGetters.getStock(a)
        imgName = None
        if (imgURL != None):
            imgName = utils.getFileName(imgURL)
            FileOperations.downloadImg(imgURL, 'img', imgName)
        try:
            if (dataCleaningUtils.isValidRow(price) == 0):
                FileOperations.createRow(searchConcept, page, imgName, fileName, code, price, description, imgURL, puntuation, imgAlt, stock)
        except(Exception):
            if (code == None):
                print("Unknown error ")
            else:
                print("Error " + code)
