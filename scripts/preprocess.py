import pandas as pd
import os
import random

INPUT_FILE = "output/dados_brutos.csv"
OUTPUT_FILE = "output/dados_processados.csv"

# Lógica de status para cada empresa
STATUS_RULES = {
    1633: {12: 60, 30: 10, 73: 5},  # Empresa 1633 (conversões para status)
    1602: {12: 70, 30: 1, 73: 1},  # Empresa 1602
    1685: {12: 90, 30: 5, 73: 5}   # Empresa 1685
}

# Carregar os dados brutos
df = pd.read_csv(INPUT_FILE)

# Função para determinar o status baseado no codemp
def determinar_status(codemp):
    if codemp in STATUS_RULES:
        escolhas = []
        for status, prob in STATUS_RULES[codemp].items():
            escolhas.extend([status] * prob)
        return random.choice(escolhas)
    return 12  # Default: entregue

# Aplicar transformação
df["status"] = df["codemp"].apply(determinar_status)

# Salvar arquivo processado
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Dados processados e salvos em {OUTPUT_FILE}")

