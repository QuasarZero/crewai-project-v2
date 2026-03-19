from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class MyCrew:
    """软件开发团队，负责软件项目的全流程开发"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["product_manager"],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def requirements_analyst(self) -> Agent:
        return Agent(config=self.agents_config["requirements_analyst"], verbose=True)

    @agent
    def project_manager(self) -> Agent:
        return Agent(
            config=self.agents_config["project_manager"],
            allow_delegation=True,
            verbose=True,
        )

    @agent
    def architect(self) -> Agent:
        return Agent(config=self.agents_config["architect"], verbose=True)

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
    def concept_definition(self) -> Task:
        return Task(
            config=self.tasks_config["concept_definition"],
        )

    @task
    def requirements_detail(self) -> Task:
        return Task(
            config=self.tasks_config["requirements_detail"],
            context=[self.concept_definition()],
        )

    @task
    def requirements_review(self) -> Task:
        return Task(
            config=self.tasks_config["requirements_review"],
            context=[self.requirements_detail()],
        )

    @task
    def architecture_design(self) -> Task:
        return Task(
            config=self.tasks_config["architecture_design"],
            context=[self.requirements_review()],
        )

    @task
    def task_breakdown(self) -> Task:
        return Task(
            config=self.tasks_config["task_breakdown"],
            context=[self.architecture_design()],
        )

    @task
    def ui_design_task(self) -> Task:
        return Task(
            config=self.tasks_config["ui_design_task"],
            context=[self.task_breakdown()],
        )

    @task
    def development_task(self) -> Task:
        return Task(
            config=self.tasks_config["development_task"],
            context=[self.task_breakdown(), self.ui_design_task()],
        )

    @task
    def testing_task(self) -> Task:
        return Task(
            config=self.tasks_config["testing_task"],
            context=[self.development_task()],
        )

    @task
    def documentation_task(self) -> Task:
        return Task(
            config=self.tasks_config["documentation_task"],
            context=[self.architecture_design(), self.development_task()],
        )

    @task
    def final_review(self) -> Task:
        return Task(
            config=self.tasks_config["final_review"],
            context=[
                self.requirements_review(),
                self.architecture_design(),
                self.testing_task(),
                self.documentation_task(),
            ],
        )

    @crew
    def crew(self) -> Crew:
        manager_llm = LLM(model="gemini/gemini-flash-latest")
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.hierarchical,
            manager_llm=manager_llm,
            verbose=True,
            output_log_file=True,
            memory=True,
        )
