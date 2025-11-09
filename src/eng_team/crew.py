from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class EngTeam():
    """EngTeam crew"""
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'],
            verbose=True
        )
    
    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            # Code execution requires Docker to be running. The SDK will try to
            # create a sandboxed container. If you don't have Docker available
            # (or you don't want the crew to execute code), set this to False.
            # To re-enable execution: start Docker Desktop/Engine and set
            # `allow_code_execution=True` and `code_execution_mode="safe"`.
            allow_code_execution=False,
            # code_execution_mode="safe",  # Uses Docker for safety
            max_execution_time=500,
            max_retry_limit=3
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_engineer'],
            verbose=True
        )
    
    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'],
            verbose=True
        )

    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'],
            verbose=True
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task']
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'],
        )

    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task'],
        )

    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_task'],
        )
    
    @task
    def devops_task(self) -> Task:
        return Task(
            config=self.tasks_config['setup_task'],
        )



    @crew
    def crew(self) -> Crew:
        """Creates the EngTeam crew"""
        return Crew(
            agents=self.agents,  # Created by @agent decorator
            tasks=self.tasks,  # Created by @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical
            # (alternative: hierarchical process - see docs)
            # See: https://docs.crewai.com/how-to/Hierarchical/
        )
