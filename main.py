from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain.agents import create_agent
from tavily import TavilyClient
from langchain.tools import tool
from langchain_core.messages import HumanMessage

load_dotenv()

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool for searching through internet
    Args:
        query: query to search for
    Returns:
        The search result
    """
    print(f"searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI(model="gpt-5")
tools = [search]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 langchain job postings near Austin, TX with descriptions")]})
    print(result)

if __name__ == "__main__":
    main()
