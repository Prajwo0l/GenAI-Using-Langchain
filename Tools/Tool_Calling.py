from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests

@tool
def multiply(a:int,b:int):
    '''Given two number a and b this tool returns their product'''
    return a * b
print(multiply.invoke({'a':5,'b':5}))
print(multiply.description())

model=ChatOpenAI

llm_tool=model.bind_tools([multiply])

