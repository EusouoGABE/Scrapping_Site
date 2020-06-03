import urllib.request
from bs4 import BeautifulSoup

vetorTitulo    = []
vetorLink      = []
vetorCategoria = []

def scrapMega(a):
    if (a != None):
        page = a
        pagina = urllib.request.urlopen(a)
        soup = BeautifulSoup(pagina, 'html5lib')

        all_links = soup.find_all('div', attrs={'class': 'home-vertical-news-data'})
        for titulo in all_links:
            link = titulo.find('a', attrs={'class': 'home-vertical-news-title-wrapper'})
            vetorLink.append(link.get('href'))
            categoria = titulo.find('span', attrs={'class': 'home-vertical-news-info-item'})
            categoria1 = categoria.find('a')
            vetorCategoria.append(categoria1.find(text=True).strip())

        titulo_div = soup.find_all('h2', attrs={'class': 'home-vertical-news-title'})
        for titulo1 in titulo_div:
            vetorTitulo.append(titulo1.find(text=True))