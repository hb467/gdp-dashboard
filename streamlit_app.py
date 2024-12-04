import streamlit as st
import pandas as pd

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

# Header Container:
st.markdown(
    """
    <div style='display: flex; margin: 0; padding: 0;'>
        <div style="background-color: #1E3A8A; padding: 60px; flex: 1;"></div>
        <div style="background-color: #2196F3; padding: 60px; flex: 1; position: relative;">
            <div style="position: absolute; bottom: 10px; width: 100%; padding: 0 20px; box-sizing: border-box;">
                <div style="display: flex; align-items: center; margin-bottom: 5px;">
                    <span style="color: white; font-weight: bold; margin-right: 5px;">Datum:</span>
                    <input type="date" style="width: 90px; padding: 3px; height: 28px; border: 1px solid #ccc; border-radius: 4px;">
                </div>
                <div style="display: flex; align-items: center;">
                    <span style="color: white; font-weight: bold; margin-right: 10px;">Schicht:</span>
                    <select style="width: 90px; padding: 3px; height: 28px; border: 1px solid #ccc; border-radius: 4px;">
                        <option value="Früh">Früh</option>
                        <option value="Spät">Spät</option>
                        <option value="Nacht">Nacht</option>
                    </select>
                </div>
            </div>
        </div>
        <div style="background-color: #2196F3; padding: 60px; flex: 1; position: relative;">
            <div style="position: absolute; bottom: 10px; width: 100%; padding: 0 20px; box-sizing: border-box;">
                <div style="display: flex; align-items: center; margin-bottom: 5px;">
                    <span style="color: white; font-weight: bold; margin-right: 10px;">Beginn:</span>
                    <select style="width: 90px; padding: 3px; height: 28px; border: 1px solid #ccc; border-radius: 4px;">
                        """ + "\n".join([f"<option value='{h:02}:00'>{h:02}:00</option>" for h in range(24)]) + """
                    </select>
                </div>
                <div style="display: flex; align-items: center;">
                    <span style="color: white; font-weight: bold; margin-right: 5px;">Ende:</span>
                    <select style="width: 90px; padding: 3px; height: 28px; border: 1px solid #ccc; border-radius: 4px;">
                        """ + "\n".join([f"<option value='{h:02}:00'>{h:02}:00</option>" for h in range(24)]) + """
                    </select>
                </div>
            </div>
        </div>
        <div style="background-color: #2196F3; padding: 60px; flex: 1;"></div>
        <div style="background-color: #2196F3; padding: 60px; flex: 1;"></div>
        <div style="background-color: #2196F3; padding: 60px; flex: 1;"></div>
        <div style="background-color: #2196F3; padding: 60px; flex: 1; position: relative;">
            <div style="position: absolute; bottom: 10px; width: 100%; padding: 0 20px; box-sizing: border-box;">
                <div style="display: flex; align-items: center;">
                    <span style="color: white; font-weight: bold; margin-right: 10px;">Direktläufer:</span>
                    <select style="width: 90px; padding: 3px; height: 28px; border: 1px solid #ccc; border-radius: 4px;">
                        <option value="Ja">Ja</option>
                        <option value="Nein">Nein</option>
                    </select>
                </div>
            </div>
        </div>
<div style="background-color: black; padding: 60px; flex: 1;"></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Button Container
with st.container():
    col1, col_mid, col2 = st.columns([1, 6, 1])
    with col1:
        if st.button("Eingabe der Deckschicht"):
            st.info("Eingabeformular ist oben verfügbar.")
    with col_mid:
        st.markdown("<h5 style='text-align: center;'>Schichtübersicht</h5>", unsafe_allow_html=True)
    with col2:
        if st.button("Letzten Eintrag löschen"):
            if not df.empty:
                df = df.iloc[:-1]
                st.warning("Der letzte Eintrag wurde gelöscht.")
            else:
                st.warning("Es gibt keine Einträge zum Löschen.")

# Table Container
with st.container():
    st.dataframe(df, use_container_width=True)
