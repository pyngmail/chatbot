import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = "Qwen/Qwen2-0.5B-Instruct",
    task = "text-generation",
    pipeline_kwargs = {"max_new_tokens":500},
)


def generate_response(text):
    for r in llm.stream(text):
        yield r


st.title("This is ChatBot")

with st.form("form"):
    text = st.text_area("Enter text:","")
    submitted = st.form_submit_button('submit')
    if submitted :
        st.write_stream(generate_response(text))
