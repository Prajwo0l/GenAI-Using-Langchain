from langchain_text_splitters import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

# Initialize embeddings (local, no API key)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

text = """
Python is a popular programming language used for data science and machine learning.
It has a simple syntax and a large ecosystem of libraries.

Cars are a common mode of transportation.
They usually run on gasoline or electricity.

Deep learning models use neural networks with many layers.
Transformers rely on self-attention mechanisms.
"""

# Create the semantic chunker
chunker = SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="percentile",  # common + intuitive
    breakpoint_threshold_amount=95
)

# Split text
chunks = chunker.split_text(text)

# Inspect results
print(f"Number of chunks: {len(chunks)}\n")
for i, chunk in enumerate(chunks, 1):
    print(f"--- Chunk {i} ---")
    print(chunk)
    print()
