import pandas as pd
import json
import numpy as np
import openai
from llama_index.core import SimpleDirectoryReader
from pdfplumber import open as open_pdf

# Configuration for the OpenAI client
client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="ZxMnS0dQqCWmjJHchufihHS1e40Y3aIP92LTeraQYuAyoubW",
)

# Function to get embeddings using the API
def get_embedding(query):
    try:
        query_emb = client.embeddings.create(
            model="thenlper/gte-large",
            input=f"{query}"
        )
        return query_emb.data[0].embedding
    except Exception as e:
        print(f"An error occurred while fetching the embedding: {e}")
        return None

# Define a custom PDF reader
class PDFReader:
    def load_data(self, file_path, extra_info=None):
        with open_pdf(file_path) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        return [text]

# Instantiate the directory reader with PDF file support
reader = SimpleDirectoryReader(input_dir="./data", file_extractor={".pdf": PDFReader()})

# Read documents using the custom PDF reader
documents = reader.load_data()

# Get embeddings for each document and handle them as needed
embeddings = [get_embedding(doc) for doc in documents]
# Example of handling embeddings - simply printing them here. You can replace this with database insertion or any other processing.
for embedding in embeddings:
    print(embedding)
