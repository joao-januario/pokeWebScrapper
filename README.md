Simple web scrapper that returns a dictionary with all pokemon cards prices, f the selected sets inside the first array.

Price source is https://www.ptcgoguide.com/gxexpokemon.html#unb , updating prices takes a lot of work so make sure to pay a visit to the website and support its creator (which is not me).

External packages that need to be imported are BeautifulSoup for html parsing and selenium to run the javascript that updates the tables on the webpage.

You can do so by running pip install BeautifulSoup and pip install selenium
