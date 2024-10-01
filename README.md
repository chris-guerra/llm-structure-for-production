# llm-structure-for-production
This is complete guide (in progress...) for creating LLMs ready for production, including connecting to llm APIs, good prompting tecniques, langchain, lama-index, OpenAI assistants, managing outputs (output parser), knowledge graphs, RAG, indexes & retrievers, data ingestion, retrievers, embeddings, chains, fine-tunning, metrics, autogpt and deployment.

- [Installation](#installation)
- [Usage](#jupyter-notebook-lessons)

## Installation

1. Open the terminal in your prefered code editor (I use Visual Studio Code)
2. Clone the repository:
    git clone https://github.com/chris-guerra/llm-structure-for-production.git
3. Create virtual environment:
    python3 -m venv .venv
4. Activate virtual environment:
    source .venv/bin/activate
5. Install requirements:
    pip install -r requirements.txt
6. Create your environment variables:
    touch .env
7. Go into OpenAI, create an account and a key
8. Open the .env file and add the following:
    OPENAI_API_KEY = "<PASTE_YOUR_OPENAI_API_KEY>"


## Jupyter Notebook Lessons

1. **[Introduction to Prompting:](jupyter-notebooks/1-introduction-to-prompting.ipynb)introduction-to-prompting:** Lessons on how to connect to API, prompting tecniques and good & bad prompting
2. **[Introduction to LangChain and Llama Index:](jupyter-notebooks/2-introduction-to-langchain-and-llama-index.ipynb):** ...