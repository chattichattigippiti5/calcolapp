import streamlit as st

import streamlit.components.v1 as components


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
/* Sfondo blu/turchese */
.stApp {
    background: #0077b6; /* fallback */
    background-image: -webkit-linear-gradient(top, #0077b6, #00b4d8); /* Safari */
    background-image: linear-gradient(to bottom, #0077b6, #00b4d8); /* Standard */
    background-attachment: scroll;
    background-size: cover;
    color: #ffffff;
    overflow-x: hidden;
}

/* Sole semplificato */
.sun {
    position: absolute;
    top: 8%;
    left: 75%;
    width: 120px;
    height: 120px;
    background: radial-gradient(circle, #FFD700 60%, #FFA500 100%);
    border-radius: 50%;
    box-shadow: 0 0 40px 15px rgba(255, 223, 0, 0.6);
    z-index: 0;
}

/* Emoji statiche ai margini */
/* Emoji statiche sparse su tutta la viewport */
.float {
    position: fixed; /* ora relative alla finestra */
    font-size: 55px;
    opacity: 0.6;
    z-index: 0;
    pointer-events: none; /* non interferiscono con bottoni e input */
}

/* Posizionamento ai bordi e distribuiti su tutta la finestra */
.float1 { top: 10%; left: 5%; }
.float2 { top: 25%; right: 8%; }
.float3 { top: 50%; left: 3%; }
.float4 { top: 55%; right: 6%; }
.float5 { bottom: 15%; left: 20%; }
.float6 { bottom: 10%; right: 25%; }


/* Hero */
.hero {
    height: 50vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}
.hero h1 {
    font-size: 3em;
    margin: 0;
    color: #ffffff;
    text-shadow: 1px 1px 6px rgba(0,0,0,0.4);
}
.hero p {
    font-size: 1.3em;
    margin-top: 15px;
    color: #d9f7ff;
    max-width: 800px;
}

/* Risultato */
.result-box {
    text-align: center;
    font-size: 2em;
    background: #00b4d8;
    padding: 18px;
    border-radius: 10px;
    margin-top: 30px;
    color: #00334d;
    font-weight: bold;
    box-shadow: 0 0 20px rgba(255,255,255,0.4);
}

/* Pulsanti (rosso/arancio caldo) */
.stButton button {
    background: linear-gradient(90deg, #ff4d4d, #ff944d) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    border: none !important;
}
.stButton button:hover {
    transform: scale(1.05);
    transition: 0.3s;
    background: linear-gradient(90deg, #ff1a1a, #ff751a) !important;
}

/* Input */
div[data-baseweb="input"] > input,
div[data-baseweb="input"] > textarea {
    background-color: #caf0f8 !important;
    color: #00334d !important;
    border-radius: 10px !important;
    border: 2px solid #00bcd4 !important;
}

/* Expander */
.streamlit-expanderHeader {
    background-color: #0096c7 !important;
    color: #ffffff !important;
    font-weight: bold;
    border-radius: 8px;
}
</style>

<div class="sun"></div>
<div class="float float1">🕶️</div>
<div class="float float2">🍍</div>
<div class="float float3">🍸</div>
<div class="float float4">🍓</div>
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
    },
    "es": {
        "alcolici": "Bebidas alcohólicas",
        "analcolici": "Ingredientes sin alcohol",
        "quantitativo": "Cantidad (ml)",
        "gradazione": "Graduación alcohólica (% vol)",
        "ingrediente": "Ingrediente",
        "calcola": "Calcular graduación 🍸",
        "reset": "🌴🔄 Siguiente 🌞",
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
            col_q, col_g = st.columns([1, 1])
            with col_q:
                q = st.text_input(f"{L['q']}", key=f"q_alc_{i}")
            with col_g:
                g = st.text_input(f"{L['g']}", key=f"g_alc_{i}")
            alcolici.append((q, g))

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
            q = st.text_input(f"{L['q']}", key=f"q_ing_{i}")
            analcolici.append(q)


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
            lista_alcolici = [(float(q), float(g)) for q, g in alcolici if q.strip() and g.strip()]
            lista_analcolici = [float(q) for q in analcolici if q.strip()]

            grado_alcol = sum(q * g for q, g in lista_alcolici)
            q_tot = sum(q for q, _ in lista_alcolici) + sum(lista_analcolici)

            if q_tot > 0:
                st.session_state["last_result"] = round(grado_alcol / q_tot, 2)
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
