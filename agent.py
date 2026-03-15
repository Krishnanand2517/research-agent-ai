from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent

from tools import search_web
from prompts import SYSTEM_PROMPT
from schema import SearchResult

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)


@tool
def web_search(query: str) -> list[SearchResult]:
    """Search the web for information."""
    return search_web(query)


tools = [web_search]

agent = create_agent(model=llm, tools=tools, system_prompt=SYSTEM_PROMPT)
