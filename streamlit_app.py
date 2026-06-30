import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st
import random

st.set_page_config(page_title="TrendyAI", page_icon="🚀", layout="wide")

st.title("🚀 TrendyAI - Générateur de Memes & Prompts IA")
st.markdown("**L'app tendance 2026** - Crée des memes viraux et des prompts parfaits !")

st.sidebar.header("💰 Premium")
if st.sidebar.button("S'abonner - 4.99€/mois"):
    st.sidebar.success("✅ Premium activé (démo)")

tab1, tab2 = st.tabs(["🎨 Memes", "✨ Prompts IA"])

with tab1:
    st.header("Créateur de Memes")
    top = st.text_input("Texte du haut", "Quand tu utilises Grok")
    bottom = st.text_input("Texte du bas", "sur Android")
    if st.button("Générer le Meme"):
        st.success(f"{top}\n\n{bottom}")
        st.image("https://picsum.photos/600/400", caption="Ton meme prêt à partager !")

with tab2:
    st.header("Boosteur de Prompts")
    prompt = st.text_area("Ton idée de base", "Un robot qui code sur téléphone")
    if st.button("Améliorer le prompt"):
        enhanced = f"{prompt}, style cyberpunk, ultra réaliste, 8k, détails incroyables, tendance 2026"
        st.code(enhanced)
        st.balloons()

st.caption("App créée avec ❤️ par Grok")