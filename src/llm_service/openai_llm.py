"""
LLM Script Oriented to using OpenAI structure
"""

import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM

# Load environment variables
load_dotenv()
MODEL = os.getenv("LLAMA_MODEL")

# Load Model
llm = OllamaLLM(model= MODEL)

response = llm.invoke("The first man on the moon was ...")
print(response)
