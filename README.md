Simple web scrapper that returns a dictionary with all pokemon cards prices of the selected sets.
The setArts dictionary represents the number of total art styles present in each set, has the pokemon company has recently started printing different number of set arts, this is needed to parse the tables, it is possible to do this dynamically and discard the array with a bit more work inside the html filtering.

Price source is https://www.ptcgoguide.com/gxexpokemon.html#unb , updating prices takes a lot of work so make sure to pay a visit to the website and support its creator (which is not me).

External packages that need to be imported are BeautifulSoup for html parsing and selenium to run the javascript that updates the tables on the webpage.

You can do so by running pip install BeautifulSoup and pip install selenium
 
Additionally, chromedriver needs to be in your computer as it is used by selenium, you can get it here https://chromedriver.chromium.org/ and point to its path in the code
