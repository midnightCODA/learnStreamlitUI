import streamlit as st
from streamlit.proto.NumberInput_pb2 import NumberInput

# Function to ask introductory questions
def ask_intro_questions():
    name = st.text_input("What is your name?")
    age = st.number_input("How old are you?", min_value=0, max_value=150, step=1)
    school_level = st.selectbox("What is your level of school?", ["High School", "College", "Other"])

    return name, age, school_level

# Function for studying something
def study_something():
    topic_to_study = st.text_area("What do you want to study about?")
    st.success(f"You want to study about: {topic_to_study}")

# Function for Q&A interface
def ask_question():
    user_question = st.text_area("Ask your question:")
    st.success(f"Your question: {user_question}")

# Main Streamlit app with multi-step form
def main():
    st.title("🎒 O-level AI teacher")

    # Initialize session state to keep track of the current step
    if "step" not in st.session_state:
        st.session_state.step = 1

    # Introductory questions (Step 1)
    if st.session_state.step == 1:
        name, age, school_level = ask_intro_questions()
        st.success(f"Hello {name}! You are {age} years old and in {school_level}.")
        st.session_state.step += 1

    # Options to ask a question or study something (Step 2)
    elif st.session_state.step == 2:
        option = st.radio("Choose an option:", ["Ask a question", "Study something"])

        if option == "Ask a question":
            ask_question()
        elif option == "Study something":
            study_something()
        
        st.session_state.step += 1

if __name__ == "__main__":
    main()
