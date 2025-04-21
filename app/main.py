from diagnostico import analisar_perdas
from relatorio import gerar_relatorio
from db import salvar_diagnostico
import json
import os
import subprocess

# Gerenciamento do processo do dashboard
dashboard_proc = None

def entrada_dados():
    try:
        velocidade = float(input("Velocidade da colhedora (km/h): "))
        rotacao = int(input("Rotação do extrator primário (rpm): "))
        umidade = int(input("Umidade (%): "))
        temperatura = int(input("Temperatura (°C): "))
        produtividade = float(input("Produtividade esperada (t/ha): "))

        return {
            "velocidade_kmh": velocidade,
            "rotacao_extrator": rotacao,
            "umidade": umidade,
            "temperatura": temperatura,
            "produtividade_esperada_t_ha": produtividade
        }
    except ValueError:
        print("Entrada inválida! Tente novamente com valores numéricos.")
        return entrada_dados()

def alterar_configuracoes():
    caminho = "parametros_diagnostico.json"
    if not os.path.exists(caminho):
        print("Arquivo de configuração não encontrado.")
        return

    with open(caminho, "r", encoding="utf-8") as f:
        config = json.load(f)

    print("\nConfigurações atuais:")
    for chave, valor in config.items():
        print(f"{chave}: {valor}")

    for chave in config:
        try:
            novo_valor = input(f"Novo valor para '{chave}' (pressione Enter para manter): ")
            if novo_valor.strip():
                config[chave] = type(config[chave])(novo_valor)
        except ValueError:
            print("Valor inválido, mantendo configuração anterior.")

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)

    print("\nConfigurações atualizadas com sucesso!\n")

def abrir_dashboard():
    global dashboard_proc
    print("Abrindo dashboard interativo em seu navegador...")
    dashboard_proc = subprocess.Popen(
        ["streamlit", "run", "../dashboard/dashboard.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )

def menu():
    global dashboard_proc
    while True:
        print("\n=== Sistema de Diagnóstico de Colheita ===")
        print("1) Alterar configurações")
        print("2) Executar novo diagnóstico")
        print("3) Encerrar aplicação")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            alterar_configuracoes()
        elif opcao == "2":
            dados = entrada_dados()
            resultado = analisar_perdas(dados)
            salvar_diagnostico(dados, resultado)
            gerar_relatorio(dados, resultado)
        elif opcao == "3":
            print("Encerrando aplicação...")
            if dashboard_proc:
                dashboard_proc.terminate()
                print("Dashboard encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    abrir_dashboard()
    menu()