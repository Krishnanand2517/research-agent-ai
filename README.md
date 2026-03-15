# Research Agent
 
A simple AI-powered research assistant that answers questions by searching the web in real time. Ask it anything and it will query DuckDuckGo, analyze the results, and return a concise, cited summary.

## How it works
 
1. You type a research question in the terminal.
2. The agent calls a `web_search` tool (backed by DuckDuckGo) to gather relevant results.
3. GPT-4.1-mini analyzes the results and produces a summary with source URLs.
4. The response streams to your terminal token by token.

## Tech stack
 
- **[LangChain](https://www.langchain.com)**: agent framework and tool orchestration
- **[LangGraph](https://www.langchain.com/langgraph)**: stateful agent execution and streaming
- **[OpenAI GPT-4.1-mini](https://developers.openai.com/api/docs/models/gpt-4.1-mini)**: the underlying LLM
- **[ddgs](https://github.com/deedy5/ddgs)**: search client for web lookups

## Requirements
 
- Python 3.12+
- An OpenAI API key
 
## Setup
 
1. Clone or unzip the project.
 
2. Install dependencies with [uv](https://docs.astral.sh/uv):
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   pip install .
   ```
 
3. Add your OpenAI API key to `.env`:
   ```
   OPENAI_API_KEY=your-key-here
   ```

## Usage
 
```bash
python main.py
```
 
Then enter any research question at the prompt:
 
```
Ask a research question (or 'exit'): What are the latest developments in fusion energy?
```
 
Type `exit` to quit.