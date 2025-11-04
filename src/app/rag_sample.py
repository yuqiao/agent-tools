"""Sample RAG implementation."""


def retrieve_relevant_docs(query):
    """Retrieve relevant documents for the query."""
    print(f"Retrieving docs for query: {query}")
    return ["doc1", "doc2"]


def generate_response(query, docs):
    """Generate response based on query and docs."""
    print(f"Generating response with docs: {docs}")
    return f"Response for {query}"