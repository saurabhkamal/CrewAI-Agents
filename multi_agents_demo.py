import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
# from langchain_openai import ChatOpenAI

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL"] = "gpt-4-32k"

search_tool = SerperDevTool()

# Creating a senior researcher agent with memory and verbose mode
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        """Driven by curiosity, you are at the forefront of
        innovation, eager to explore knowledge and share knowledege that could change
        the world."""
    ),
    tools=[search_tool],
    allow_delegation=True   # Allow delegation to other agents
)

# Creating a writer agent with custom tools and delegation capability
writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        """With a flair for simplyfying complex topics, you craft 
        engaging narratives that captivate and educate, bringing new
        discoveries to light in an accessible manner. Do mention the topic heading, 
        then continue writing the blog"""
    ),
    tools = [search_tool],
    allow_delegation=False  # No further delegation to other agents
)

# Task for the researcher agent to explore new technologies
research_task = Task(
    description=(
        "Identify the next big trend in {topic}. "
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market oppportunities, and potential risks"
    ),
    expected_output="A comprehensive 3 paragraphs long report on the latest AI trends.",
    tools=[search_tool],
    agent=researcher,
)

write_task = Task(
    description=(
        "Compose an insightful article on {topic}. "
        "Focus on the latest trends and how it's impacting the industry. "
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output="A 4 paragraph article on {topic} advancements formatted as markdown.",
    tools=[search_tool],
    agent=writer,
    async_execution=False,
    output_file = "new-blog-post.md"
)

# Formatting the tech-focused crew with enhanced configurations
crew= Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential    
)

# Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'topic': "AI in financial markets"})
print(result)





