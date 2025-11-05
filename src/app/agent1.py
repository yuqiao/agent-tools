import os
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(
    model="qwen3-max",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

tools = load_tools(["serpapi", "llm-math"], llm=chat)


agent = initialize_agent(
    tools, chat, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

if __name__ == "__main__":
    agent.run("What will be the weather in Sheanghai three days from now?")
