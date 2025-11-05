import os
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory


prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template('''
The following is a friendly conversation between a human and an AI.
The Ai is talkative and provides lots of specific details from its context.
If the Ai does not know the answer to a question, it truthfully says ist does not know.
    '''),
    # MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])


llm = ChatOpenAI(
    model="qwen3-max",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")

memory = ConversationBufferMemory()

conversation = L(prompt=prompt, llm=llm)

if __name__ == '__main__':
    v = conversation.invoke({"input":  "你好, 我是乔云"})
    print(v)