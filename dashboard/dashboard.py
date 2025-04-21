import streamlit as st
import os
import json
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="Dashboard de Diagnósticos", layout="wide")
st.title("📊 Histórico de Diagnósticos de Colheita de Cana")

# === Verificação de atualização automática via modificação de arquivos ===
pasta = "../relatorios"
if "_last_check" not in st.session_state:
    st.session_state._last_check = 0

if os.path.isdir(pasta):
    modificacoes = [os.path.getmtime(os.path.join(pasta, f)) for f in os.listdir(pasta) if f.endswith(".json")]
    ultima_modificacao = max(modificacoes) if modificacoes else 0

    if ultima_modificacao > st.session_state._last_check:
        st.session_state._last_check = ultima_modificacao
        st.rerun()

else:
    st.warning("Nenhum diretório de relatórios encontrado.")
    st.stop()

arquivos = sorted(os.listdir(pasta), reverse=True)
dados_list = []

for nome in arquivos:
    if not nome.endswith(".json"):
        continue
    with open(os.path.join(pasta, nome), "r", encoding="utf-8") as f:
        dados = json.load(f)
        entrada = dados.get("entrada", {})
        resultado = dados.get("resultado", {})
        entrada.update(resultado)
        entrada["arquivo"] = nome
        dados_list.append(entrada)

if not dados_list:
    st.info("Nenhum dado disponível para visualização.")
    st.stop()

# === Continuação do dashboard ===
df = pd.DataFrame(dados_list)

st.sidebar.header("🔍 Filtros")
status_options = df["status"].unique().tolist()
status_filter = st.sidebar.multiselect("Status", options=status_options, default=status_options)

perda_min, perda_max = int(df["perdas_estimadas"].min()), int(df["perdas_estimadas"].max())
if perda_min < perda_max:
    faixa_perda = st.sidebar.slider("Faixa de Perdas (%)", min_value=perda_min, max_value=perda_max, value=(perda_min, perda_max))
else:
    faixa_perda = (perda_min, perda_max)

temp_min, temp_max = int(df["temperatura"].min()), int(df["temperatura"].max())
if temp_min < temp_max:
    faixa_temp = st.sidebar.slider("Faixa de Temperatura (°C)", min_value=temp_min, max_value=temp_max, value=(temp_min, temp_max))
else:
    faixa_temp = (temp_min, temp_max)

df_filtrado = df[(df["status"].isin(status_filter)) &
                 (df["perdas_estimadas"] >= faixa_perda[0]) &
                 (df["perdas_estimadas"] <= faixa_perda[1]) &
                 (df["temperatura"] >= faixa_temp[0]) &
                 (df["temperatura"] <= faixa_temp[1])]

st.subheader("📁 Tabela Consolidada de Diagnósticos")
st.dataframe(df_filtrado, use_container_width=True)

st.subheader("📊 Distribuição de Perdas Estimadas")
fig_hist = px.histogram(df_filtrado, x="perdas_estimadas", nbins=10, color_discrete_sequence=["#1f77b4"])
fig_hist.update_layout(title="Distribuição das Perdas Estimadas", xaxis_title="Perdas (%)", yaxis_title="Frequência")
st.plotly_chart(fig_hist, use_container_width=True)

st.subheader("📌 Classificação de Status")
status_df = df_filtrado["status"].value_counts().reset_index()
status_df.columns = ["Status", "Quantidade"]
fig_bar = px.bar(status_df, x="Status", y="Quantidade",
                 color="Status",
                 color_discrete_map={"OK": "green", "ALERTA": "orange", "CRÍTICO": "red"})
fig_bar.update_layout(title="Quantidade de Diagnósticos por Status")
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("📈 Perdas por Temperatura")
fig_scatter = px.scatter(df_filtrado, x="temperatura", y="perdas_estimadas", color="status",
                         title="Correlação entre Temperatura e Perdas",
                         labels={"temperatura": "Temperatura (°C)", "perdas_estimadas": "Perdas (%)"})
st.plotly_chart(fig_scatter, use_container_width=True)

st.subheader("📐 Estatísticas Resumidas")
col1, col2 = st.columns(2)
with col1:
    st.metric("Média de Perdas (%)", round(df_filtrado["perdas_estimadas"].mean(), 2))
    st.metric("Máxima Temperatura (°C)", df_filtrado["temperatura"].max())
with col2:
    st.metric("Mínima Temperatura (°C)", df_filtrado["temperatura"].min())
    st.metric("Total de Diagnósticos Filtrados", df_filtrado.shape[0])

with st.expander("📂 Ver dados individuais"):
    for _, row in df_filtrado.iterrows():
        with st.container():
            st.markdown(f"**Arquivo:** {row['arquivo']}")
            st.write(row)
