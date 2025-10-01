import streamlit as st

import streamlit.components.v1 as components

import pandas as pd

# Carica la lista alcolici da CSV
df_alcolici = pd.read_csv("lista_alcolici.csv", sep=";")

# Crea un dizionario {nome: gradazione}
alcolici_db = dict(zip(df_alcolici["Nome"], df_alcolici["Gradazione"]))


st.set_page_config(page_title="Calcolatore Cocktail", page_icon="🍹", layout="wide")

components.html(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-QRZKCGPPKY"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-QRZKCGPPKY');
    </script>
    """,
    height=0,
    width=0,
)

# -------------------
# CSS + animazioni
# -------------------
page_bg = """
<style>
/* Sfondo rosso/arancio caldo */
.stApp {
    background: #ff4d4d; /* fallback */
    background-image: -webkit-linear-gradient(top, #ff4d4d, #ff944d); /* Safari */
    background-image: linear-gradient(to bottom, #ff4d4d, #ff944d); /* Standard */
    background-attachment: scroll; /* Safari fix */
    background-size: cover;
    color: #ccff33;
    overflow-x: hidden;
}



/* Sole animato */
.sun {
    position: absolute;
    top: 5%;
    left: 80%;
    width: 150px;
    height: 150px;
    background: radial-gradient(circle, #FFD700 40%, #FFA500 100%);
    border-radius: 50%;
    box-shadow: 0 0 80px 30px rgba(255, 223, 0, 0.8);
    animation: pulse 6s ease-in-out infinite, colorShift 10s linear infinite;
    z-index: 0;
}

.sun::before {
    content: "";
    position: absolute;
    top: -50px;
    left: -50px;
    right: -50px;
    bottom: -50px;
    border: 12px solid rgba(255, 215, 0, 0.5);
    border-radius: 50%;
    animation: spin 25s linear infinite, pulse 6s ease-in-out infinite;
}

/* Emoji animate */
.float {
    position: fixed;
    font-size: 60px;
    opacity: 0.8;
    animation: floaty 14s ease-in-out infinite, fade 6s ease-in-out infinite alternate;
    z-index: 0;
}

.float1 { top: 70%; left: 10%; animation-delay: 0s, 0s; }
.float2 { top: 60%; left: 80%; animation-delay: 3s, 2s; }
.float3 { top: 85%; left: 40%; animation-delay: 6s, 4s; }
.float4 { top: 20%; left: 15%; animation-delay: 9s, 1s; }
.float5 { top: 30%; left: 60%; animation-delay: 12s, 3s; }
.float6 { top: 75%; left: 70%; animation-delay: 15s, 5s; }

/* Hero */
.hero {
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.hero h1 {
    font-size: 3em;
    margin: 0;
    color: #ccff33;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}
.hero p {
    font-size: 1.3em;
    margin-top: 20px;
    color: #ccff33;
    max-width: 800px;
}

/* Risultato */
.result-box {
    text-align: center;
    font-size: 2em;
    background: #FFD700;
    padding: 20px;
    border-radius: 12px;
    margin-top: 30px;
    color: #00334d;
    font-weight: bold;
    box-shadow: 0 0 25px rgba(255,255,255,0.6);
}

/* Input */
div[data-baseweb="input"] > input,
div[data-baseweb="input"] > textarea {
    background-color: #d1f7ff !important;
    color: #00334d !important;
    border-radius: 10px !important;
    border: 2px solid #00bcd4 !important;
}
.streamlit-expanderHeader {
    background-color: #00bcd4 !important;
    color: #00334d !important;
    font-weight: bold;
    border-radius: 8px;
}
.stButton button {
    background: linear-gradient(90deg, #00e5ff, #00bcd4) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    border: none !important;
}
.stButton button:hover {
    transform: scale(1.05);
    transition: 0.3s;
}

/* Label grandi */
.big-label {
    font-size: 1.2em;
    font-weight: bold;
    color: #00334d;
    margin-bottom: 10px;
}

/* Animazioni */
@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}
@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
@keyframes floaty {
    0% { transform: translate(0px, 0px); }
    50% { transform: translate(20px, -40px); }
    100% { transform: translate(0px, 0px); }
}
@keyframes fade {
    from { opacity: 0.4; }
    to { opacity: 1; }
}
@keyframes colorShift {
    0% { background: radial-gradient(circle, #FFD700 40%, #FFA500 100%); }
    50% { background: radial-gradient(circle, #FFA500 40%, #FF6347 100%); }
    100% { background: radial-gradient(circle, #FFD700 40%, #FFA500 100%); }
}

/* --- Mobile responsive fix --- */

@media (max-width: 768px) {
    /* Le colonne di Streamlit diventano blocchi verticali */
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }
    .stHorizontalBlock {
        flex-direction: column !important;
    }
    .stColumn {
        width: 100% !important;
        flex: 1 1 100% !important;
    }

    /* Titoli e testo più leggibili */
    .hero h1 {
        font-size: 2em !important;
    }
    .hero p {
        font-size: 1.1em !important;
    }
    .result-box {
        font-size: 1.5em !important;
    }

    /* bandiere allineate */
    .flags-container {
        display: flex;
        justify-content: center;
        gap: 12px;
        margin-bottom: 15px;
    }
    .flags-container button {
        font-size: 1.5em !important;
        padding: 4px 8px;
    }

    /* Inputs e pulsanti più grandi */
    input, textarea {
        font-size: 18px !important;
    }
    .stButton button {
        width: 100% !important;
        font-size: 18px !important;
    }

    /* Titoli centrati */
    h1, h2, h3, label {
        text-align: center !important;
    }
}

</style>

<div class="sun"></div>
<div class="float float1">🕶️</div>
<div class="float float2">⛱️</div>
<div class="float float3">🏖️</div>
<div class="float float4">🍸</div>
<div class="float float5">🍹</div>
<div class="float float6">🌊</div>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- CSS per modificare lo sfondo degli errori ---
error_style = """
<style>
.stAlert {
    background-color: black !important;  /* oppure white */
    color: white !important;             /* se scegli white sopra, qui metti black */
    border-radius: 10px;
    padding: 15px;
    font-weight: bold;
}
</style>
"""
st.markdown(error_style, unsafe_allow_html=True)

# -------------------
# TRADUZIONI
# -------------------
TEXTS = {
    "it": {
        "title": "🍹 Calcolatore di Gradazione Alcolica Cocktail",
        "subtitle": ("Vuoi stupire i tuoi amici? Ti senti particolarmente creativo oggi? "
                     "Il nostro calcolatore è il tuo migliore alleato per creare un cocktail bilanciato "
                     "e diventare il <b>re della festa</b>! 🍓🍍🥭"),
        "alcolici": "🍷 Alcolici",
        "analcolici": "🍹 Ingredienti analcolici",
        "n_alcol": "Quanti alcolici ha il tuo cocktail?",
        "n_analcol": "Quanti altri ingredienti ha il tuo cocktail?",
        "alc": "Alcolico",
        "ing": "Ingrediente",
        "q": "Quantitativo (ml)",
        "g": "Gradazione (% vol)",
        "calc": "Calcola Gradazione 🍸",
        "reset": "🌴🔄 Prossimo cocktail 🌞",
        "error_num": "Errore: devi inserire solo numeri validi!",
        "error_ing": "Errore: devi inserire almeno un ingrediente con quantità > 0!",
        "result": "👉 {value} % 🌴🥥"
    },
    "en": {
        "title": "🍹 Cocktail Alcohol Content Calculator",
        "subtitle": ("Want to impress your friends? Feeling creative today? "
                     "Our calculator is your best ally to create a balanced cocktail "
                     "and become the <b>life of the party</b>! 🍓🍍🥭"),
        "alcolici": "🍷 Alcoholic ingredients",
        "analcolici": "🍹 Non-alcoholic ingredients",
        "n_alcol": "How many alcoholic ingredients does your cocktail have?",
        "n_analcol": "How many other ingredients does your cocktail have?",
        "alc": "Alcohol",
        "ing": "Ingredient",
        "q": "Quantity (ml)",
        "g": "Alcohol by volume (% vol)",
        "calc": "Calculate ABV 🍸",
        "reset": "🌴🔄 Next cocktail 🌞",
        "error_num": "Error: you must insert only valid numbers!",
        "error_ing": "Error: you must insert at least one ingredient with a quantity > 0!",
        "result": "👉 {value} % 🌴🥥"
    },
    "es": {
        "title": "🍹 Calculadora de Graduación Alcohólica de Cócteles",
        "subtitle": ("¿Quieres impresionar a tus amigos? ¿Te sientes creativo hoy? "
                     "¡Nuestra calculadora es tu mejor aliada para crear un cóctel equilibrado "
                     "y convertirte en el <b>rey de la fiesta</b>! 🍓🍍🥭"),
        "alcolici": "🍷 Ingredientes alcohólicos",
        "analcolici": "🍹 Ingredientes sin alcohol",
        "n_alcol": "¿Cuántos ingredientes alcohólicos tiene tu cóctel?",
        "n_analcol": "¿Cuántos otros ingredientes tiene tu cóctel?",
        "alc": "Alcohólico",
        "ing": "Ingrediente",
        "q": "Cantidad (ml)",
        "g": "Graduación (% vol)",
        "calc": "Calcular graduación 🍸",
        "reset": "🌴🔄 Siguiente cóctel 🌞",
        "error_num": "Error: ¡debes insertar solo números válidos!",
        "error_ing": "Error: ¡debes insertar al menos un ingrediente con cantidad > 0!",
        "result": "👉 {value} % 🌴🥥"
    }
}

# -------------------
# LINGUA
# -------------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "it"

# --- Traduzioni ---
translations = {
    "it": {
        "alcolici": "Alcolici",
        "analcolici": "Ingredienti analcolici",
        "quantitativo": "Quantitativo (ml)",
        "gradazione": "Gradazione (% vol)",
        "ingrediente": "Ingrediente",
        "calcola": "Calcola Gradazione 🍸",
        "reset": "🌴🔄 Prossimo 🌞",
    },
    "en": {
        "alcolici": "Alcoholic drinks",
        "analcolici": "Non-alcoholic ingredients",
        "quantitativo": "Quantity (ml)",
        "gradazione": "Alcohol content (% vol)",
        "ingrediente": "Ingredient",
        "calcola": "Calculate ABV 🍸",
        "reset": "🌴🔄 Next 🌞",
        "Nome ingrediente" : "Ingredient's name",
        "Seleziona Alcolico" : "Choose alcohol",
    },
    "es": {
        "alcolici": "Bebidas alcohólicas",
        "analcolici": "Ingredientes sin alcohol",
        "quantitativo": "Cantidad (ml)",
        "gradazione": "Graduación alcohólica (% vol)",
        "ingrediente": "Ingrediente",
        "calcola": "Calcular graduación 🍸",
        "reset": "🌴🔄 Siguiente 🌞",
        "Nome ingrediente" : "Nombre ingrediente",
        "Seleziona Alcolico" : "Seleccionas alcohol",
    }
}

lang = st.session_state.get("lang", "it")
t = translations[lang]


# Bandiere
col_space, col_it, col_en, col_es = st.columns([7.5, 0.5, 0.5, 0.5])
with col_it:
    if st.button("🇮🇹"):
        st.session_state["lang"] = "it"
        st.rerun()
with col_en:
    if st.button("🇬🇧"):
        st.session_state["lang"] = "en"
        st.rerun()
with col_es:
    if st.button("🇪🇸"):
        st.session_state["lang"] = "es"
        st.rerun()

L = TEXTS[st.session_state["lang"]]

# -------------------
# HERO
# -------------------
st.markdown(f"<div class='hero'><h1>{L['title']}</h1><p>{L['subtitle']}</p></div>", unsafe_allow_html=True)


# Layout due colonne
# -------------------
col1, col2 = st.columns(2)

with col1:
    st.header(L["alcolici"])
    n_alcol = st.number_input(
        L["n_alcol"],
        min_value=0,
        step=1,
        key="n_alcol"
    )

    alcolici = []
    for i in range(n_alcol):
        with st.expander(f"{L['alc']} {i+1}"):
            col_nome, col_grad = st.columns([2, 1])

            with col_nome:
                # Menu a tendina con alcolici dal CSV + "Altro"
                alcolico_scelto = st.selectbox(
                    f"Seleziona alcolico {i+1}",
                    options=list(alcolici_db.keys()) + ["Altro / Other"],
                    key=f"alc_nome_{i}"
                )

                if alcolico_scelto == "Altro / Other":
                    nome_altro = st.text_input(f"Nome alcolico {i+1}", key=f"nome_altro_{i}")
                else:
                    nome_altro = alcolico_scelto


            with col_grad:
                if alcolico_scelto != "Altro / Other":
                    g = alcolici_db[alcolico_scelto]
                    st.markdown(f"**Gradazione: {g}%**")
                else:
                    g = st.text_input(
                    f"{L['g']}",
                    key=f"g_alc_{i}"
                    )


            # Campo quantitativo sempre presente
            q = st.text_input(f"{L['q']}", key=f"q_alc_{i}")

            # Aggiunge alla lista
            alcolici.append((nome_altro, q, g))



with col2:
    st.header(L["analcolici"])
    n_analcol = st.number_input(
        L["n_analcol"],
        min_value=0,
        step=1,
        key="n_analcol"
    )

    analcolici = []
    for i in range(n_analcol):
        with st.expander(f"{L['ing']} {i+1}"):
            # Campo per il nome dell'ingrediente
            nome = st.text_input(f"Nome ingrediente {i+1}", key=f"nome_ing_{i}")
            # Campo per il quantitativo
            q = st.text_input(f"{L['q']}", key=f"q_ing_{i}")
            analcolici.append((nome, q))



# -------------------
# Pulsanti
# -------------------
# --- Bottoni azione ---
st.markdown("<div style='text-align: center; margin-top: 30px;'>", unsafe_allow_html=True)

# --- Pulsanti centrati e vicini ---
col_spacer, col_btn1, col_btn2, col_spacer2 = st.columns([1, 2, 1, 1])

with col_btn1:
    if st.button(L["calc"]):
        try:
            #lista_alcolici: (nome, q, g)
            lista_alcolici = [(nome, float(q), float(g))
                                for nome, q, g in alcolici if str(q).strip() and str(g).strip()]
            lista_analcolici = [(nome, float(q))
                                for nome, q in analcolici if str(q).strip()]

            grado_alcol = sum(q * g for _, q, g in lista_alcolici)
            q_tot = sum(q for _, q, _ in lista_alcolici) + sum(q for _, q in lista_analcolici)

            if q_tot > 0:
                st.session_state["last_result"] = round(grado_alcol / q_tot, 2)

                # 🔹 Prepariamo il testo della ricetta
                cocktail_txt = "════════════════════════════════════\n"
                cocktail_txt += "   🍸                            🍸\n"
                cocktail_txt += "════════════════════════════════════\n\n"

                cocktail_txt += "🥃 Alcolici:\n"
                for nome, q, g in lista_alcolici:
                    cocktail_txt += f"- {nome:<12} {q} ml @ {g}%\n"

                cocktail_txt += "\n🥤 Analcolici:\n"
                for nome, q in lista_analcolici:
                    cocktail_txt += f"- {nome:<12} {q} ml\n"

                cocktail_txt += "\n------------------------------------\n"
                cocktail_txt += f"👉 : {st.session_state['last_result']} % vol\n"
                cocktail_txt += "════════════════════════════════════\n"


                # 🔹 Pulsante di download
                # 🔹 Pulsante di download centrato in basso e rosso
                st.markdown(
                    """
                    <style>
                    .centered-download {
                        display: flex;
                        justify-content: center;
                        margin-top: 40px;
                    }
                    .stDownloadButton button {
                        background-color: #ff4d4d !important; /* Rosso */
                        color: white !important;             /* Testo bianco */
                        font-weight: bold !important;
                        border-radius: 10px !important;
                        padding: 12px 24px !important;
                        font-size: 18px !important;
                    }
                    .stDownloadButton button:hover {
                        background-color: #cc0000 !important; /* Rosso più scuro al passaggio */
                        transform: scale(1.05);
                        transition: 0.3s;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

                with st.container():
                    st.markdown("<div class='centered-download'>", unsafe_allow_html=True)
                    st.download_button(
                        label="📥 Download ricetta",
                        data=cocktail_txt,
                        file_name="cocktail.txt",
                        mime="text/plain",
                        key="download_button"
                    )
                    st.markdown("</div>", unsafe_allow_html=True)


            else:
                                st.error(L["error_ing"])
        except ValueError:
                            st.error(L["error_num"])


with col_btn2:
    if st.button(L["reset"]):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()



st.markdown("</div>", unsafe_allow_html=True)

# -------------------
# Risultato
# -------------------
if "last_result" in st.session_state:
    st.markdown(
        f"<div class='result-box'>{L['result'].format(value=st.session_state['last_result'])}</div>",
        unsafe_allow_html=True
    )
