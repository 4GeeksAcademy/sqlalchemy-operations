from sqlalchemy import create_engine
from models import db
from db_operations import Database_Operations

ops=Database_Operations(db)

# In this file you can use the `ops` object to access the operation in order to test them