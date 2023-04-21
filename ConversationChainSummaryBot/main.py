from langchain.llms import AzureOpenAI
from langchain import ConversationChain
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")

llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
conversation = ConversationChain(llm=llm, verbose=True)
while True:
    user_input = input("Enter your message: ")
    if(user_input in ["exit", "quit", "bye"]):
        break
    # wait to get response from following code
    res = conversation.predict(input=user_input)
    print(res)
    # Ask it to generate summary in the end