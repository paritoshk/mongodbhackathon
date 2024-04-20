import openai
import os
import fitz  # PyMuPDF

# Configuration for the OpenAI client
client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="ZxMnS0dQqCWmjJHchufihHS1e40Y3aIP92LTeraQYuAyoubW",
)

def extract_title(page_content):
    # Assume the title is the first non-empty line of text
    for line in page_content.split('\n'):
        if line.strip():
            return line.strip()
    return 'Title Not Found'  # Return a default placeholder if no title could be found

def get_embedding(text):
    try:
        response = client.embeddings.create(
            model="thenlper/gte-large",
            input=text
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"An error occurred while fetching the embedding: {e}")
        return None

def read_documents(folder_path):
    document_dict = {}
    embeddings_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            try:
                # Open the PDF file
                doc = fitz.open(file_path)
                # Extract text from the entire document
                full_text = ""
                for page in doc:
                    full_text += page.get_text()
                # Extract text from the first page for the title
                if len(doc) > 0:
                    first_page_text = doc[0].get_text()
                    title = extract_title(first_page_text)
                else:
                    title = "No content"
                    first_page_text = ""
                document_dict[title] = full_text
                # Optionally, get embeddings for the full document text or first page text
                embeddings_dict[title] = get_embedding(full_text)
            except Exception as e:
                print(f"Failed to read {filename}: {str(e)}")
            finally:
                doc.close()  # Ensure the document is closed after processing
    return document_dict, embeddings_dict

# Example usage
folder_path = './data'  # Update with the path to your PDF documents
documents, embeddings = read_documents(folder_path)
for title, content in documents.items():
    print(f"Title: {title}\nContent: {content[:500]}...")  # Print the title and the first 500 characters of the content
    if embeddings[title]:
        print(f"Embedding: {embeddings[title][:10]}...")  # Print the first 10 elements of the embedding