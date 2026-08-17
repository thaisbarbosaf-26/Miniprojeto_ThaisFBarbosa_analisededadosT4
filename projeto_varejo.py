import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o arquivo CSV 
df = pd.read_csv("Base Varejo.csv", sep=";")

print("\n============================================================================================")
print("DADOS ORIGINAIS:")
print(df)  


# Remover linhas duplicadas 
df = df.drop_duplicates() 

# Remover colunas inválidas 
df = df.dropna(axis=1, how="all")

# Verificar valores vazios 
print("\n============================================================================================")
print("\nQUANTIDADE DE VALORES VAZIOS POR COLUNA:\n") 
print(df.isna().sum())
print('\n')

# Correção de valores inválidos na coluna 'DATA'
datas_teste = pd.to_datetime(df['DATA'], format='%d/%m/%Y', errors='coerce')
print('Datas inválidas:', datas_teste.isna().sum())

# Alteração de valores inválidos em PR_CAT e PR_NOME p/ "SEM CATEGORIA.p/ 'SEM CATEGORIA'
def corrigir_categoria(categoria):
    if categoria == '#N/D':
        return 'SEM CATEGORIA'
    else:
        return categoria

print("\nQUANTIDADE DE PRODUTOS POR CATEGORIA:\n")
df['PR_CAT'] = df['PR_CAT'].apply(corrigir_categoria)
df['PR_NOME'] = df['PR_NOME'].apply(corrigir_categoria)


print(df['PR_CAT'].value_counts(dropna=False))

print("\nQUANTIDADE DE PRODUTOS POR NOME:\n")
print(df['PR_NOME'].value_counts(dropna=False))

# Comandos para obter os resultados de estatistica da coluna CL_FLH (n° de filhos)
print("\n\nESTATISTICA DA COLUNA CL_FHL (NÚMERO DE FILHOS)\n")

filhos_por_cliente = df.groupby("CL_ID")["CL_FHL"].nunique()

print("\nClientes com mais de um valor de CL_FHL:")
print(filhos_por_cliente[filhos_por_cliente > 1])

clientes = df[["CL_ID", "CL_FHL"]].drop_duplicates("CL_ID")

print("\nQuantidade de clientes:", len(clientes))
print(clientes.head())

print("\nQUANTIDADE DE CLIENTES POR NÚMERO DE FILHOS:")
print(clientes["CL_FHL"].value_counts().sort_index())

filhos = pd.to_numeric(clientes["CL_FHL"], errors="coerce")

estatisticas_filhos = pd.Series(
    {
        "contagem": filhos.count(),
        "média": filhos.mean(),
        "mediana": filhos.median(),
        "desvio padrão": filhos.std(),
        "moda": filhos.mode().iloc[0],
        "mínimo": filhos.min(),
        "1º quartil": filhos.quantile(0.25),
        "2º quartil": filhos.quantile(0.50),
        "3º quartil": filhos.quantile(0.75),
        "máximo": filhos.max(),
    }
)

print("\nESTATÍSTICAS DE NÚMERO DE FILHOS POR CLIENTE:")
print(estatisticas_filhos.round(2))



# Construindo gráfico p/ avaliar a quantidade de produtos por categoria
sns.countplot(data=df, y="PR_CAT", color="purple")
plt.title("Quantidade de Produtos por Categoria")
plt.ylabel("Categoria")
plt.yticks(rotation=25)
plt.xlabel("Quantidade")
plt.xticks(rotation=25)
plt.show()



# Salvar os dados tratados em um novo arquivo CSV
df.to_csv("Base Varejo Tratada.csv", sep=";", index=False) 
print("\n============================================================================================")
print("\nDADOS TRATADOS:")
print(df)
