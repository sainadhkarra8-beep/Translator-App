import streamlit as st
from deep_translator import MyMemoryTranslator

st.title("AI Translator App")
st.write("Translate text between languages instantly.")

languages = {
    "english": "en-US",
    "telugu": "te-IN",
    "hindi": "hi-IN",
    "tamil": "ta-IN",
    "kannada": "kn-IN",
    "french": "fr-FR",
    "spanish": "es-ES",
    "german": "de-DE",
    "japanese": "ja-JP",
    "arabic": "ar-SA",
    "russian": "ru-RU",
    "malayalam": "ml-IN",
    "marathi": "mr-IN",
    "urdu": "ur-PK",
    "bengali": "bn-IN",
    "gujarati": "gu-IN",
    "punjabi": "pa-IN",
    "portuguese": "pt-PT",
    "italian": "it-IT",
    "chinese": "zh-CN",
}

lang_names = list(languages.keys())

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From Language", lang_names, index=lang_names.index("english"))

with col2:
    target_lang = st.selectbox("To Language", lang_names, index=lang_names.index("telugu"))

text = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            source_code = languages[source_lang]
            target_code = languages[target_lang]
            translated = MyMemoryTranslator(source=source_code, target=target_code).translate(text)
if translated and translated.strip():
    st.subheader("Translated Text:")
    st.success(translated)
else:
    st.warning("This language pair isn't supported right now. Try a different language.")
        except Exception as e:
            st.error(f"Translation failed: {e}")
