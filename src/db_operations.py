from models import db,People
class Database_Operations:
  db=None
  def __init__(self, session):
    self.db=session

  def people_create(self,name):
    user=People(name=name)
    try:
      self.db.add(user)
    except Exception as e:
      self.db.rollback()
      print(f"Error occurred: {e}")
      return None
    else:
      self.db.commit()
      print("People created")
      return user

  def people_get(self):
    return None
  def people_list(self):
    return None
  def people_edit(self):
    return None
  def people_delete(self):
    return None

  def planet_create(self):
    return None
  def planet_get(self):
    return None
  def planet_list(self):
    return None
  def planet_edit(self):
    return None
  def planet_delete(self):
    return None

  def film_create(self):
    return None
  def film_get(self):
    return None
  def film_list(self):
    return None
  def film_edit(self):
    return None
  def film_delete(self):
    return None

  def people_get_homeworld(self):
    return None
  def planet_residents(self):
    return None
  def film_locations(self):
    return None
  def film_characters(self):
    return None
