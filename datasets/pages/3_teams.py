import streamlit as st

# Para aplicar a página em tamanho WideScreen
st.set_page_config(
    page_title="Players",
    layout="wide"
)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[(df_data["Club"] == club)].set_index("Name") # Data Frame filtrado pelo clubes, com indice aplicado por nome

st.image(df_filtered.iloc[0]["Club Logo"]) # Para adicionar a imagem do logo
st.markdown(f"## {club}")

# Adicionar colunas da tabela que deseja visualizar
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined',
           "Height(cm.)", 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                    "Overall", format="%d", min_value=0, max_value=100
                    ),
                    "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f",
                                                               min_value=0, max_value=df_filtered["Wage(£)"].max()),
                    "Photo": st.column_config.ImageColumn(),
                    "Flag": st.column_config.ImageColumn("Country"),
             })



