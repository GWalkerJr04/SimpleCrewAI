from langchain.llms import Ollama
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = "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"

ollama_llm = Ollama(model="llama2")
mistral_llm = Ollama(model="mistral")



llm = ChatOpenAI(
    model="crewai-llama2",
    base_url="http://localhost:11434/v1"

)

researcher = Agent(
    role='Researcher',
    goal='Research new AI insights',
    backstory='You are an AI research assistant.',
    verbose=True,
    allow_delegation=False,
    llm=ollama_llm
)

writer = Agent(
    role='Writer',
    goal='Write compelling and engaging blog posts about AI trends and insights.',
    backstory='You are an AI bot blog post writer who specializes in writing AI topics.',
    verbose=True,
    allow_delegation=False,
    llm=mistral_llm
)

task1 = Task(description='Investigate the latest AI trends', expected_output='Full analysis report in bullet points', agent=researcher)
task2 = Task(description='Write a compelling blog post based on the latest AI trends', expected_output='Full blog post of at least 4 paragraphs', agent=writer)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()