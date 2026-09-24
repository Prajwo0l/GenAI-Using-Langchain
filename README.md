# GenAI-Using-Langchain

Small, focused scripts and notebooks working through LangChain's core
building blocks one concept at a time.

## ⚠️ Before using this repo

`Currency_Converter.py` has a live ExchangeRate-API key hardcoded
directly in the request URL, committed in plaintext to this public repo.
Rotate that key and move it to an environment variable before relying on
this script further.

## What's covered

| Folder | Topic |
|---|---|
| [`Chains`](Chains) | Simple and parallel chains |
| [`Runnables`](Runnables) | The Runnable primitives — sequences, parallel, branch, lambda, passthrough |
| [`Document Loader`](Document%20Loader) | Loading from CSV, PDF, plain text, a directory, and the web |
| [`Text Splitters`](Text%20Splitters) | Length-based, recursive-character, semantic-meaning-based, and code-aware splitting |
| [`Retrievers`](Retrievers) | Vector-store retrievers and contextual compression |
| [`Vector Store`](Vector%20Store) | Chroma as a vector store |
| [`Tools`](Tools) | Base tools, built-in tools, custom tools, structured tools, and tool calling |

`Currency_Converter.py` is a standalone example combining a custom tool
(exchange-rate lookup) with `InjectedToolArg` for a two-step
currency-conversion tool call.

## Setup

```bash
pip install -r requirements.txt
```

Most examples need `OPENAI_API_KEY` set in your environment; the currency
converter additionally needs its own ExchangeRate-API key (see the
warning above — don't hardcode it).
