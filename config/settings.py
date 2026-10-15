import os
from dotenv import load_dotenv

load_dotenv()

# Database
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "jobs.db")

# API Keys (optional for test version)
ADZUNA_APP_ID = os.getenv("ADZUNA_APP_ID", "")
ADZUNA_APP_KEY = os.getenv("ADZUNA_APP_KEY", "")
SERPAPI_KEY = os.getenv("SERPAPI_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
HUNTER_API_KEY = os.getenv("HUNTER_API_KEY", "")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")

# Email Settings (Gmail SMTP)
SENDER_EMAIL = os.getenv("SENDER_EMAIL", "")
SENDER_APP_PASSWORD = os.getenv("SENDER_APP_PASSWORD", "")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "hamuha330@gmail.com")

# Daily digest scheduler
DAILY_EMAIL_HOUR = int(os.getenv("DAILY_EMAIL_HOUR", "9"))   # IST hour
DAILY_EMAIL_TIMEZONE = "Asia/Kolkata"
DAILY_JOBS_COUNT = int(os.getenv("DAILY_JOBS_COUNT", "15"))  # how many jobs in email

# Google Sheets
GOOGLE_SHEETS_CREDS = os.getenv("GOOGLE_SHEETS_CREDS", "credentials.json")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")

# Search criteria defaults
DEFAULT_SEARCH_TERMS = [
    "remote backend developer python",
    "remote fastapi developer",
    "remote backend engineer python",
    "remote python developer",
    "remote content officer",
    "remote web content writer",
    "remote seo manager",
    "remote seo analyst",
    "remote seo specialist",
    "remote technical seo specialist",
]

RELEVANT_TECH = [
    "python", "fastapi", "postgresql", "postgres", "mysql", "mongodb", 
    "docker", "kubernetes", "node", "nodejs", "express", "sql", "nosql", 
    "microservices", "seo optimization", "content writing"
]

TITLE_KEYWORDS_POSITIVE = [
    "backend", "back-end", "back end", "python", "django",
    "fastapi", "software engineer", "software developer",
    "full stack", "fullstack", "full-stack", "seo analyst", 
    "seo manager", "remote", "technical seo specialist"
]

TITLE_KEYWORDS_NEGATIVE = [
    "frontend", "front-end", "front end", "ios", "android",
    "mobile", "devops", "data scientist", "machine learning",
    "ml engineer", "ui/ux", "designer", "qa", "test",
    "junior",
]

# ── Location / India Remote Filtering ──

# Keywords that CONFIRM India/Asia people can apply
LOCATION_INDIA_POSITIVE = [
    "worldwide", "global", "anywhere", "africa",
    "remote - global", "remote global", "globally distributed",
    "work from anywhere", "location independent",
    "east africa", "eastern africa", "emea", "emea/apac",
    "nairobi", "kenya", "nzalae/nzawa", "remote-kenya", 
    "remote kenya",
]

# Keywords that BLOCK India — these mean US/EU only
LOCATION_INDIA_NEGATIVE = [
    "us only", "usa only", "us-only", "united states only",
    "must be located in the us", "must reside in the us",
    "us-based", "us based", "u.s. only", "u.s. based",
    "canada only", "uk only", "eu only", "europe only",
    "european union only", "uk-based", "eu-based",
    "must be authorized to work in the united states",
    "no visa sponsorship", "us citizen", "us work authorization",
    "est/cst/pst/ist", "india", "americas only", "americas timezone",
    "north america only", "na only", "latam only",
]

# Timezone overlap hints — India (IST = UTC+5:30)
# These timezones have reasonable overlap with IST
TIMEZONE_COMPATIBLE = [
    "eat", "gmt", "utc", "flexible", "async", "asynchronous",
    "overlap", "any timezone", "all timezones",
]

TIMEZONE_INCOMPATIBLE = [
    "pst only", "est only", "cst only", "mst only",
    "pacific time only", "eastern time only",
    "us timezone required", "us hours required",
    "core hours pst", "core hours est", "ist"
]

# Minimum relevance score to show in polished results
MIN_RELEVANCE_SCORE = 50

# Server
HOST = "127.0.0.1"
PORT = 8000
