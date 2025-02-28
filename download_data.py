import pandas as pd
import os

# Diretório de saída
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Criando dados fictícios
dados_brutos = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "mensagem": [
        "Olá! Gostaria de falar com um consultor.",
        "Quero saber mais sobre o produto.",
        "Meu pedido não chegou.",
        "Preciso de suporte técnico.",
        "Posso pagar parcelado?"
    ],
    "codemp": [1633, 1685, 1633, 1602, 1685],
    "data_envio": ["2024-05-01", "2024-06-15", "2024-07-03", "2024-07-10", "2024-08-01"]
})

# Salvar CSV bruto
RAW_FILE = os.path.join(OUTPUT_DIR, "dados_brutos.csv")
dados_brutos.to_csv(RAW_FILE, index=False)

print(f"✅ Dados brutos salvos em {RAW_FILE}")
