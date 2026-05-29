from llm import OllamaLLM
from tools import get_tools
from job_scraper import JobScraper
from resume_parser import ResumeParser
from memory import Memory


class AgentExecutor:
    def __init__(self):
        self.llm = OllamaLLM()
        self.tools = get_tools()
        self.scraper = JobScraper()
        self.resume_parser = ResumeParser()
        self.memory = Memory()

    def run(self, user_input: str, resume_text: str = "") -> str:
        """
        Main agent execution
        """
        intent = self._detect_intent(user_input)

        if intent == "job_search":
            return self._handle_job_search(user_input)

        elif intent == "resume_match":
            return self._handle_resume_match(user_input, resume_text)

        elif intent == "cover_letter":
            return self._handle_cover_letter(user_input)

        else:
            return self.llm.generate(user_input)

    # 🔹 Intent Detection (simple but effective)

    def _detect_intent(self, user_input: str) -> str:

        user_input = user_input.lower()

    # 🔥 Priority matters (most specific first)
        if "cover letter" in user_input:
          return "cover_letter"

        elif "match" in user_input or "resume" in user_input:
          return "resume_match"

        elif "job" in user_input or "find" in user_input:
          return "job_search"

        else:
          return "general"

    # 🔹 Handle Job Search
    def _handle_job_search(self, query: str) -> str:
        jobs = self.scraper.search_jobs(query)

        output = "🔍 Jobs Found:\n\n"

        for job in jobs:
            self.memory.add_viewed_job(job)

            output += f"{job['title']} at {job['company']} ({job['location']})\n"

        return output

    # 🔹 Handle Resume Match
    def _handle_resume_match(self, query: str, resume_text: str) -> str:
        jobs = self.scraper.search_jobs(query)

        if not resume_text:
            return "❌ Please provide resume text for matching."

        output = "📊 Resume Match Results:\n\n"

        for job in jobs:
            match = self.resume_parser.match_resume_to_job(resume_text, job)

            output += (
                f"{job['title']} at {job['company']}\n"
                f"Match: {match['match_score']}%\n\n"
            )

        return output

    # 🔹 Handle Cover Letter
    def _handle_cover_letter(self, job_desc: str) -> str:
        return self.tools["cover_letter"].run(job_desc)


# 🔹 Debug Test
if __name__ == "__main__":
    agent = AgentExecutor()

    resume_text = """
    Python developer with experience in Django, FastAPI,
    Machine Learning and SQL.
    """

    print("🤖 Agent Executor Started (type 'exit' to quit)\n")

    while True:
        user_input = input("👤 You: ")

        if user_input.lower() == "exit":
            print("👋 Exiting...")
            break

        response = agent.run(user_input, resume_text)

        print("\n🤖 Agent:\n")
        print(response)
        print("\n" + "-" * 50 + "\n")