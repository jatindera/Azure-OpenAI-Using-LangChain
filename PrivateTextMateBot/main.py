import os
import openai
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings

from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.text_splitter import TokenTextSplitter

from langchain.vectorstores import FAISS

from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

load_dotenv()

# print(os.environ.get("OPENAI_API_TYPE"))
openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")

# Initialize gpt-35-turbo and our embedding model
llm = AzureChatOpenAI(deployment_name="gpt-35-turbo", openai_api_version=os.environ.get("OPENAI_API_VERSION"))
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", chunk_size=1)

loader = DirectoryLoader('D:/rasp-gpt/PrivateTextMateBot/data/qna/', glob="*.txt", loader_cls=TextLoader)
documents = loader.load()
text_splitter = TokenTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
print(docs)

db = FAISS.from_documents(documents=docs, embedding=embeddings)

# Adapt if needed
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template("""Given the following conversation and a follow up 
question, rephrase the follow up question to be a standalone question.
Chat History:
{chat_history}
Follow Up Input: {question}
Standalone question:""")

qa = ConversationalRetrievalChain.from_llm(llm=llm,
                                           retriever=db.as_retriever(),
                                           condense_question_prompt=CONDENSE_QUESTION_PROMPT,
                                           return_source_documents=True,
                                           verbose=False)

chat_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "quit", "exit"]:
        print("Chatbot: Bye")
        break
    else:
        result = qa({"question": user_input, "chat_history": chat_history})
        print("Question:", user_input)
        print("Answer:", result["answer"])

