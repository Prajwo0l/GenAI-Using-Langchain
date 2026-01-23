from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path='timezone.csv')
data=loader.lazy_load()
for loop in data:
    print(loop.metadata)
