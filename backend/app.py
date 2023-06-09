# save this as app.py
from flask import Flask
from flask_cors import CORS
import sqlalchemy as db
import os

db_name = os.environ["DB_NAME"]
print("DB name",f'mysql+pymysql://root:admin@{db_name}:3306/sample_db')
engine = db.create_engine(f'mysql+pymysql://root:admin@{db_name}:3306/sample_db')

conn = engine.connect() 
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

