import streamlit as st
from deep_translator import MyMemoryTranslator

st.title("AI Translator App")
st.write("Translate text between languages instantly.")

@st.cache_data
def get_languages():
    return MyMemoryTranslator().get_supported_languages(as_dict=True)

languages = get_languages()
lang_names = list(languages.keys())

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("From Language", ["auto"] + lang_names, index=0)

with col2:
    target_lang = st.selectbox("To Language", lang_names, index=lang_names.index("english") if "english" in lang_names else 0)

text = st.text_area("Enter text to translate:")

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            source_code = "en-us" if source_lang == "auto" else languages[source_lang]
            target_code = languages[target_lang]
            translated = MyMemoryTranslator(source=source_code, target=target_code).translate(text)
            st.subheader("Translated Text:")
            st.success(translated)
        except Exception as e:
            st.error(f"Translation failed: {e}")
