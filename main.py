import re

import requests
from bs4 import BeautifulSoup as bs
from util.StringUtil import remove_acentos, remove_varios_espacos

class extrator():

    def acesso(self):
        url = 'https://www.fundsexplorer.com.br/ranking'
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ 97.0.4692.99 Safari/537.36"}
        site = requests.get(url, headers=headers)
        soup_extrator = bs(site.content, 'html.parser')

        self.informacao(soup_extrator)

    def informacao(self, soup_extrator):
        section = soup_extrator.find('section', {'id':'ranking'})
        tabela = section.find('table', {'id':'table-ranking'})
        cabecalho = tabela.find('thead').find('tr')
        conteudo = tabela.find('tbody').find_all('tr')
        localizar = soup_extrator.find('span', text=re.compile('.*Carteira Recomendada.*'))
        print(localizar)

if __name__ == "__main__":
    ex = extrator()
    ex.acesso()