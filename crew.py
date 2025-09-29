from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class AnalystBusiness():
    """AnalystBusines crew"""

    agents_config = "config/agents.yaml"
    tasks_config="config/tasks.yaml"


    @agent
    def junior_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['junior_researcher'], verbose=True)

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['report_writer'],
            verbose=True
        )

    @task
    def collect_insights(self) -> Task:
        return Task(
            config=self.tasks_config['collect_insights'], )

    @task
    def write_report(self) -> Task:
        return Task(
            config=self.tasks_config['write_report'], output_file='report.md')

    @crew
    def crew(self) -> Crew:
        """Creates the AnalystBusiness crew"""


        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
