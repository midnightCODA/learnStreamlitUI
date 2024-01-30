import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from dotenv import load_dotenv

load_dotenv()


def teach_me_about(subject, topic, openai_api_key):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

    prompt_template_name = PromptTemplate(
        input_variables = ['topic', 'subject'],
        template = "I am a 15 year old, o-level student in Tanzania. Teach me about a topic of {topic} from the {subject}. give me relevant examples where neccesary  "
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="answers")

    response = name_chain({'topic': topic, 'subject': subject})


    return response

if __name__ == "__main__":
    print(teach_me_about("15", "Chemical Bonds", "Chemistry"))