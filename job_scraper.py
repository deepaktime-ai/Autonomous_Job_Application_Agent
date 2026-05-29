from typing import List, Dict


class JobScraper:
    def __init__(self):
        pass

    def search_jobs(self, query: str, location: str = "India") -> List[Dict]:
        """
        Simulate job search (replace with real scraping later)
        """
        mock_jobs = [
            {
                "title": "Python Developer",
                "company": "TCS",
                "location": "Remote",
                "skills": ["Python", "Django", "REST"],
                "description": "Looking for Python developer with Django experience."
            },
            {
                "title": "AI Engineer",
                "company": "Infosys",
                "location": "Bangalore",
                "skills": ["Python", "Machine Learning", "Deep Learning"],
                "description": "AI Engineer with ML and DL knowledge."
            },
            {
                "title": "Backend Developer",
                "company": "Wipro",
                "location": "Hyderabad",
                "skills": ["Python", "FastAPI", "Databases"],
                "description": "Backend developer with API experience."
            },
        ]

        # 🔹 Simple filter logic (important for realism)
        filtered_jobs = [
            job for job in mock_jobs
            if query.lower() in job["title"].lower()
        ]

        return filtered_jobs if filtered_jobs else mock_jobs


# 🔹 Debug Test
if __name__ == "__main__":
    scraper = JobScraper()

    print("🔍 Testing Job Scraper...\n")

    jobs = scraper.search_jobs("Python")

    for idx, job in enumerate(jobs, 1):
        print(f"{idx}. {job['title']} at {job['company']}")
        print(f"   Location: {job['location']}")
        print(f"   Skills: {', '.join(job['skills'])}")
        print(f"   Description: {job['description']}\n")