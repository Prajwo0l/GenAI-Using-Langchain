from langchain_text_splitters import CharacterTextSplitter   
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('1984.pdf')

docs=loader.load()



spliter=CharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0,
    separator=''
)

result=spliter.split_documents(docs)

print(result[10].page_content)