import os
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
)
from langchain.schema.output_parser import StrOutputParser

chat = ChatOpenAI(
    model="qwen3-max",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

chat_prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")

chain = chat_prompt | chat | StrOutputParser()

if __name__ == '__main__':
    v = chain.invoke({"topic" : "bears"})
    print(v)
