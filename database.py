from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row._mapping))
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val": id}
        )
        row = result.mappings().first()

        if row is None:
            return None
        else:
            return dict(row)


def add_application_to_db(job_id, data):
    query = text("""
        INSERT INTO applications (
            job_id, full_name, email, linkedin_url,
            education, work_experience, resume_url
        )
        VALUES (
            :job_id, :full_name, :email, :linkedin_url,
            :education, :work_experience, :resume_url
        )
    """)

    with engine.begin() as conn:  # auto-commit
        conn.execute(query, {
            "job_id": job_id,
            "full_name": data["full_name"],
            "email": data["email"],
            "linkedin_url": data.get("linkedin_url"),
            "education": data.get("education"),
            "work_experience": data.get("work_experience"),
            "resume_url": data.get("resume_url")
        })