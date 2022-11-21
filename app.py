import streamlit as st

from google.colab import drive
drive.mount('/content/drive')
from transformers import TFAutoModelForCausalLM
model = TFAutoModelForCausalLM.from_pretrained("drive/My Drive/DataScientest - NLP_Mail/Model2_HuggingFace")

def text_generator (feed, length):
   input_sentence = feed
   for i in range(length):
        tokenized = tokenizer(input_sentence, return_tensors="np")
        target_length = len(tokenized['input_ids'][0])+1
        outputs = model.generate(**tokenized, max_length=target_length )
        input_sentence = tokenizer.decode(outputs[0])
   return input_sentence

st.title("NLP Online formail")
length_gen = st.slider('Combien de mot voulez vous generer?', 1, 10, 3)
ingredients = st.text_input('Ingredients (séparer par une virgule) :', 'chicken, beef, carrot')
start = st.text_input('Début de la recette :', 'Cut the chiken in cube')

if st.button('Generate'):
    text_gen = text_generator('[Ingredients]'&ingredients&'[Start]'&start,length_gen)
st.write('Generation : ', text_gen)
