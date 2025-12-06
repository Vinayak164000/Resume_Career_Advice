import streamlit as st
import base64
from agent import AgentBuilder
from base_model import Model

st.header("Resume Checker and Career Advisor")

def generate_response(input_text):
    model = AgentBuilder()
    response = model.agent_response(input_text)
    final_output = (f"** Response:**\n{response.punny_response}\n\n{response.career_advice}")
    st.markdown(final_output)

def pdf_response(prompt_file):
    pdf_bytes = prompt_file.read()
    pdf_base = base64.b64encode(pdf_bytes).decode("utf-8")
    my_model = Model()
    response = my_model.model_response(pdf_base)
    st.markdown(f"** Response:**\n{response}")



prompt = st.chat_input(
    "Write you career details in bulleted points here... or attach pdf file",
    accept_file= True,
    file_type=["pdf"]
)


if prompt:
    if prompt.text:
        generate_response(prompt.text)

    elif prompt["files"]:
        pdf_file = prompt["files"][0]
        pdf_response(pdf_file)


