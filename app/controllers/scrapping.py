from bs4 import BeautifulSoup
import urllib.request
tituloVet = []  # Vetores que serão armazenados os titulos
linkVet = []  # Vetores que serão armazenados os titulos
dataVet = []  # Vetores que serão armazenados as datas

def scrap(a):

    if (a != None):
        site = a #site utilizado
        pag  = urllib.request.urlopen('https://www.tecmundo.com.br/novidades/') #recebe o site para ser utilizado no soup
        soup = BeautifulSoup(pag, 'html5lib') #recebendo o html

        all_links = soup.find_all('h3', attrs={'class': 'tec--card__title'}) #procurando o titulo e o link da pagina da noticia
        for titulo in all_links:
            link = titulo.find('a', attrs={'class': 'tec--card__title__link'})#seleciona a tag <a> que se encontrava dentro do h3
            linkVet.append(link.get('href')) #.get('href') para selecionar somente o link
            tituloVet.append(titulo.find(text=True).strip(" "))  # Strip serve como TRIM, para tirar espaços
            # listando todas as noticias

        data_div = soup.find_all('div', attrs={'class': 'tec--timestamp__item z--font-semibold'}) #procurando a data da noticia
        for data in data_div:
            dataVet.append(data.find(text=True))
            # listando todas as datas



