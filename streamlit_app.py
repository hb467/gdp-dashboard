import streamlit as st
import pandas as pd
from datetime import datetime

# Mock data for the dashboard
data = {
    "FIN": [],
    "Produktvariante": [],
    "Im Takt?": [],
    "Fehlercode": [],
    "Bemerkung": [],
    "Qualität": [],
    "Meldezeit": [],
    "Taktzeit": []
}

df = pd.DataFrame(data)

# Set page configuration
st.set_page_config(page_title="Produktionsdokumentation Dashboard", layout="wide")

# Divide page into three parts: top, buttons, and bottom
header_container = st.container()
button_container = st.container()
table_container = st.container()

with header_container:
    st.markdown(
        """
        <div style='background-color: #2196F3; padding: 20px;'>
            <h2 style='color: white; text-align: center;'>Produktionsdokumentation Dashboard</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

with button_container:
    col1, col_mid, col2 = st.columns([1, 6, 1])
    with col1:
    if st.button("Eingabe der Schicht"):
        st.info("Eingabeformular ist oben verfügbar.")
    with col_mid:
        st.markdown("<h5 style='text-align: center; margin: 0;'>Schichtübersicht</h5>", unsafe_allow_html=True)
    with col2:
    if st.button("Letzten Eintrag löschen"):
        if not df.empty:
            df = df.iloc[:-1]
            st.warning("Der letzte Eintrag wurde gelöscht.")
        else:
            st.warning("Es gibt keine Einträge zum Löschen.")



with table_container:
    # Display Table with Data Entries
    st.dataframe(df, use_container_width=True)

