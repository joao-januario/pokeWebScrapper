import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

set = ['Unified Minds','Unbroken Bonds','Team Up','Lost Thunder','Dragons Majesty','Celestial Storm','Forbidden Light','Ultra Prism','Crimson Invasion','Shining Legends','Burning Shadows','Guardians Rising','Sun Moon']
setArts = {'Unified Minds':4,'Unbroken Bonds':4,'Team Up':4,'Lost Thunder':3,'Dragons Majesty':3,'Celestial Storm':3,'Forbidden Light':3,'Ultra Prism':3,'Crimson Invasion':3,'Shining Legends':3,'Burning Shadows':3,'Guardians Rising':3,'Sun Moon':3}
tableStrings={}

chromeDrivePath = 'insert path here'
url = "https://www.ptcgoguide.com/gxexpokemon.html#unb"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=chromeDrivePath,options=options)
driver.get(url)
time.sleep(3)
page = driver.page_source
driver.quit()
soup = BeautifulSoup(page, 'html.parser')
soup = soup.find(id='set_table')
soup = soup.findAll('table')
i = 0
for table in soup:
    if (i<len(set)):
        row = table.find('tbody')
        tableString = ""
        artNumber = setArts[set[i]]
        for column in row:
            column.findAll('th')
            newCard = True
            for cell in column:
                if (cell.text == "Card Name" or cell.text == "RA" or cell.text == "FA" or cell.text == "AA" or cell.text == "SR"):
                    pass
                else:
                    if (artNumber > 0):
                        tableString = tableString + " " + cell.text
                        artNumber -= 1
                    else:
                        tableString = tableString + " " + cell.text + " ||||| "
                        artNumber = setArts[set[i]]
        tableStrings[set[i]] = tableString
    i +=1

print(tableStrings)