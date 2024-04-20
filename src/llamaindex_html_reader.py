import logging
import sys
from typing import List

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display
import os

def setup_logging():
    """
    Configures the logging system to output to standard output at the INFO level.
    """
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler(stream=sys.stdout))

def load_web_documents(urls: List[str]) -> List[dict]:
    """
    Loads and converts web page content from specified URLs into text documents.

    Args:
        urls (List[str]): A list of URLs from which to load web pages.

    Returns:
        List[dict]: A list of dictionaries containing document data.
    """
    reader = SimpleWebPageReader(html_to_text=True)
    documents = reader.load_data(urls)
    return documents

# Example usage
if __name__ == "__main__":
    setup_logging()
    urls = [
        "https://legiscan.com/CA/text/SB532/id/2832404/California-2023-SB532-Amended.html"
    ]
    documents = load_web_documents(urls)
    for doc in documents:
        display(Markdown(doc['text']))  # Assuming 'text' is the key in the dict containing the content
