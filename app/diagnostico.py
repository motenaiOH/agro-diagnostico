import json
import os

# Caminho seguro e relativo ao próprio arquivo
BASE_DIR = os.path.dirname(__file__)
PARAMS_PATH = os.path.join(BASE_DIR, "parametros_diagnostico.json")

with open(PARAMS_PATH, "r", encoding="utf-8") as f:
    PARAMS = json.load(f)

def analisar_perdas(dados):
    perdas = 0
    if dados["velocidade_kmh"] > PARAMS["velocidade_kmh"]:
        perdas += PARAMS["peso_velocidade"]
    if dados["rotacao_extrator"] > PARAMS["rotacao_extrator"]:
        perdas += PARAMS["peso_rotacao"]
    if dados["umidade"] > PARAMS["umidade"]:
        perdas += PARAMS["peso_umidade"]
    if dados["temperatura"] > PARAMS["temperatura"]:
        perdas += PARAMS["peso_temperatura"]

    perdas = min(perdas, 15)
    status = "OK" if perdas < 5 else "ALERTA" if perdas < 10 else "CRÍTICO"
    sugestao = PARAMS["sugestao"]

    return {
        "perdas_estimadas": perdas,
        "status": status,
        "sugestao": sugestao
    }
