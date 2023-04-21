import os
import openai
from dotenv import load_dotenv
# from langchain.chat_models import AzureChatOpenAI
from langchain.llms import AzureOpenAI


load_dotenv()

# print(os.environ.get("OPENAI_API_TYPE"))
openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")

llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
# take inputs from user and return the answer until the user says "bye" or "quit" or "exit"
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "quit", "exit"]:
        print("Chatbot: Bye")
        break
    else:
        print("Chatbot: ", llm(user_input))
