import os
import openai
from langchain.llms import AzureOpenAI
from dotenv import load_dotenv
from langchain.llms import AzureOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain


load_dotenv()

openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")

llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
# take inputs from user and return the answer until the user says "bye" or "quit" or "exit"
print("Chatbot: Hi, I am a chatbot. I can help you find vacation destinations in India based on your choice of food and choice of hotels.\n") 

prompt_food = PromptTemplate(
    input_variables=["food"],
    template="What are the 5 vacation destinations for someone who likes {food}?",
)
print("What is your favorite food? (type 'bye' to exit)")
user_input = input("You: ")
if user_input.lower() in ["bye", "quit", "exit"]:
    print("Chatbot: Bye")
# Food chain
chain_food = LLMChain(llm=llm, prompt=prompt_food)
print(chain_food.run(user_input))

#Hotel chain
prompt_hotel_type = PromptTemplate(
    input_variables=["hotel_type"],
    template="does the location has any {hotel_type} hotel?",
)
print("which type of hotel you are looking for? For example, are you interested in a 5-star, 4-star, or another category of hotel? (type 'bye' to exit)")
user_input_hotel_type = input("You: ")
if user_input_hotel_type.lower() in ["bye", "quit", "exit"]:
    print("Chatbot: Bye")
chain_hotel_type = LLMChain(llm=llm, prompt=prompt_hotel_type)
overall_chain = SimpleSequentialChain(chains=[chain_food,chain_hotel_type], verbose=False)

output = overall_chain.run(user_input_hotel_type)
print(output)