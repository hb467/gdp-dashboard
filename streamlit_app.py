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

# Divide page into two parts: top and bottom
header_container = st.container()
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

with table_container:
    # Display Table with Data Entries
    st.dataframe(df, use_container_width=True)

    # Save the data to a CSV file
    if st.button("Daten speichern"):
        df.to_csv("produktionsdaten.csv", index=False)
        st.success("Daten wurden erfolgreich gespeichert.")
