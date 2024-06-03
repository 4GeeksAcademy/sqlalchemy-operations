from sqlalchemy.orm import Session
from models import engine,User

def people_create():
  with Session(engine) as session:
    session.begin()
    try:
      user=User(id=1)
      session.add(user)
    except:
      session.rollback()
    else:
      session.commit()
  return None
def people_get():
  return None
def people_list():
  return None
def people_edit():
  return None
def people_delete():
  return None

def planet_create():
  return None
def planet_get():
  return None
def planet_list():
  return None
def planet_edit():
  return None
def planet_delete():
  return None

def film_create():
  return None
def film_get():
  return None
def film_list():
  return None
def film_edit():
  return None
def film_delete():
  return None

def people_get_homeworld():
  return None
def planet_residents():
  return None
def film_locations():
  return None
def film_characters():
  return None
