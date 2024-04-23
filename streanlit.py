# Load model directly
import streamlit as st
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google-t5/t5-base")
model = AutoModelForSeq2SeqLM.from_pretrained("google-t5/t5-base")

st.title(''''Using huggingface model with streamlit!!
                Translation for English, German, French, Romanian''')
input = st.text_input(value="translate English to German : ", label="Prompt")

if input:  # Check if input is not empty
  # Generate text using the model
  inputs = tokenizer([input], return_tensors="pt", padding=True)
  outputs = model.generate(**inputs)
  decoded_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]

  # Display the generated text
  st.write("Generated Text:")
  st.write(decoded_text)
