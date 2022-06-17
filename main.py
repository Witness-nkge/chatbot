import streamlit as st
from transformers import pipeline

st.title('AI Homework Helper')
context = st.text_input('input context or paragraph you want to ask questions based on')
question = st.text_input('input your question')

if st.button('answer'):
  qna = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")
  answer = qna(question = question,context = context)
  st.write(f"Answer: '{answer['answer']} \nConfindence: {answer['score']}")
