from langchain_openai import ChatOpenAI
from langchain_core.tools import tool,InjectedToolArg
from langchain_core.messages import HumanMessage
from typing import Annotated
import requests
import json

@tool
def get_conversion_factor(base_currency:str,target_currency:str)->float:
    '''This Function fetches the currency conversion factor between a given base curreny and a target currency'''
    url=f'https://v6.exchangerate-api.com/b26171241903018253c3dc6e/pair/{base_currency}/{target_currency}'

    response=requests.get(url)
    return response.json()
@tool
def convert(base_currency_value:int,conversion_rate:Annotated[float,InjectedToolArg])->float:
    '''Given a currency conversion rate this function calculates the target currency value from a given base currency value'''
    return base_currency_value*conversion_rate

print(get_conversion_factor.invoke({'base_currency':'USD','target_currency':'INR'}))

convert.invoke({'base_currency_value':10,'conversion_rate':147.01})

#tool Binding
model=ChatOpenAI()
model_tools=model.bind_tools([get_conversion_factor,convert])
messages=[HumanMessage('What is the conversion factor between USD and NPR,and based on that can you concet 10 usd to NPR')]

ai_message=model_tools.invoke(messages)
messages.append(ai_message)

print(ai_message.tool_calls)

for tool_call in ai_message.tool_calls:
    #Execute the first tool and get the value of conversion rate
    if tool_call['name']=='get_conversion_factor':
        tool_message1=get_conversion_factor.invoke(tool_call)
        print(tool_message1)
        #Fetch this conversion rate
        conversion_rate=json.loads(tool_message1.content['conversion_rate'])
        messages.append(tool_message1)
    #Execute the second tool using the conversion rate from tool1
    if tool_call['name']=='convert':
        #fetch the current argument
        tool_call['args']['conversion_rate']=conversion_rate
        tool_messages2=convert.invoke(tool_call)
print(messages)

model_tools.invoke(messages).content
    





