import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    st.session_state["data"] = df_data


st.markdown("# FIFA23 OFFICIAL DATASET")
st.sidebar.markdown("Desenvolvido por Xind (https://www.globo.com/)")

btn = st.button("Acesso dados no Kaggle")
if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/")