from langchain_community.document_loaders import PyPDFLoader

loader=PyPDFLoader('1984.pdf')

docs=loader.load()
print(len(docs))
print(docs[142].page_content)
print(docs[1].metadata)
