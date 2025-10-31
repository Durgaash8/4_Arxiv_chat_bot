import sys
import os

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st
from src.rag_chatbot import RagChatbot
from src.faiss_indexer import Retriever

st.set_page_config(page_title="ArXiv CS Chatbot", layout="wide")
st.title("ArXiv-CS Expert Chatbot")

# Initialize
@st.cache_resource
def get_bot():
    bot = RagChatbot(generator=None)  # attach generator wrapper if available
    return bot

bot = get_bot()
with st.sidebar:
    st.markdown("## Search papers")
    q = st.text_input("Search / Ask about concept", value="")
    top_k = st.slider("Top-k retrieved", 1, 10, 5)

if q:
    with st.spinner("Retrieving..."):
        context, hits = bot.make_context(q, top_k=top_k)
    st.subheader("Top retrieved excerpts")
    for i,h in enumerate(hits):
        st.write(f"**{i+1}. {h['title']}** (score: {h['score']:.3f})")
        st.write(h['text'][:800] + ("..." if len(h['text'])>800 else ""))
    st.subheader("Answer / Explanation")
    answer = bot.answer(q, top_k=top_k)
    st.write(answer)
    st.subheader("Follow-up")
    # A very simple chat simulation: user types follow-up and we re-call answer with conversation appended
    follow = st.text_input("Ask follow-up", key="follow")
    if follow:
        combined = q + " Follow-up: " + follow
        st.write(bot.answer(combined, top_k=top_k)) 
