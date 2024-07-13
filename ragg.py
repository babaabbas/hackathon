import os
from langchain_community.document_loaders import TextLoader


os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
loader = TextLoader('/Users/abbasbaba/PycharmProjects/hackathon/abs.txt')
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


from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings()

from langchain.vectorstores import FAISS

db = FAISS.from_documents(docs, embeddings)
print(wrap_text_preserve_newlines(str(docs[0].page_content)))
query = "who is speaking here"
docs = db.similarity_search(query)
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub
from langchain_community.llms import HuggingFaceEndpoint

llm=HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2", temperature=0.1, max_length=512)
chain = load_qa_chain(llm, chain_type="stuff")
query = "what is this"
docs = db.similarity_search(query)
result=chain.run({"input_documents":docs, "question":query})
print(result)
def query_answer(query):
    result = chain.run({"input_documents": docs, "question": query})
    return result




