import os
import openai
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


load_dotenv()

openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")

llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
# take inputs from user and return the answer until the user says "bye" or "quit" or "exit"
prompt = PromptTemplate(
    input_variables=["food"],
    template="What are the 5 vacation destinations for someone in India who likes {food}?",
)
print("Chatbot: Hi, I am a chatbot. I can help you find vacation destinations in India based on your choice of food and Fruit.\n") 
print("What is your favorite food? (type 'bye' to exit)")
user_input = input("You: ")
if user_input.lower() in ["bye", "quit", "exit"]:
    print("Chatbot: Bye")
chain = LLMChain(llm=llm, prompt=prompt)
print(chain.run(user_input))