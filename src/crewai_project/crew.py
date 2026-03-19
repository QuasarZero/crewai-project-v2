from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class MyCrew:
    """Development team crew for software projects"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def product_manager(self) -> Agent:
        return Agent(config=self.agents_config["product_manager"], verbose=True)

    @agent
    def requirements_analyst(self) -> Agent:
        return Agent(config=self.agents_config["requirements_analyst"], verbose=True)

    @agent
    def ui_designer(self) -> Agent:
        return Agent(config=self.agents_config["ui_designer"], verbose=True)

    @agent
    def software_developer(self) -> Agent:
        return Agent(config=self.agents_config["software_developer"], verbose=True)

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(config=self.agents_config["qa_engineer"], verbose=True)

    @agent
    def technical_writer(self) -> Agent:
        return Agent(config=self.agents_config["technical_writer"], verbose=True)

    @task
    def requirements_gathering(self) -> Task:
        return Task(
            config=self.tasks_config["requirements_gathering"],
        )

    @task
    def ui_design(self) -> Task:
        return Task(
            config=self.tasks_config["ui_design"],
        )

    @task
    def development(self) -> Task:
        return Task(
            config=self.tasks_config["development"],
        )

    @task
    def testing(self) -> Task:
        return Task(
            config=self.tasks_config["testing"],
        )

    @task
    def documentation(self) -> Task:
        return Task(
            config=self.tasks_config["documentation"],
        )

    @task
    def product_review(self) -> Task:
        return Task(
            config=self.tasks_config["product_review"],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
