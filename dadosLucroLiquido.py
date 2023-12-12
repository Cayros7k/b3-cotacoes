import pandas as pd

# Seleciona o arquivo JSON (Selecionar de acordo com o local onde o arquivo se encontra)

dados_acao = pd.read_json('./BRUTO/UGPA3.json')

# Ajusta o valor (divide o valor por 1000)
# dadosVirgula=[
# "lucroLiquido"    
# ]

# for coluna in dadosVirgula:
#     dados_acao[coluna]=[i/1000 for i in dados_acao[coluna]]

# Função para formatar com separadores de milhar
# def formatar(valor):
#    return '{:,}'.format(valor)

# Adiciona a coluna 'codigoNegocio' no DataFrame
df = pd.DataFrame(dados_acao)
#df['lucroLiquido'] = df['lucroLiquido'].astype(int)
df['cod_negociacoes'] = ['UGPA3']*20

#df['year'] = pd.to_datetime(df['year'], format = '%Y') 
#df['year'] = df['year'].dt.strftime('%Y')

df['year'] = df.apply(lambda row: pd.Timestamp(f'{row["year"]}-{3*(row["quarter"]-1)+1}-01'), axis=1)
df['year'] = df['year'].dt.strftime('%d/%m/%Y')

# Define quais colunas serão mostradas
dr = df[['cod_negociacoes','year', 'quarter', 'lucroLiquido']]

print (dr)

#Salva o arquivo no formato csv
fileO = open('UGPA3_lucro.csv', "w")
fileO.write(dr.to_csv())
fileO.close