from langchain.llms import OpenAI

def langchain_agent():
    llm = OpenAI(temperature=0.5)

    tools = load_tools(['wikipedia', 'll-math'], llm=llm)

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    result = agent.run(
        "what is teh average age of a dog? multiply by 3"
    )

    print(result)

if __name__ == "__main__":
    langchain_agent()
