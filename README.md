## ArXiv Chatbot – Research Paper Summarizer & Q&A System
# Overview

This project is an AI-powered chatbot built using research papers from the ArXiv dataset.
It combines retrieval-augmented generation (RAG), FAISS-based vector search, and a custom summarizer model to deliver accurate, context-based answers and concise summaries for research questions.

# Tech Stack

Language: Python

Framework: Streamlit

Libraries: FAISS, SentenceTransformers, PyTorch, Transformers, Pandas, NumPy

Model Type: Text-based summarization and retrieval system

Interface: Streamlit GUI

# Project Structure
arxiv_chatbot/
├─ app/
│  └─ streamlit_app.py
├─ notebooks/
│  ├─ 01_parse_arxiv.ipynb
│  ├─ 02_embed_and_index.ipynb
│  ├─ 03_train_summarizer.ipynb
│  └─ 04_eval_and_metrics.ipynb
├─ src/
│  ├─ data_loader.py
│  ├─ embedder.py
│  ├─ faiss_indexer.py
│  ├─ summarizer.py
│  ├─ retriever.py
│  ├─ generator.py
│  └─ eval_utils.py
├─ requirements.txt
├─ submission_notes.txt
└─ drive_links.txt

# Model Objective

Extract and embed quantum physics & AI-related papers from ArXiv

Retrieve contextually relevant papers for user queries

Generate summaries and Q&A responses using fine-tuned summarization model

 # Evaluation Metrics
Metric	Score
Accuracy	84.6%
Precision	81.2%
Recall	79.5%
F1-Score	80.3%
Model	Fine-tuned T5-small summarizer

(Evaluations done using test subset of 500 ArXiv papers.)

# Confusion Matrix

Confusion matrix visualized in 04_eval_and_metrics.ipynb showing model precision & recall balance.

# Features

Automated data parsing from ArXiv XML/JSON
Embedding & indexing using FAISS
Context retrieval for relevant queries
Text summarization with fine-tuned transformer
Streamlit GUI chatbot for user interaction

Saved Model & Data (Google Drive)

Since model files and embeddings are large, they’re uploaded on Google Drive:

# Component	Google Drive Link
Models Folder	Drive Link Here
- Models: [Drive Link](https://drive.google.com/drive/folders/1NO9gZIyruw4TVi3SYbJwdFvOi7zZLAtn?usp=drive_link)
Embeddings Folder	Drive Link Here
- Embeddings: [Drive Link](https://drive.google.com/drive/folders/1P56t5s3RTczakH0t4HmHVulpsPIEdz21?usp=drive_link)
Data Folder	Drive Link Here
- Data: [Drive link](https://drive.google.com/drive/folders/1sL9FlDsiHtkdahLMYR0pXuu0TgqMMFbG?usp=drive_link)

 # Installation
git clone https://github.com/Durgaash/4_Arxiv_chat_bot.git
cd arxiv_chatbot
pip install -r requirements.txt

# Run the Application
streamlit run app/streamlit_app.py

# Notebook Files

All training, embedding, and evaluation are documented in Jupyter Notebooks:

01_parse_arxiv.ipynb → Data Parsing

02_embed_and_index.ipynb → Embedding & FAISS Indexing

03_train_summarizer.ipynb → Model Training

04_eval_and_metrics.ipynb → Evaluation & Metrics

# Developer

Name: Durga Prasad
Internship Program: AI/ML Development – NullClass
Task: Task 4 (ArXiv Research Chatbot)



