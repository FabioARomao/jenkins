import pandas as pd
import os

INPUT_FILE = "output/dados_processados.csv"
FINAL_FILE = "output/dados_final.csv"

# Carregar dados processados
df = pd.read_csv(INPUT_FILE)

# Simulação: renomear colunas e salvar o resultado final
df_final = df.rename(columns={"mensagem": "conteudo_mensagem", "data_envio": "data"})

# Salvar CSV final
df_final.to_csv(FINAL_FILE, index=False)

print(f"✅ Dados finais salvos em {FINAL_FILE}")
