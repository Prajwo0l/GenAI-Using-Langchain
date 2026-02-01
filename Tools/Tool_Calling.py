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
llm_tool.invoke('Can you help me!')

query=HumanMessage('Can you multiply 3 with 10')
messages=[query]
result=llm_tool.invoke(messages)
messages.append(result)
print(result.tool_calls[0]['args'])

tool_result=multiply.invoke(result.tool_calls[0])
messages.append(tool_result)

final_result=llm_tool.invoke(messages).content
print(final_result)