from langchain_core.tools import tool

#Firstly create a function
def multiply(a,b):
    "Multiply two numbers"
    return a*b

#Secondly Add type hints
def multiply(a:int,b:int)->int:
    "Multiply two numbers"
    return a*b

#Thirdly Add a tool Decorater
@tool
def multiply(a:int,b:int)->int:
    "Multiply two numbers"
    return a*b

result=multiply.invoke({"a":5,"b":5})
print(result)



