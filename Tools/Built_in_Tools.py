from langchain_community.tools import DuckDuckGoSearchRun

search_tools=DuckDuckGoSearchRun()
results=search_tools.invoke('Gold Price in Nepal today')

print(results)

print(search_tools.name)
print(search_tools.description)
print(search_tools.args)

