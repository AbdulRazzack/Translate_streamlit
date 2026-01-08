import streamlit as st
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# 1. Use @st.cache_resource so the model loads only once, not on every user action
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-base")
    model = AutoModelForSeq2SeqLM.from_pretrained("google-t5/t5-base")
    return tokenizer, model

tokenizer, model = load_model()

st.title('T5-Base Translator')
st.subheader('English, German, French, Romanian')

# 2. Create columns for the language selectors for a better layout
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        ["English", "German", "French", "Romanian"]
    )

with col2:
    # Filter target options to avoid translating English to English, etc.
    # (Though T5 can handle it, it's better UX to distinct them)
    options = ["English", "German", "French", "Romanian"]
    target_lang = st.selectbox(
        "Target Language",
        options,
        index=1 # Default to German
    )

# 3. Text Area for input (separated from the command)
text_to_translate = st.text_area("Enter text to translate:", height=150)

# 4. Button to trigger translation
if st.button("Translate"):
    if text_to_translate:
        with st.spinner('Translating...'):
            # Construct the T5 specific prefix format
            # Format: "translate <Source> to <Target>: <Text>"
            prompt = f"translate {source_lang} to {target_lang}: {text_to_translate}"
            
            # Generate text
            inputs = tokenizer([prompt], return_tensors="pt", padding=True)
            output_sequences = model.generate(
                **inputs, 
                max_length=512,  # Allow for longer translations
                num_beams=5,     # Improves quality slightly
                early_stopping=True
            )
            
            decoded_text = tokenizer.batch_decode(output_sequences, skip_special_tokens=True)[0]

            # Display Result
            st.success("Translation Complete:")
            st.markdown(f"**{decoded_text}**")
    else:
        st.warning("Please enter some text to translate.")
