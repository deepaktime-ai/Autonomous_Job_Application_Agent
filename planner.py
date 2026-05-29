from llm import OllamaLLM
from agent_executor import AgentExecutor


class PlannerAgent:
    def __init__(self):
        self.llm = OllamaLLM()
        self.executor = AgentExecutor()

    def create_plan(self, goal: str) -> list:
        """
        Use LLM to break goal into steps
        """
        prompt = f"""
You are an AI planning agent.

Break the following goal into clear step-by-step tasks.

Goal:
{goal}

Rules:
- Output only numbered steps
- Keep steps short and actionable
- Do not explain anything

Steps:
"""

        response = self.llm.generate(prompt)

        steps = self._parse_steps(response)
        return steps

    def _parse_steps(self, text: str) -> list:
        """
        Convert LLM output into list of steps
        """
        lines = text.split("\n")
        steps = []

        for line in lines:
            line = line.strip()

            if line and (line[0].isdigit() or line.startswith("-")):
                # Remove numbering
                step = line.lstrip("0123456789.- ").strip()
                steps.append(step)

        return steps

    def execute_plan(self, goal: str, resume_text: str = "") -> str:
        """
        Execute plan step by step
        """
        steps = self.create_plan(goal)

        if not steps:
            return "❌ Failed to create plan."

        output = "🧠 Plan:\n"
        for i, step in enumerate(steps, 1):
            output += f"{i}. {step}\n"

        output += "\n🚀 Execution:\n\n"

        for step in steps:
            result = self.executor.run(step, resume_text)
            output += f"👉 Step: {step}\n{result}\n\n"

        return output


# 🔹 Debug Test
if __name__ == "__main__":
    planner = PlannerAgent()

    resume_text = """
    Python developer with experience in Django, FastAPI,
    Machine Learning and SQL.
    """

    print("🤖 Planner Agent Started (type 'exit' to quit)\n")

    while True:
        goal = input("🎯 Enter Goal: ")

        if goal.lower() == "exit":
            print("👋 Exiting...")
            break

        result = planner.execute_plan(goal, resume_text)

        print("\n" + result)
        print("\n" + "-" * 50 + "\n")