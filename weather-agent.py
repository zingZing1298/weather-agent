from langchain_openrouter import ChatOpenRouter
from langchain_core import tools
from dotenv import load_dotenv

load_dotenv()

import os

def get_weather(city:str)-> str:
    """
    Get weather for a given city
    """
    return f"The weather in {city} is sunny with a high of 25°C and a low of 15°C." # DUMMY

tools = [get_weather]

llm = ChatOpenRouter(model="nvidia/nemotron-3-super-120b-a12b:free",temperature=0.1,top_p=0.1)

response = llm.invoke("What is the weather in New York?")
print(response)