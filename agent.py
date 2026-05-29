from llm import OllamaLLM


class SimpleAgent:
    def __init__(self):
        self.llm = OllamaLLM()

    def run(self, user_input: str) -> str:
        """
        Basic agent execution loop
        """
        prompt = self._build_prompt(user_input)

        response = self.llm.generate(prompt)

        return response

    def _build_prompt(self, user_input: str) -> str:
        """
        Structured prompt for better control
        """
        return f"""
You are an intelligent job assistant AI agent.

User Query:
{user_input}

Instructions:
- Understand the user query clearly
- Give helpful, structured response
- Be concise but informative

Response:
"""


# 🔹 Debug / Test
if __name__ == "__main__":
    agent = SimpleAgent()

    print("🤖 Autonomous Job Agent Started (type 'exit' to quit)\n")

    while True:
        user_input = input("👤 You: ")

        if user_input.lower() == "exit":
            print("👋 Exiting agent...")
            break

        response = agent.run(user_input)

        print("\n🤖 Agent:\n")
        print(response)
        print("\n" + "-" * 50 + "\n")