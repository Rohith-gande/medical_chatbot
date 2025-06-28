🩺 Medical Chatbot using Gemini + LangChain + Pinecone
A conversational medical assistant built with Gemini 2.0 Flash (via LangChain) for answering health-related questions using RAG (Retrieval-Augmented Generation). Includes a clean chat-style UI like ChatGPT.

🚀 Features
🤖 Conversational interface powered by Gemini Flash

📚 Retrieval-augmented responses from uploaded medical documents

🔎 Pinecone vector store for fast semantic search

🧠 LangChain chains for document parsing and QA

💬 ChatGPT-style frontend built using HTML, CSS, Bootstrap

🔐 API key management using .env

🛠️ Tech Stack
Python 3.10

langchain, langchain-community, langchain-google-genai

sentence-transformers, transformers, torch

pinecone-client, flask

dotenv, pypdf, bootstrap

⚙️ Setup Instructions
1. Clone the repo & setup Python 3.10 environment
   
git clone <repo_url>
cd medical_chatbot
python3.10 -m venv env
source env/bin/activate  # Or `env\Scripts\activate` on Windows


2. Install dependencies

pip install -r requirements.txt
Make sure to use these compatible versions:


sentence-transformers==2.2.2
huggingface-hub==0.14.1
transformers==4.29.2
torch==2.0.1
pinecone-client==3.2.0
langchain==0.1.16
langchain-community==0.0.34
langchain-openai==0.0.8
langchain-pinecone==0.0.3
langchain-experimental==0.0.11
flask==3.0.2
pypdf==3.17.4
python-dotenv==1.0.1
🔐 Set up .env file
Create a .env file in your root directory:

GEMINI_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key

💡 How it Works
You upload or load medical documents into Pinecone vector store.

When a user asks a question, LangChain fetches the most relevant chunks.

Gemini 2.0 Flash answers the question using the retrieved context.

The frontend sends input to the Flask API and shows the output.

🧪 Run Locally
python app.py
Then open chat.html in your browser to start chatting.

✨ Sample Question
Q: What is the treatment for acne?

A: Acne can be treated with topical medications like benzoyl peroxide or salicylic acid. Oral antibiotics may also be used for more severe cases. Maintaining skin hygiene is important.

📌 Future Improvements
Add speech-to-text input

Deploy with Docker + Streamlit or Gradio

Add user authentication

📜 License
MIT License. Open for learning and contribution.
