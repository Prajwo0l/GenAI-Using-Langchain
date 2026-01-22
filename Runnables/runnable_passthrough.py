from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel

load_dotenv()

prompt=PromptTemplate(
    template='Write a joke about {topic}.',
    input_variables=['topic']
)
prompt2=PromptTemplate(
    template='Write a detailed Explanation of following joke{text}',
    input_variable=['text']
)
model=ChatOpenAI()
parser=StrOutputParser()
joke_gen_chain=RunnableSequence(prompt,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explaination':RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
print(final_chain.invoke({'topic':'AI'}))
