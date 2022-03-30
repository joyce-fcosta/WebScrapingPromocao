import urllib.request
from bs4 import BeautifulSoup
import re

''' pagina html que queremos '''
page = "https://www.pizzariaatlantico.com.br/"

''' acessa e abre a pg html '''
o_pg = urllib.request.urlopen(page)

''' pega a estrutura html bagunçado '''
soup = BeautifulSoup(o_pg, 'html.parser')

''' alinha as estruturas do html '''
soup.prettify()


''' procurar a palavra 'promocoes' na ta 'section, retorna uma lista sendo cada div um elemento' '''
tag = soup.find("section", "promocoes")


''' procura nas divs a palavra promocao com intuito de encontrar cada prato em promoção '''
''' items = tag.find_all('div',"promocao").split(',')
print(items) '''

print("\n\n\n")
''' procurar tags de titulos. usa 're' para encontra-las pois começam com 'h' e seu conteudo'''

dados = []
for proc_tag in tag.find_all(re.compile("^h")):
  i_tag = str(proc_tag.name)
  texto = str(proc_tag.text)
  ''' texto.strip() '''
  dados.append(texto)
  
print(dados)


atualizacao_dados=[]
def tirar_formatacao (lista, NovaLista):
  for ver in lista:
    salva = ver.lstrip() #tirou os caracters de tabulação
    NovaLista.append(salva.strip()) #tirar espaço 

tirar_formatacao(dados, atualizacao_dados)
print(atualizacao_dados)
print("\n")


#Eliminação de itens repetidos
def Elimina_Items_Repetidos(ListaAtualizada):
  for i in ListaAtualizada:
    print(i)
    perg = input("Deseja remover? ")
    if perg == 's':
      ListaAtualizada.remove(i)

Elimina_Items_Repetidos(atualizacao_dados)
print(atualizacao_dados)


titulo_arquivo = "PROMOÇÕES do " + soup.find("title").get_text().strip() + "\n"

print(titulo_arquivo)


arquivo_promocoes = open('promocoes.txt','w')

arquivo_promocoes.write(titulo_arquivo)

atualizacao_dados_2 = atualizacao_dados

print(atualizacao_dados_2)
print("PROMOÇÕES do",soup.find("title").get_text())
for x in atualizacao_dados_2:
  arquivo_promocoes.write(x)
  arquivo_promocoes.write("\n")
  print(x)

arquivo_promocoes.close()
