from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Function to load PDF files from a directory
def load_pdf_file(data):
    loader=DirectoryLoader(data,glob="*.pdf",
                          loader_cls=PyPDFLoader)
    documents=loader.load()

    return documents

# Function to split documents into smaller chunks
def text_split(extracted_data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20,
    )
    text_chunks = text_splitter.split_documents(extracted_data)

    return text_chunks

def download_embeddings():
    # Load the HuggingFace embeddings model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
    )
    return embeddings