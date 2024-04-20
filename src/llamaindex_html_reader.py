import logging
import sys

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display
import os

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

documents = SimpleWebPageReader(html_to_text=True).load_data(
    ["https://legiscan.com/CA/text/SB532/id/2832404/California-2023-SB532-Amended.html"]
)
