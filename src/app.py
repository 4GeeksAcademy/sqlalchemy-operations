from db_operations import Database_Operations
from models import db

ops=Database_Operations(db)

newpeople=ops.people_create(name="Rigo")
print(newpeople)
