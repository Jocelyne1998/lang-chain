from typing import List
from pydantic import BaseModel, Field

from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

class Source(BaseModel):
    """Schema for the source used by the agent"""
    url: str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
    """Schema for the agent response with sources and response"""
    sources: List[Source] = Field(description="List of sources used to generate the response")
    response: str = Field(description="The response from the agent")

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(llm, tools=tools, response_format=AgentResponse)

def main():
    print("Hello from icebreaker!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(result)
if __name__ == "__main__":
    main()

