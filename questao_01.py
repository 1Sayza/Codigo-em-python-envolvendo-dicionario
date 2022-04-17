from time import sleep
import requests, os
from datetime import datetime, timedelta, time

arquivo_log = os.path.dirname(os.path.abspath(__file__)) + '\\log.txt'

#url = 'https://apitempo.inmet.gov.br/condicao/capitais/2022-03-02'

# Definindo a URL base
url_base = 'https://apitempo.inmet.gov.br/condicao/capitais/{0}'

# Definindo o ano base (substituir por um input - CUIDADO: exceções!!!!!)
ano = int(input("Digite o ano: "))

# Definindo a data inicial do período
data_inicial = str(ano) + '-01-01'
data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')

# Definindo a data final do período
data_final = str(ano) + '-12-31'
data_final = datetime.strptime(data_final, '%Y-%m-%d')

arquivo_output = open(arquivo_log, 'w', encoding='utf-8')

data = data_inicial
temp_min = {}
temp_max = {}
por_cidade = {}
c = []
while data <= data_final:
    # Definindo a URL de requisição
    url = url_base.format(data.strftime('%Y-%m-%d'))

    mes_atual = str(data)[5:7]

    # Efetuando a requisição     
    print('\nRequisitando dados do dia {0}'.format(data.strftime('%d-%m-%Y')))
    try:
        retorno_dados = requests.get(url).json()
        for a in range(len(retorno_dados)):
            nome_da_cidade = retorno_dados[a]['CAPITAL']
            temp_min = retorno_dados[a]['TMIN18'].replace('*','')
            temp_max = retorno_dados[a]['TMAX18'].replace('*','')
            por_cidade[nome_da_cidade] = {'Tmin': temp_min, 'Tmax': temp_max}
        c.append(por_cidade)    
    except:
        arquivo_output.write('Erro na data...{0}\n'.format(data.strftime('%d-%m-%Y')))
    else:
        arquivo_output.write('Dados Lidos...{0}\n'.format(data.strftime('%d-%m-%Y')))


    # Incrementando 1 dia na data
    data = data + timedelta(days=1)

    novo_mes = str(data)[5:7]

    if (mes_atual != novo_mes):
        mes_atual = novo_mes
        sleep(1)

#print(c)
#TODO: Item B

s = 0
j = 0
dados = 0
while s < (len(retorno_dados)):
    if (retorno_dados[s]['TMIN18'].replace('*','')) != '':
        dados = dados + float(retorno_dados[s]['TMIN18'].replace('*',''))
        j+=1
        s+=1
    else:
        s+=1
    
dados = dados/(j+1)

g = 0
h = 0
dadosmaximo = 0
while g < (len(retorno_dados)):
    if (retorno_dados[g]['TMAX18'].replace('*','')) != '':
        dadosmaximo = dadosmaximo + float(retorno_dados[g]['TMAX18'].replace('*',''))
        h+=1
        g+=1
    else:
        g+=1

dadosmaximo = dadosmaximo / (h+1)

print(f'Média da Temperatura mínima das cidades do ano de {ano}: {dados}')
print(f'Média da Temperatura máxima das cidades do ano de {ano}: {dadosmaximo}')

arquivo_output.close()