import streamlit as st
from agent import AgentBuilder

st.header("Resume Checker and Career Advisor")

def generate_response(input_text):
    model = AgentBuilder()
    response = model.agent_response(input_text)
    final_output = (f"** Response:**\n{response.punny_response}\n\n{response.career_advice}")
    st.markdown(final_output)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Write you career details in bulleted points here...",
    )
    submitted = st.form_submit_button("Submit")

    if submitted:
        generate_response(text)

