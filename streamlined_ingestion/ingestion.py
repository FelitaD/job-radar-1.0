import pandas as pd
from sqlalchemy import create_engine

from config.definitions import JOB_MARKET_DB_USER, JOB_MARKET_DB_PWD

pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 100)

db_string = f"postgresql://{JOB_MARKET_DB_USER}:{JOB_MARKET_DB_PWD}@localhost:5432/job_market"
engine = create_engine(db_string)

jobs = pd.read_sql("jobs", engine)
# de_jobs = pd.read_sql("SELECT * FROM jobs WHERE title LIKE '%data engineer%';", engine)

print(jobs.head())
de_jobs = jobs