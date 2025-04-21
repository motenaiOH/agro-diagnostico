import os
import json
from app.relatorio import gerar_relatorio

def test_gerar_relatorio(tmp_path):
    entrada = {
        "velocidade_kmh": 6.0,
        "rotacao_extrator": 1000,
        "umidade": 50,
        "temperatura": 25,
        "produtividade_esperada_t_ha": 85.0
    }
    resultado = {
        "perdas_estimadas": 3,
        "status": "ALERTA",
        "sugestao": "Reduza a velocidade."
    }

    # Define diretório de saída temporário para o relatório
    output_dir = tmp_path / "relatorios"
    gerar_relatorio(entrada, resultado, diretorio=output_dir)

    arquivos = list(output_dir.glob("relatorio_*.json"))
    assert len(arquivos) == 1

    with open(arquivos[0], "r", encoding="utf-8") as f:
        conteudo = json.load(f)

    assert conteudo["entrada"] == entrada
    assert conteudo["resultado"] == resultado
