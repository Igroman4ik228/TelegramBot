import sqlalchemy as db

from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

engine = db.create_engine(f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
print(engine)
engine.connect()
