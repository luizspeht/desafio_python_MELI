import requests
import random
import time
import pandas as pd

# Habilita o modo simulação
MODO_SIMULACAO = True

# URL base da API
API_BASE_URL = "https://api.mercadolibre.com"

# Funções

def buscar_lista_de_ids():
    if MODO_SIMULACAO:
    # Se o modo simulação estiver habilitado vamos gerar uma lista de ids de 1 a 100
        return list(range(1, 101))
    else:
    # Se o modo simulação estiver desabilitado vamos extrair da API os ids
        url = f"{API_BASE_URL}/compliance_alerts?status=open&limit=100"
        resp = requests.get(url)
        if resp.status_code == 200: # O código 200 indica que a requisição foi bem-sucedida
            dados = resp.json()  # Converte a resposta JSON para um objeto Python, no caso uma lista de dicionários
            # Criamos uma lista vazia para receber os valores dos ids
            ids = []
            for item in dados:
                ids.append(item["id"])
            return ids
        else:
            print(f"Erro ao buscar IDs: {resp.status_code}")
            return []

def buscar_detalhes_por_id(id_alerta):
    if MODO_SIMULACAO:
    # Se o modo simulação estiver habilitado, vamos gerar os dados aleatoriamente utilizando a biblioteca random
        tipos = ["Alertas de Conformidade", "Incidentes Fiscais"]
        responsaveis = ["João", "Maria", "José"]
        impactos = ["Baixo", "Médio", "Alto"]

        return {
            "id": id_alerta,
            "tipo_alerta": random.choice(tipos),
            "status": "open",
            "responsavel": random.choice(responsaveis),
            "data_criacao": "2025-07-09",
            "data_resolucao": "N/A",
            "impacto": random.choice(impactos),
        }
    else:
    # Se o modo simulação estiver desabilitado, vamos consultar a API para cada id da nossa lista
        url = f"{API_BASE_URL}/compliance_alerts/{id_alerta}"
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"Erro ao buscar detalhes do ID {id_alerta}: {resp.status_code}")
            return None

# Código Principal

print("=== INICIANDO COLETA DE ALERTAS ===")

# Obtém a lista de IDs
ids = buscar_lista_de_ids()

# Lista para armazenar o dicionário de cada id
dados = []

# Percorre cada ID da lista
for id_atual in ids:
    detalhe = buscar_detalhes_por_id(id_atual)
    if detalhe:
        dados.append(detalhe)
        print(f"Processado ID {id_atual}")
    time.sleep(0.01) # Adiciona um intervalo entre cada uma das requisições

# Converte uma lista em dataframe (df)
df = pd.DataFrame(dados)

# Salva o DataFrame em um arquivo CSV
df.to_csv("alertas.csv", index=False, encoding="utf-8")

print(f"✅ {len(dados)} alertas salvos em alertas.csv")