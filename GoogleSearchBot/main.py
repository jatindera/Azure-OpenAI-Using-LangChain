from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import AzureOpenAI
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_type = os.environ.get("OPENAI_API_TYPE")
openai.api_key = os.environ.get("OPENAI_API_KEY")
openai.api_base = os.environ.get("OPENAI_API_BASE")
openai.api_version = os.environ.get("OPENAI_API_VERSION")
openai.serpapi_api_key = os.environ.get("SERPAPI_API_KEY")

# https://serpapi.com/manage-api-key
llm = AzureOpenAI(deployment_name="text-davinci-003", model_name="text-davinci-003")
print(llm)
tools = load_tools(["serpapi", "llm-math"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
agent.run("which date Navjot singh sidhu was released in 2023 and which day of week.")