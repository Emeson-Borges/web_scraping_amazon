import requests
from bs4 import BeautifulSoup
import csv
import datetime

# URL da página de resultados da pesquisa
url = 'https://www.amazon.com.br/s?k=livro+programa%C3%A7%C3%A3o+python&i=stripbooks&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&qid=1617694513&ref=sr_pg_1'

# Obtém a data atual
date_now = datetime.datetime.now().strftime('%d/%m/%Y')

# Obtém o conteúdo HTML da página
response = requests.get(url)
html_content = response.content

# Analisa o conteúdo HTML usando o BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Procura por todos os itens da lista de resultados de pesquisa
items = soup.find_all('div', {'data-component-type': 's-search-result'})

# Cria um arquivo CSV para armazenar os dados
filename = 'livros_python.csv'
with open(filename, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Escreve o cabeçalho do arquivo CSV
    writer.writerow(['Nome', 'Preço', 'Data de verificação'])

    # Loop pelos itens da lista de resultados de pesquisa
    for item in items:
        # Obtém o nome do livro
        name_tag = item.find('span', {'class': 'a-size-medium a-color-base a-text-normal'})
        if name_tag:
            name = name_tag.text.strip()
        else:
            name = 'Não Encontrado'

        # Obtém o preço do livro
        price_tag = item.find('span', {'class': 'a-offscreen'})
        if price_tag:
            # substitui vírgula por ponto para o formato correto do CSV
            price = price_tag.text.strip().replace(',', '.')
        else:
            price = 'N/A'

        # Escreve os dados no arquivo CSV
        writer.writerow([name, price, date_now])

print('Nome:', name)
print('Preço:', price)
print('Data de verificação:', date_now)
