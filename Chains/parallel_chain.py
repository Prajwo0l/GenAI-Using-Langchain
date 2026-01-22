from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic

load_dotenv()

model1=ChatOpenAI()
model2=ChatAnthropic()

prompt = PromptTemplate(
    template="Generate a short and simple points  from the following text:\n{text}",
    input_variables=['text']
)
prompt2=PromptTemplate(
    template="Generate five question from the following text:\n{text}",
    input_variables=['text']
)
prompt3=PromptTemplate(
    template='Combine the previous two ouput into a single format:\n{notes} and QA->{qa}',
    input_variables=['notes','qa']
)
parser=StrOutputParser()

parallel_chain=RunnableParallel({
    'notes':prompt|model1|parser,
    'qa':prompt2|model2|parser,
})
merge_chain=parallel_chain|prompt3|model1|parser
chain=parallel_chain|merge_chain
text="LangChain is a framework for developing applications powered by language models. It can be used for chatbots, Generative Question-Answering (GQA), summarization, and much more."
result=chain.invoke({'text':text})
print(result)
