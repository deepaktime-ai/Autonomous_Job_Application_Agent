from typing import Dict, Callable


class Tool:
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func

    def run(self, input_data: str) -> str:
        return self.func(input_data)


# 🔹 TOOL 1: Job Search (Mock for now)
def job_search_tool(query: str) -> str:
    """
    Simulates job search results
    """
    jobs = [
        {"title": "Python Developer", "company": "TCS", "location": "Remote"},
        {"title": "Backend Engineer", "company": "Infosys", "location": "Bangalore"},
        {"title": "AI Engineer", "company": "Wipro", "location": "Hyderabad"},
    ]

    results = "\n".join(
        [f"{job['title']} at {job['company']} ({job['location']})" for job in jobs]
    )

    return f"🔍 Job Results for '{query}':\n{results}"


# 🔹 TOOL 2: Resume Match (Basic logic)
def resume_match_tool(input_data: str) -> str:
    """
    Simulates resume-job matching
    """
    return "✅ Your resume matches this job at 75% (mock result)"


# 🔹 TOOL 3: Cover Letter Generator
def cover_letter_tool(job_description: str) -> str:
    """
    Generates a simple cover letter
    """
    return f"""
Dear Hiring Manager,

I am excited to apply for this position. Based on the job description:
{job_description}

I believe my skills align well with your requirements.

Best regards,
[Your Name]
"""


# 🔹 Register all tools
def get_tools() -> Dict[str, Tool]:
    return {
        "job_search": Tool(
            name="job_search",
            description="Search for jobs based on user query",
            func=job_search_tool,
        ),
        "resume_match": Tool(
            name="resume_match",
            description="Match resume with job description",
            func=resume_match_tool,
        ),
        "cover_letter": Tool(
            name="cover_letter",
            description="Generate a cover letter for a job",
            func=cover_letter_tool,
        ),
    }


# 🔹 Debug Test
if __name__ == "__main__":
    tools = get_tools()

    print("🛠️ Testing Tools...\n")

    print(tools["job_search"].run("Python Developer"))
    print("\n" + "-" * 50 + "\n")

    print(tools["resume_match"].run("My resume data"))
    print("\n" + "-" * 50 + "\n")

    print(tools["cover_letter"].run("Looking for Python Developer with AI skills"))