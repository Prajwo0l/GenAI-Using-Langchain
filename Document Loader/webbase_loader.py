from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader   
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
url='https://www.olizstore.com/product/apple-macbook-air-m4-price-in-nepal'
loader=WebBaseLoader(url)
model=ChatOpenAI()

prompt=PromptTemplate(
    template='Answer the following question. \n{question} from the following text-\n{text}',
    input_variables=['question','text']
)
parser=StrOutputParser()
docs=loader.load()

chain=prompt|model|parser

print(chain.invoke({'question':'What is the specs of this Laptop.','text':docs[0].page_content}))

