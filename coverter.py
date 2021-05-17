import pandas as pd
import json

# Exemplo  de um dicionário que virará um arquivo .json
dict = {"students": [{"name": "Alan", "lastname": "Silva", "exam1": 50, "exam2": 80, "exam3": 91},
    {"name": "Paula", "lastname": "Souza", "exam1": 95, "exam2": 98, "exam3": 99}]
    }

# Criar uma função que escreve um arquivo .json
def escrever_json(dados):
    with open('meu_arquivo.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
# Criar uma função que lê o arquivo .json
def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)

# Chamar a função escreve_jason()
#escrever_json(dict)

# Ler o arquivo .json e jogar na variável 'data'
data = ler_json('meu_arquivo.json')

# Pegar as chaves de dentro de 'students' e jogar na variável 'keys'
keys = data['students'][0].keys()
print(keys)
# Pegar os de dentro de 'students' e jogar na variável 'values'
values = data['students'][0].values()
print(values)
# Finalmente, criar a tabela que você queria em um DataFrame
df = pd.DataFrame(values, index=keys, columns=['Valores'])
df
print(df)