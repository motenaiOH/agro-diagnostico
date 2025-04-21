import json
import os
from datetime import datetime

def gerar_relatorio(dados, resultado, diretorio="../relatorios"):
    os.makedirs(diretorio, exist_ok=True)
    nome_arquivo = f"{diretorio}/relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        json.dump({"entrada": dados, "resultado": resultado}, f, indent=4, ensure_ascii=False)
    print(f"Relatório gerado em: {nome_arquivo}")