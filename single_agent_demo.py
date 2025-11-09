import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

search_tool = SerperDevTool()

def create_research_agent():
    
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    # CrewAI works in this way, and these are the parameters to create an agent.
    return Agent(
        role = "Research Assistant",
        goal = "Conduct thorough research on given topics",
        backstory = "You are an experienced researcher with expertise in finding and synthesizing information from various sources",
        verbose=True,           # Seeing execution logs in the terminal
        allow_delegation=False, # single agent, not creating multiagent, after this we do not have other agents
        tools=[search_tool],    # SerperDev search tool
        llm=llm,
    )

# Define the task for the agent
def create_research_task(agent, topic):
    return Task(
        description=f"Research the following topic and provide a comprehensive summary: {topic}",
        agent=agent,
        expected_output="A detailed summary of the research findings, including key points and insights related to the topic"
    )

def run_research(topic):
    agent = create_research_agent()
    task = create_research_task(agent, topic)
    crew = Crew(agents=[agent], tasks=[task])
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    print("Welcome to the Research Agent!")
    topic = input("Enter the research topic: ")
    result = run_research(topic)
    print("Research Result")
    print(result)