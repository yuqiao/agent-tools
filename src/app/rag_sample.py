from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings  # 导入 Ollama 嵌入类

# 1. 初始化本地 Ollama 嵌入模型
# 指定您刚拉取的模型 "nomic-embed-text"
embeddings = OllamaEmbeddings(
    model="nomic-embed-text",
    base_url="http://localhost:11434",  # 确保与 Ollama 服务地址一致
)

# 2. 您的文档数据
documents = [
    Document(page_content="猫是非常独立的动物。", metadata={"source": "动物百科"}),
    Document(
        page_content="狗是忠诚的伙伴，经常陪伴人类。", metadata={"source": "动物百科"}
    ),
    Document(
        page_content="LangChain是一个用于构建大模型应用的框架。",
        metadata={"source": "技术文档"},
    ),
]

# 3. 创建向量存储时直接使用本地嵌入模型
# 文档会自动通过本地的 Ollama 服务进行向量化
vector_store = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,  # 使用本地嵌入模型
    persist_directory="/tmp/local_ollama_db1",  # 指定本地存储路径
)

# 4. 进行相似性搜索 (体验与之前无异)
query = "什么样的宠物适合当人类伙伴？"
results = vector_store.similarity_search(query, k=2)

for doc in results:
    print(f"内容: {doc.page_content}")
