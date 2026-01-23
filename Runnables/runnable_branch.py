from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda,RunnableBranch

load_dotenv()

prompt1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variable=['topic']
)
prompt2=PromptTemplate(
    template='Sumaarize the following text.\n{text}',
    input_variables=['text']
)

model=ChatOpenAI()
parser=StrOutputParser()

first_chain=RunnableSequence(prompt1,model,parser)
second_chain=RunnableBranch(
    (lambda x :len(x.split())>500,RunnableSequence(prompt2,model,parser)),
    RunnablePassthrough()

)
final_chain=RunnableSequence(first_chain,second_chain)
print(final_chain.invoke({'topic':'Transformer Model'}))