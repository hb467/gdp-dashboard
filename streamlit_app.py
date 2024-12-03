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

    # Form to Input Data
    with st.form("data_entry_form"):
        st.subheader("Auftragsdaten SATTELHALS eingeben")
        arbeitsplatz = st.text_input("Ausgewählter Arbeitsplatz", "Sattelhals", disabled=True)
        fin = st.text_input("FIN")
        variante = st.selectbox("Variante", ["Standard", "RoRo", "Co2"])
        datum_schichtbeginn = st.date_input("Datum Schichtbeginn", datetime.today())
        schicht = st.selectbox("Schicht", ["Früh", "Spät", "Nacht"])
        meldezeit = st.time_input("Meldezeit", datetime.now().time())
        zeit_letzte_meldung = st.time_input("Zeit letzte Meldung", datetime.now().time())
        zeit_seit_letzter_meldung = st.number_input("Zeit seit letzter Meldung (Minuten)", min_value=0, value=0)
        vorgegebene_taktzeit = st.text_input("Vorgegebene Taktzeit", "00:25:30", disabled=True)
        in_taktzeit_gefertigt = st.radio("In Taktzeit gefertigt?", ["Ja", "Nein"])
        fehlercode = st.selectbox("Fehlercode", [
            "Störung auswählen", "Technische Störung", "Zündfehler", "Warten auf Logistik",
            "Brennerwechsel", "Fehler ohne Alarm", "Rüsten", "Drahtwechsel", "Anlage nicht besetzt", "Sonstiges"
        ])
        bemerkungen = st.text_area("Bemerkungen")
        qualitaet = st.radio("Qualität des gefertigten Produktes?", [
            "i.O. fehlerfrei / Direktläufer", "e.i.O. Nacharbeit nötig", "n.i.O. Ausschuss"
        ])
        submit_button = st.form_submit_button(label="Eingabe")

# Handling form submission
if submit_button:
    new_data = {
        "FIN": fin,
        "Produktvariante": variante,
        "Im Takt?": in_taktzeit_gefertigt,
        "Fehlercode": fehlercode if fehlercode != "Störung auswählen" else "",
        "Bemerkung": bemerkungen,
        "Qualität": qualitaet,
        "Meldezeit": meldezeit.strftime("%H:%M"),
        "Taktzeit": vorgegebene_taktzeit
    }
    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    st.success(f"Sattelhals Daten hinzugefügt: FIN {fin}")

with button_container:
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Eingabe Deckschicht"):
            # Open a modal-like window for entering data
            with st.expander("Deckschicht-Daten eingeben", expanded=True):
                st.subheader("Deckschicht-Daten eingeben")
                fin = st.text_input("FIN (Deckschicht)")
                variante = st.selectbox("Variante (Deckschicht)", ["Standard", "RoRo", "Co2"])
                datum_schichtbeginn = st.date_input("Datum Schichtbeginn (Deckschicht)", datetime.today())
                schicht = st.selectbox("Schicht (Deckschicht)", ["Früh", "Spät", "Nacht"])
                meldezeit = st.time_input("Meldezeit (Deckschicht)", datetime.now().time())
                vorgegebene_taktzeit = st.text_input("Vorgegebene Taktzeit (Deckschicht)", "00:25:30", disabled=True)
                in_taktzeit_gefertigt = st.radio("In Taktzeit gefertigt? (Deckschicht)", ["Ja", "Nein"])
                fehlercode = st.selectbox("Fehlercode (Deckschicht)", [
                    "Störung auswählen", "Technische Störung", "Zündfehler", "Warten auf Logistik",
                    "Brennerwechsel", "Fehler ohne Alarm", "Rüsten", "Drahtwechsel", "Anlage nicht besetzt", "Sonstiges"
                ])
                bemerkungen = st.text_area("Bemerkungen (Deckschicht)")
                qualitaet = st.radio("Qualität des gefertigten Produktes? (Deckschicht)", [
                    "i.O. fehlerfrei / Direktläufer", "e.i.O. Nacharbeit nötig", "n.i.O. Ausschuss"
                ])

                if st.button("Deckschicht-Daten speichern"):
                    new_data = {
                        "FIN": fin,
                        "Produktvariante": variante,
                        "Im Takt?": in_taktzeit_gefertigt,
                        "Fehlercode": fehlercode if fehlercode != "Störung auswählen" else "",
                        "Bemerkung": bemerkungen,
                        "Qualität": qualitaet,
                        "Meldezeit": meldezeit.strftime("%H:%M"),
                        "Taktzeit": vorgegebene_taktzeit
                    }
                    df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
                    st.success(f"Deckschicht Daten hinzugefügt: FIN {fin}")
    with col2:
        if st.button("Letzten Eintrag löschen"):
            if not df.empty:
                df = df.iloc[:-1]
                st.warning("Der letzte Eintrag wurde gelöscht.")
            else:
                st.warning("Es gibt keine Einträge zum Löschen.")

with table_container:
    st.markdown(
        """
        <div style='background-color: white; padding: 10px; margin-top: 20px;'>
            <h3 style='text-align: center;'>Schichtübersicht</h3>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Display Table with Data Entries
    st.dataframe(df)

    # Save the data to a CSV file
    if st.button("Daten speichern"):
        df.to_csv("produktionsdaten.csv", index=False)
        st.success("Daten wurden erfolgreich gespeichert.")
