import pandas as pd


dados_acao = pd.read_excel('./patrimonioLiquido/PATRIMONIO_LIQUIDO.xlsx')

#Ajusta o valor (divide o valor por 1000)
# dadosVirgula=[
# "Patrimônio Líquido"    
# ]

# for coluna in dadosVirgula:
#     dados_acao[coluna]=[i*100 for i in dados_acao[coluna]]


# Adiciona a coluna 'codigoNegocio' no DataFrame

df = pd.DataFrame(dados_acao)

new_names = {
    'Patrimônio Líquido': 'patrimonioLiquido',
    'TRIMESTRE': 'data'
    
}
df = df.rename(columns=new_names)

df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
df['quarter'] = df['data'].dt.quarter
pd.options.display.float_format = '{:,.3f}'.format
df['patrimonioLiquido'] = df['patrimonioLiquido'].apply(lambda x: '{:.3f}'.format(x).replace('.', '').replace(',', ''))

dr = df[['data','quarter', 'patrimonioLiquido', 'cod_negociacao']]

print (dr)

#Salva o arquivo no formato csv
fileO = open('patrimonioLiquido.csv', "w")
fileO.write(dr.to_csv())
fileO.close