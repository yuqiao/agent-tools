import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    FewShotPromptTemplate,
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

chat = ChatOpenAI(
    model="qwen3-max",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

template = (
    "You are a helpful assistant that translate {input_language} to {output_language}."
)
system_message_prompt = SystemMessagePromptTemplate.from_template(template)

human_template = "{text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

chain = chat_prompt | chat

if __name__ == "__main__":
    v = chain.invoke(
        dict(
            input_language="English",
            output_language="French",
            text="I love programming.",
        )
    )
    print(v)
