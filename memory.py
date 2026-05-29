import json
import os
from typing import List, Dict


class Memory:
    def __init__(self, file_path: str = "memory.json"):
        self.file_path = file_path
        self.data = {
            "applied_jobs": [],
            "viewed_jobs": []
        }
        self._load_memory()

    def _load_memory(self):
        """
        Load memory from file if exists
        """
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    self.data = json.load(f)
            except Exception:
                # If corrupted, reset memory
                self._save_memory()
        else:
            self._save_memory()

    def _save_memory(self):
        """
        Save memory to file
        """
        with open(self.file_path, "w") as f:
            json.dump(self.data, f, indent=4)

    # 🔹 Add viewed job
    def add_viewed_job(self, job: Dict):
        if job not in self.data["viewed_jobs"]:
            self.data["viewed_jobs"].append(job)
            self._save_memory()

    # 🔹 Add applied job
    def add_applied_job(self, job: Dict):
        if job not in self.data["applied_jobs"]:
            self.data["applied_jobs"].append(job)
            self._save_memory()

    # 🔹 Get viewed jobs
    def get_viewed_jobs(self) -> List[Dict]:
        return self.data["viewed_jobs"]

    # 🔹 Get applied jobs
    def get_applied_jobs(self) -> List[Dict]:
        return self.data["applied_jobs"]

    # 🔹 Check if already applied
    def is_applied(self, job: Dict) -> bool:
        return job in self.data["applied_jobs"]


# 🔹 Debug Test
if __name__ == "__main__":
    memory = Memory()

    test_job = {
        "title": "Python Developer",
        "company": "TCS"
    }

    print("🧠 Testing Memory System...\n")

    memory.add_viewed_job(test_job)
    memory.add_applied_job(test_job)

    print("Viewed Jobs:", memory.get_viewed_jobs())
    print("Applied Jobs:", memory.get_applied_jobs())
    print("Already Applied?", memory.is_applied(test_job))