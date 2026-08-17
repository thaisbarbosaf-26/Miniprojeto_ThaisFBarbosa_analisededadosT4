# Projeto - Analisando base de dados - Varejo  
## Mini projeto avaliativo
***
### 1. **Realizando Limpeza e Transformação de dados**    
   
A partir do envio do arquivo citado acima, na primeira análise foram identificados:        

   
1.1 Colunas com valores inválidos e linhas duplicadas: 
-|colunas|linhas
---|---|---
antes|830000|14
depois|733447|10 
    
1.2 Conversão p/ valores válidos: 
    
  1.2.1 Produtos sem identificação ou com informação inválida na coluna _categoria_ e _nome_ foi atribuído ao item *sem categoria*, pois são parte de informações relevantes p/ análise geral.  
  1.2.2 Na coluna .data foi feita a conversão do formato p/ unificar e tornar .possível pesquisas futuras. 

### 2. **Execução**   

   Após a limpeza dos dados, foram inseridas informações gerais como: quantidade de produtos por categoria e também pelo nome de cada um deles. Em seguida uma análise mais voltada p/ comparação entre clientes, gênero e número de filhos. E para finalizar, uma avaliação do produto que é mais consumido e o estado civil de cada cliente consumidor deste.

### 3. **Conclusão** 

1. Entre as categorias existentes, o item *alimentos* é o mais consumido. **OBS:* gráfico inserido no vs code;
2. Os três produtos mais consumidos, são desta mesma categoria: presunto cozido, sardinha e banana;
3. De um total de mil clientes, os que mais consomem não possuem filhos;
<img width="420" height="159" alt="image" src="https://github.com/user-attachments/assets/962dd2eb-3293-4e3c-9aa2-05e9fc48e903" />

4. Entre os que não possuem filhos, o gênero feminino, é o que se destaca em relação ao gênero masculino por comprar mais. Em contrapartida, este mesmo gênero com 4 filhos (n° máximo de filhos ), foi o que menos consumiu, levando em conta o período que consta na tabela disponibilizada;   
<img width="480" height="283" alt="image" src="https://github.com/user-attachments/assets/d060c4af-3682-401f-8e50-acb66a786108" />

   
5. Em relação ao estado civil, quem menos consumiu foram os viúvos e as maiores vendas foram para os separados;

   
<img width="368" height="200" alt="image" src="https://github.com/user-attachments/assets/be809d77-5c27-4ba2-9dec-b585ef9f9ad3" /> 

Considerando: 
 
CL_EC|Estado Civil
---|---
1|Casado(a) ou União estável
2|Divorciado(a)
3|Separado(a)
4|Solteiro(a)
5|Viúvo(a)  
  
*** 
 

  
_Base Dados_Varejo_     
 
**Fonte:**  
Site: https://www.kaggle.com/datasets/namespaiva/base-varejo?resource=download&select=Projeto+III+-+Anlise+Exploratria+de+Dados+Utilizando+o+Python+ou+RStudio.pd
