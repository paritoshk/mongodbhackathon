import openai
import os
import fitz  # PyMuPDF
from typing import Dict, Tuple, Optional

class DocumentProcessor:
    """
    A class to process PDF documents by extracting text and generating embeddings.

    Attributes:
        client (openai.OpenAI): A client to communicate with OpenAI's API.
        folder_path (str): Path to the directory containing PDF files.
    """
    def __init__(self, base_url: str, api_key: str, folder_path: str):
        """
        Initializes the DocumentProcessor with OpenAI API configuration and the folder path.

        Args:
            base_url (str): The base URL for the OpenAI API.
            api_key (str): The API key for authenticating requests to OpenAI.
            folder_path (str): The local path to the folder containing PDF files.
        """
        self.client = openai.OpenAI(
            base_url=base_url,
            api_key=api_key,
        )
        self.folder_path = folder_path
    def extract_title(self, page_content: str) -> str:
        """
        Extracts the title from the first non-empty line of the PDF page content.

        Args:
            page_content (str): Text content of a PDF page.

        Returns:
            str: The extracted title or a default placeholder if no title is found.
        """
        for line in page_content.split('\n'):
            if line.strip():
                return line.strip()
        return 'Title Not Found'
    def get_embedding(self, text: str) -> Optional[str]:
        """
        Generates an embedding for the given text using OpenAI's API.

        Args:
            text (str): The text to generate an embedding for.

        Returns:
            Optional[str]: The embedding as a string, or None if an error occurs.
        """
        try:
            response = self.client.embeddings.create(
                model="thenlper/gte-large",
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"An error occurred while fetching the embedding: {e}")
            return None
    def read_documents(self) -> Tuple[Dict[str, str], Dict[str, Optional[str]]]:
        """
        Reads all PDF documents in the specified folder, extracting their text and generating embeddings.

        Returns:
            Tuple[Dict[str, str], Dict[str, Optional[str]]]: A tuple containing two dictionaries,
            one with document titles as keys and their text as values, and another with titles
            as keys and their corresponding embeddings as values.
        """
        document_dict = {}
        embeddings_dict = {}
        for filename in os.listdir(self.folder_path):
            if filename.endswith(".pdf"):
                file_path = os.path.join(self.folder_path, filename)
                try:
                    doc = fitz.open(file_path)
                    full_text = ""
                    for page in doc:
                        full_text += page.get_text()
                    first_page_text = doc[0].get_text() if len(doc) > 0 else ""
                    title = self.extract_title(first_page_text)
                    document_dict[title] = full_text
                    embeddings_dict[title] = self.get_embedding(full_text)
                except Exception as e:
                    print(f"Failed to read {filename}: {str(e)}")
                finally:
                    doc.close()
        return document_dict, embeddings_dict
def main():
    """
    Main function to initialize DocumentProcessor and process documents.
    """
    folder_path = './data'
    processor = DocumentProcessor(
        base_url="https://api.fireworks.ai/inference/v1",
        api_key="ZxMnS0dQqCWmjJHchufihHS1e40Y3aIP92LTeraQYuAyoubW",
        folder_path=folder_path
    )
    documents, embeddings = processor.read_documents()
    for title, content in documents.items():
        print(f"Title: {title}\nContent: {content[:500]}...")
        if title in embeddings and embeddings[title]:
            print(f"Embedding: {embeddings[title][:10]}...")
if __name__ == '__main__':
    main()
