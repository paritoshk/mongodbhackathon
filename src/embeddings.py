import pandas as pd
import json
import numpy as np
import openai

client = openai.OpenAI(
    base_url = "https://api.fireworks.ai/inference/v1",
    api_key="ZxMnS0dQqCWmjJHchufihHS1e40Y3aIP92LTeraQYuAyoubW",
)


def get_embedding(query):
    query_emb = client.embeddings.create(
      model="thenlper/gte-large",
      input=f"{query}"
    )
    return query_emb.data[0].embedding
