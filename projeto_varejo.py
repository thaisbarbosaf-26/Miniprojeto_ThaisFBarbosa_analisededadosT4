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

# Salvar os dados tratados em um novo arquivo CSV
df.to_csv("Base Varejo Tratada.csv", sep=";", index=False) 
print("\n==================================================================================================================")
print("\nDADOS TRATADOS:")
print(df)
