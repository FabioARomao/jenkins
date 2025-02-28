import os
import pandas as pd

# Caminhos dos arquivos processados
OUTPUT_DIR = "output"
PROCESSED_FILE = os.path.join(OUTPUT_DIR, "dados_processados.csv")


def test_arquivo_existe():
    """Verifica se o arquivo processado foi gerado corretamente"""
    assert os.path.exists(PROCESSED_FILE), "O arquivo processado não foi encontrado!"


def test_formato_do_arquivo():
    """Verifica se o arquivo está no formato CSV correto"""
    try:
        df = pd.read_csv(PROCESSED_FILE)
        assert not df.empty, "O arquivo processado está vazio!"
    except Exception as e:
        assert False, f"Erro ao abrir o CSV: {str(e)}"


def test_valores_dos_dados():
    """Verifica se os dados possuem valores esperados (exemplo: coluna 'status')"""
    df = pd.read_csv(PROCESSED_FILE)

    assert "status" in df.columns, "A coluna 'status' não foi encontrada no CSV!"
    
    valores_esperados = {"entregue", "enviado dispositivo indisponível", "restrição operadora"}
    valores_no_arquivo = set(df["status"].unique())

    assert valores_no_arquivo.issubset(valores_esperados), "Valores inesperados encontrados na coluna 'status'!"


if __name__ == "__main__":
    import pytest
    pytest.main()

