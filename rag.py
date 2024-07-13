What ra abbas

import getpass
import os

if "HUGGINGFACEHUB_API_TOKEN" not in os.environ:
    os.environ["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"] = getpass.getpass("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")

import requests

url = "https://raw.githubusercontent.com/hwchase17/chat-your-data/master/state_of_the_union.txt"
res = requests.get(url)
with open("state_of_the_union.txt", "w") as f:
  f.write(res.text)
# Document Loader
from langchain.document_loaders import TextLoader
loader = TextLoader('./state_of_the_union.txt')
documents = loader.load()

import textwrap

def wrap_text_preserve_newlines(text, width=110):
    # Split the input text into lines based on newline characters
    lines = text.split('\n')

    # Wrap each line individually
    wrapped_lines = [textwrap.fill(line, width=width) for line in lines]

    # Join the wrapped lines back together using newline characters
    wrapped_text = '\n'.join(wrapped_lines)

    return wrapped_text
print(wrap_text_preserve_newlines(str(documents[0])))
# Text Splitter
from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# Embeddings
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings()
# Vectorstore: https://python.langchain.com/en/latest/modules/indexes/vectorstores.html
from langchain.vectorstores import FAISS

db = FAISS.from_documents(docs, embeddings)
query = "What did the president say about the Supreme Court"
docs = db.similarity_search(query)
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain_community.llms import HuggingFaceEndpoint


llm=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.1, max_length=512)
chain = load_qa_chain(llm, chain_type="stuff")
query = "What did the president say about the Supreme Court"
docs = db.similarity_search(query)
chain.run(input_documents=docs, question=query)
query = "What did the president say about economy?"
docs = db.similarity_search(query)
chain.run(input_documents=docs, question=query)
