from app.diagnostico import analisar_perdas

def test_diagnostico_critico():
    entrada = {
        "velocidade_kmh": 10.0,
        "rotacao_extrator": 1400,
        "umidade": 80,
        "temperatura": 35,
        "produtividade_esperada_t_ha": 85.0
    }
    resultado = analisar_perdas(entrada)
    assert resultado["status"] == "CRÍTICO"
    assert resultado["perdas_estimadas"] == 14

def test_diagnostico_ok():
    entrada = {
        "velocidade_kmh": 6.0,
        "rotacao_extrator": 1000,
        "umidade": 50,
        "temperatura": 25,
        "produtividade_esperada_t_ha": 85.0
    }
    resultado = analisar_perdas(entrada)
    assert resultado["status"] == "OK"
    assert resultado["perdas_estimadas"] == 0
