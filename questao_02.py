
# Nome Comum em Português / Nome Oficial em
# Português / Moeda / Capital / Coordenadas Geográficas da Capital / Região /
# Sub-Região / Idiomas / Área / Bandeira (guardar a URL do formato em SVG) /
#Brasão de Armas (guardar a URL do formato em SVG);
# ------------------------------------------------------------------------------------------------

import os
import requests
url = 'https://restcountries.com/v3.1/all'

dados_brutos = requests.get(url).json() 
     
def dados(lista_valores):
    dicionario = dict()

    for linha in range (len(lista_valores)):
        try:
            nome = (lista_valores[linha]['translations']['por']['common'])
            nome_oficial = (lista_valores[linha]['translations']['por']['official'])
            moeda = (lista_valores[linha]['currencies'])
            capital = (lista_valores[linha]['capital'])
            coordenadas =(lista_valores[linha]['capitalInfo']['latlng'])
            regiao = (lista_valores[linha]['region'])
            subregiao = (lista_valores[linha]['subregion'])
            idiomas = (lista_valores[linha]['languages'])
            area = (lista_valores[linha]['area'])
            bandeira = (lista_valores[linha]['flags']['svg'])
            brasao = (lista_valores[linha]['coatOfArms']['svg'])
        
            dicionario[nome] = { "Nome Comum em português": nome, 
                                'Nome Oficial em Português': nome_oficial,
                                'Moeda': moeda, 'Capital': capital, 
                                'Coordenadas Geográficas da Capital': coordenadas, 
                                'Região': regiao, 'Sub-Região': subregiao, 
                                'Idiomas': idiomas, 
                                'Área': area,
                                'Bandeira': bandeira,
                                'Brasão de Armas': brasao}
        except:
            continue
    
    
    return dicionario

dados_retorno = dados(dados_brutos)
print('Dados tratados!')
print(dados_retorno)
      
# Obtendo o diretório (caminho) do arquivo .py
diretorio = os.path.dirname(os.path.realpath(__file__))

# Montando o nome do arquivo
nome_arquivo_output = diretorio + '\\valores_tratados.json'

arquivo_output = open(nome_arquivo_output, "w" , encoding = "utf-8")
arquivo_output.write(str(dados_retorno))
arquivo_output.close()
        






    


    


    