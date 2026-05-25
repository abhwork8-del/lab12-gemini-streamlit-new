import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Lab 12")

api_key = st.text_input(
    "Enter Gemini API Key",
    type="password"
)

if api_key:

    genai.configure(
        api_key=api_key
    )

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

    prompt = st.text_area(
        "Enter Prompt"
    )

    if st.button("Generate"):

        if prompt:

            response = model.generate_content(
                prompt
            )

            st.write(response.text)

else:
    st.warning("Enter Gemini API Key")
