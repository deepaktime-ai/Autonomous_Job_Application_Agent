from typing import Dict
from memory import Memory


class AutoApplyBot:
    def __init__(self):
        self.memory = Memory()

    def apply_to_job(self, job: Dict) -> str:
        """
        Simulate job application
        """

        # 🔹 Check if already applied
        if self.memory.is_applied(job):
            return f"⚠️ Already applied to {job['title']} at {job['company']}"

        # 🔹 Simulate application process
        print(f"🚀 Applying to {job['title']} at {job['company']}...")

        # (Future: Selenium / Playwright automation here)

        # 🔹 Save to memory
        self.memory.add_applied_job(job)

        return f"✅ Successfully applied to {job['title']} at {job['company']}"


# 🔹 Debug Test
if __name__ == "__main__":
    bot = AutoApplyBot()

    test_job = {
        "title": "Python Developer",
        "company": "TCS",
        "location": "Remote"
    }

    print("🤖 Testing Auto Apply Bot...\n")

    result1 = bot.apply_to_job(test_job)
    print(result1)

    print("\nTrying again...\n")

    result2 = bot.apply_to_job(test_job)
    print(result2)