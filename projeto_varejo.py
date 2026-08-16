import pandas as pd
#import numpy as np

# Carregar o arquivo CSV 
df = pd.read_csv("Base Varejo.csv", sep=";")

print("\n==================================================================================================================")
print("DADOS ORIGINAIS:")
print(df)  


# Remover linhas duplicadas 
df = df.drop_duplicates() 

# Remover colunas inválidas 
df = df.dropna(axis=1, how="all")

# Verificar valores vazios 
print("\n==================================================================================================================")
print("\nQUANTIDADE DE VALORES VAZIOS POR COLUNA:") 
print(df.isna().sum())
print('\n')

# Correção de valores inválidos na coluna 'DATA'
datas_teste = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
print('Datas inválidas:', datas_teste.isna().sum())

# Alteração de valores inválidos em PR_CAT p/ 'SEM CATEGORIA'
df['PR_CAT'] = df['PR_CAT'].replace('#N/D', 'SEM CATEGORIA')
print(df['PR_CAT'].value_counts(dropna=False))


# Salvar os dados tratados em um novo arquivo CSV
df.to_csv("Base Varejo Tratada.csv", sep=";", index=False) 
print("\n==================================================================================================================")
print("\nDADOS TRATADOS:")
print(df)
