import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


class LLM:
    def __init__(self, model: str):
        self._model = model
        self.llm = ChatOpenAI(
            model=model,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

    def stream(self, query: str):
        messages = [{"role": "user", "content": f"{query}"}]
        for chunk in self.llm.stream(messages):
            print(chunk.content, end="", flush=True)

    def invoke(self, messages: list):
        return self.llm.invoke(messages)


if __name__ == "__main__":
    template_string = """Thanslate the text that is delimited by 
    triple backtiks into a style that is {style}.
    text: ```{text}``` """
    customer_style = "American English in a calm and respectful tone"
    customer_email = """ Arrr, I be fuming that me blender lid flew off
    and splattered me kitchen walls with smoothie! And to make matters worse,
    the warranty don't cover the cost of cleaning up me kitchen. I need yer help
    right now, matey! """
    template = ChatPromptTemplate.from_template(template_string)
    messages = template.format_messages(style=customer_style, text=customer_email)
    # print(messages)
    llm = LLM("qwen3-max")
    response = llm.invoke(messages)
    print(response)
