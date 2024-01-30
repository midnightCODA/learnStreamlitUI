import streamlit as st
import langchain_helper as lch

st.title("🎒 O-level Student teacher")

st.header('can i get moving please')

subject = st.sidebar.selectbox("What do you want to study subject?", ("Chemistry", "biology", "physiscs", "history", "civics"))

if subject == "Chemistry":
  topic = st.sidebar.selectbox(
    "What topic do you want to study?",
    ("Oxygen", "Fire", "Chemical bonds")
    )

if subject == "biology":
  topic = st.sidebar.selectbox(
    "What topic do you want to study?",
    ("classification", "skeleton")
    )

if subject == "physiscs":
  topic = st.sidebar.selectbox(
    "What topic do you want to study?",
    ("Laws of floatation", "Pressure")
    )


if subject == "civics":
  topic = st.sidebar.selectbox(
    "What topic do you want to study?",
    ("citizenship", "life skills")
    )

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="langchain_search_api_key_openai", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/rishabkumar7/pets-name-langchain/tree/main)"

if topic:
    if not openai_api_key:
      st.info("Please add your OpenAI API key to continue.")
      st.stop()
    response = lch.teach_me_about(subject, topic, openai_api_key)
    st.text(response['pet_name'])