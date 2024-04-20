import pandas as pd
import json
import numpy as np
import openai
from typing import Any

# Configuration for the OpenAI client
client = openai.OpenAI(
    base_url="https://api.fireworks.ai/inference/v1",
    api_key="ZxMnS0dQqCWmjJHchufihHS1e40Y3aIP92LTeraQYuAyoubW",
)

def get_embedding(query: str) -> Any:
    """
    Retrieves the text embedding for a given query using a specified model from the OpenAI API.

    Args:
        query (str): The text input for which the embedding needs to be generated.

    Returns:
        Any: The embedding of the query as a list (usually a list of floats). The return type
             is kept generic (`Any`) as the structure depends on the model used and API response.
    """
    query_emb = client.embeddings.create(
        model="thenlper/gte-large",
        input=f"{query}"
    )
    return query_emb.data[0].embedding

# Example usage
if __name__ == "__main__":
    # Example query for testing
    test_query = "Example text for generating embeddings."
    embedding = get_embedding(test_query)
    print("Generated Embedding:", embedding)
