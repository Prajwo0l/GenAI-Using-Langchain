from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel,RunnableLambda

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
def word_count(text):
    return len(text.split)

joke_gen_chain=RunnableSequence(prompt,model,parser)
parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
}

)
final_chain=RunnableSequence(joke_gen_chain,parallel_chain)
result=final_chain.invoke({'topic':'Life'})

final_result=''''{}\n word count - {}'''.format(result['joke'],result['wrod_Count'])

print(final_result)
