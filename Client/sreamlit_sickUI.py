import streamlit as st

# Function to ask introductory questions
def ask_intro_questions():
    name = st.text_input("What is your name?")
    age = st.number_input("How old are you?", min_value=0, max_value=150, step=1)
    school_level = st.selectbox("What is your level of school?", ["High School", "College", "Other"])

    return name, age, school_level

# Function for studying something
def study_something():
    topic_to_study = st.text_input("What do you want to study about?")
    st.success(f"You want to study about: {topic_to_study}")

# Function for Q&A interface
# customise the styling
def ask_question():
    with st.chat_message("user"):
         st.write("Hello 👋")
         
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
    
    # user_question = st.text_input("Ask your question:")
    # st.success(f"Your question: {user_question}")

# Function for displaying chatbot response
def display_chatbot_response():
    st.write("Chatbot Response:")
    st.text_area("Type the chatbot response here...")

# Main Streamlit app with multi-step form and input validation
def main():
    st.title("🎒🏫🚸 O-level Ai Tutor")
    st.header("This is an experimental version of our chatbot for teaching ui")

    # Initialize session state to keep track of the current step
    if "step" not in st.session_state:
        st.session_state.step = 1

    # Step 1: Introductory questions
    if st.session_state.step == 1:
        name, age, school_level = ask_intro_questions()

        # Check if all required info is provided before moving to the next step
        if name and age is not None and school_level:
            st.success(f"Hello {name}! You are {age} years old and in {school_level}.")
            st.session_state.step += 1
        else:
            st.warning("Please provide all the required information.")

    # Step 2: Options to ask a question or study something using buttons
    elif st.session_state.step == 2:
        st.write("Choose an option:")
        if st.button("Ask a question"):
            st.session_state.step += 1
        if st.button("Study something"):
            st.session_state.step += 2

    # Step 3: Ask a question
    elif st.session_state.step == 3:
        ask_question()
        display_chatbot_response()
        st.session_state.step += 1

    # Step 4: Study something
    elif st.session_state.step == 4:
        study_something()
        st.session_state.step += 1

if __name__ == "__main__":
    main()
