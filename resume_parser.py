from typing import List, Dict


class ResumeParser:
    def __init__(self):
        # 🔹 Predefined skill keywords (can expand later)
        self.skill_keywords = [
            "python", "java", "c++", "machine learning",
            "deep learning", "django", "flask", "fastapi",
            "sql", "mongodb", "data analysis", "nlp"
        ]

    def extract_skills(self, resume_text: str) -> List[str]:
        """
        Extract skills from resume text
        """
        resume_text = resume_text.lower()

        found_skills = [
            skill for skill in self.skill_keywords
            if skill in resume_text
        ]

        return found_skills

    def match_resume_to_job(self, resume_text: str, job: Dict) -> Dict:
        """
        Match resume skills with job skills
        """
        resume_skills = self.extract_skills(resume_text)
        job_skills = [skill.lower() for skill in job.get("skills", [])]

        if not job_skills:
            return {
                "match_score": 0,
                "matched_skills": [],
                "missing_skills": []
            }

        matched = [skill for skill in job_skills if skill in resume_skills]
        missing = [skill for skill in job_skills if skill not in resume_skills]

        score = int((len(matched) / len(job_skills)) * 100)

        return {
            "match_score": score,
            "matched_skills": matched,
            "missing_skills": missing
        }


# 🔹 Debug Test
if __name__ == "__main__":
    parser = ResumeParser()

    resume_text = """
    I am a Python developer with experience in Django, FastAPI,
    Machine Learning and SQL databases.
    """

    job = {
        "title": "AI Engineer",
        "skills": ["Python", "Machine Learning", "Deep Learning", "SQL"]
    }

    print("📄 Testing Resume Parser...\n")

    skills = parser.extract_skills(resume_text)
    print("Extracted Skills:", skills)

    match = parser.match_resume_to_job(resume_text, job)
    print("\nMatch Result:", match)