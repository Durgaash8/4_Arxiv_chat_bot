
# src/rag_chatbot.py
from src.faiss_indexer import Retriever

# For generation, use an open-source model via HuggingFace transformers (or use local llama wrapper).
# Here I show an interface; implement model loading per your environment.

class RagChatbot:
    def __init__(self, generator=None):
        self.ret = Retriever()
        self.generator = generator  # function that accepts (prompt, context) -> text

    def make_context(self, query, top_k=5):
        hits = self.ret.query(query, top_k=top_k)
        context = "\n\n".join([f"Title: {h['title']}\nText: {h['text']}" for h in hits])
        return context, hits

    def answer(self, query, top_k=5):
        context, hits = self.make_context(query, top_k)
        prompt = f"""You are an expert in computer science research. A user asks: "{query}"
Use the following retrieved excerpts from arXiv papers to answer the question. Cite titles when helpful.
Context:
{context}

Answer concisely but in depth. If the answer references a paper, mention the paper title.
"""
        if self.generator:
            return self.generator(prompt)
        else:
            # fallback short answer
            return "Generator not configured. Retrieved passages:\n\n" + context

if __name__ == "__main__":
    print("Chatbot is running...")
