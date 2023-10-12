import pandas as pd

# Seleciona o arquivo JSON (Selecionar de acordo com o local onde o arquivo se encontra)
dados_acao = pd.read_json('./receitaLiquida_bruto/getrevenueSLCE3.json')

# Ajusta o valor (divide o valor por 1000)
dadosVirgula=[
"receitaLiquida"    
]

for coluna in dadosVirgula:
    dados_acao[coluna]=[i/1000 for i in dados_acao[coluna]]

# Função para formatar com separadores de milhar
# def formatar(valor):
#    return '{:,}'.format(valor)

# Adiciona a coluna 'codigoNegocio' no DataFrame
df = pd.DataFrame(dados_acao)
df['codigoNegocio'] = ['SLCE3']*20

#df['year'] = pd.to_datetime(df['year'], format = '%Y') 
#df['year'] = df['year'].dt.strftime('%Y')

df['year'] = df.apply(lambda row: pd.Timestamp(f'{row["year"]}-{3*(row["quarter"]-1)+1}-01'), axis=1)
df['year'] = df['year'].dt.strftime('%d/%m/%Y')

# Define quais colunas serão mostradas
dr = df[['codigoNegocio','year', 'quarter', 'receitaLiquida']]

print (dr)

# Salva o arquivo no formato csv
fileO = open('SLCE3_RECEITA.csv', "w")
fileO.write(dr.to_csv())
fileO.close