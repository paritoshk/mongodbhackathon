import pymongo
import time
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.agent.openai import OpenAIAgent
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, Settings
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.llms.mistralai import MistralAI
from transformers import AutoTokenizer

def get_mongo_client(mongo_uri):
  """Establish connection to the MongoDB."""
  try:
    client = pymongo.MongoClient(mongo_uri)
    print("Connection to MongoDB successful")
    return client
  except pymongo.errors.ConnectionFailure as e:
    print(f"Connection failed: {e}")
    return None

def query(text):
  mongo_uri = os.environ["MONGO_URI"]

  if not mongo_uri:
    print("MONGO_URI not set in environment variables")

  mongo_client = get_mongo_client(mongo_uri)

  DB_NAME = "pdf"
  COLLECTION_NAME = "bills"

  db = mongo_client[DB_NAME]
  collection = db[COLLECTION_NAME]

  # collection.delete_many({})

  # Load documents
  documents = SimpleDirectoryReader("/Users/kawaitsoi/Desktop/Desktop - KA’s MacBook Pro/mdb-hack/data").load_data()

  embed_model = OpenAIEmbedding(
              model = "thenlper/gte-large",
              api_base="https://api.fireworks.ai/inference/v1",
              api_key="ZxMnS0dQqCWmjJHchufihHS1e40Y3aIP92LTeraQYuAyoubW",
              embed_batch_size=100
          )

  Settings.embed_model = embed_model

  llm = MistralAI(model="mistral-large-latest", temperature=0.1, api_key=os.environ["MISTRAL_API_KEY"])

  Settings.llm = llm

  atlas_vector_search = MongoDBAtlasVectorSearch(
      mongo_client,
      db_name = DB_NAME,
      collection_name = COLLECTION_NAME,
      index_name = "vector_index",
      embedding_key="embedding"
  )
  # vector_store_context = StorageContext.from_defaults(vector_store=atlas_vector_search)

  # vector_store_index = VectorStoreIndex.from_documents(
  #    documents, storage_context=vector_store_context, show_progress=True
  # )

  vector_store_index = VectorStoreIndex.from_vector_store(vector_store=atlas_vector_search)

  response = vector_store_index.as_query_engine().query(text)
  print(response)
  return response

def agent():
  llm = MistralAI(model="mistral-large-latest", temperature=0.1, api_key=os.environ["MISTRAL_API_KEY"])