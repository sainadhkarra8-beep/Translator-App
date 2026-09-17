import streamlit as st
from deep_translator import GoogleTranslator

st.title("AI Translator App")
st.write("Translate text between languages instantly.")

languages = {
    "english": "en",
    "telugu": "te",
    "hindi": "hi",
    "tamil": "ta",
    "kannada": "kn",
    "french": "fr",
    "spanish": "es",
    "german": "de",
    "chinese (simplified)": "zh-CN",
    "japanese": "ja",
    "arabic": "ar",
    "russian": "ru",
    "malayalam": "ml",
    "marathi": "mr",
    "urdu": "ur",
    "bengali": "bn",
    "gujarati": "gu",
    "punjabi": "pa",
    "portuguese": "pt",
    "italian": "it",
}

lang_names = list(languages.keys())

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From Language", ["auto"] + lang_names, index=0)

with col2:
    target_lang = st.selectbox("To Language", lang_names, index=lang_names.index("english"))

text = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            source_code = "auto" if source_lang == "auto" else languages[source_lang]
            target_code = languages[target_lang]
            translated = GoogleTranslator(source=source_code, target=target_code).translate(text)
            st.subheader("Translated Text:")
            st.success(translated)
        except Exception as e:
            st.error(f"Translation failed: {e}")
