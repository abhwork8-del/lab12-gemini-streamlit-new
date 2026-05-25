import streamlit as st
import google.generativeai as genai

st.set_page_config(
    page_title="Lab 12 Gemini",
    page_icon="🤖"
)

st.title("🤖 AI Lab 12")

api_key = st.text_input(
    "Enter Gemini API Key",
    type="password"
)

if api_key:

    try:
        genai.configure(api_key=api_key)

        model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

        prompt = st.text_area(
            "Ask something"
        )

        if st.button("Generate"):

            if prompt:

                response = model.generate_content(
                    prompt
                )

                st.write(response.text)

    except Exception as e:
        st.error(str(e))

else:
    st.info("Enter Gemini API Key")
