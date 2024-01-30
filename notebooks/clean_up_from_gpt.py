from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI
from langchain_community.tools import WikipediaQueryRun, YouTubeSearchTool
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain_community.utilities import SerpAPIWrapper

import os

os.environ['OPENAI_API_KEY'] = "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"
os.environ['SERPAPI_API_KEY'] = "e1ae793a2b03140d73f9efb132ad50d0569b02cb9ffa7a85b8a88da2fcc6e8ca"

def load_language_model_and_tools():
    """Load language model and necessary tools."""
    llm = OpenAI(temperature=0.1)
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    return llm, tools

def load_learning_materials(directory_path):
    """Load learning materials from the specified directory."""
    loader = DirectoryLoader(directory_path, glob='**/*.txt')
    documents = loader.load()
    return documents

def setup_retrieval_qa(documents):
    """Set up the RetrievalQA system."""
    # Get text splitter ready
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    # Split documents into texts
    texts = text_splitter.split_documents(documents)

    # Turn texts into embeddings
    embeddings = OpenAIEmbeddings()

    # Get docsearch ready
    docsearch = FAISS.from_documents(texts, embeddings)

    # Load up LLM
    llm = OpenAI()

    # Create Retriever
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=docsearch.as_retriever())

    return qa

def generate_questions_and_answers(query, llm, tools):
    """Generate questions and answers based on the provided query."""
    # Initialize AgentExecutor
    agent_executor = initialize_agent(tools, llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    agent_executor.handle_parsing_errors = True
    
    # Run the query
    agent_executor.run(query)

def provide_explanation(query, llm, tools, qa):
    """Provide an explanation based on the provided query."""
    # Set up tools for additional depth
    wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100))
    youtube_tool = YouTubeSearchTool()
    google_search_wrapper = GoogleSearchAPIWrapper()
    
    # Run tools to gather additional information
    wikipedia_result = wikipedia_tool.run(query)
    youtube_result = youtube_tool.run(query)
    google_search_result = google_search_wrapper.run(query)
    
    # Run a query using the RetrievalQA system
    qa.run(query)
    
    # Print or process the results as needed
    print("Wikipedia Result:", wikipedia_result)
    print("YouTube Result:", youtube_result)
    print("Google Search Result:", google_search_result)

def main(topic):
    """Main function to demonstrate how to use the two functions."""
    learning_materials_directory = '/content/drive/MyDrive/FYP_Training_data'
    
    # Load learning materials
    documents = load_learning_materials(learning_materials_directory)
    
    # Set up the RetrievalQA system
    qa = setup_retrieval_qa(documents)
    
    llm, tools = load_language_model_and_tools()
    
    # Example usage of the generate_questions_and_answers function
    generate_questions_and_answers("what is" + topic, llm, tools)

    print('')
    print('')
    print('------------------   WHEN YOU TRY TO LEARN ABOUT SOMETHING   ------------------')
    print('')
    print('')

    # Example usage of the provide_explanation function
    provide_explanation("teach me about life skills" + topic, llm, tools, qa)

if __name__ == "__main__":
    main("life skills")
