import streamlit as st

st.title("Calcola Prezzo noleggio auto")

giorni = st.number_input("Giorni di noleggio", min_value=1, required = True, step = 1)
veicolo = st.selectbox("Tipo di mezzo",options=[{"Modello": "Utilitaria","Prezzo":35},
                                        {"Modello": "Berlina","Prezzo":60},
                                        {"Modello": "SUV","Prezzo":90}], format_func=lambda x: f"{x['Modello']} - {x['Prezzo']}€ al giorno")
st.text("Supplementi")
cambio_automatico = st.checkbox("Cambio automatico - 10€ al giorno")
assicurazione_kasko = st.checkbox("Assicurazione Kasko - 15 € al giorno")
if st.button("Calcola Preventivo"):
    st.write(f"HAI SELEZIONATO {giorni} GIORNI DI NOLEGGIO, {veicolo['Modello']} - {veicolo['Prezzo']}€ AL GIORNO")
    st.write(f"SUPPLEMENTI: {'Cambio automatico' if cambio_automatico else ''} {'Assicurazione Kasko' if assicurazione_kasko else ''}")    
    totale = giorni * veicolo['Prezzo'] + (10 * giorni if cambio_automatico else 0) + (15 * giorni if assicurazione_kasko else 0)
    st.write(f"IL PREVENTIVO TOTALE È: {totale}€")