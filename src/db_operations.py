from sqlalchemy import select, Column
from models import People, Planets, Films, Locations,Character


class Database_Operations:
    # Constructor to initialize the object
    def __init__(self, session):
        self.session = session

    #####################
    # Planets operations
    #####################
    def planet_create(self):
       return None

    def planet_get(self):
        return None

    def planet_find_by_name(self):
      return None

    def planet_list(self):
        return None

    def planet_edit(self):
        return None

    def planet_delete(self):
        return None

    ###################
    # Films operations
    ###################
    def film_create(self):
        return None

    def film_get(self):
        return None
        
    def film_get_episode(self):
      return None

    def film_list(self):
        return None

    def film_edit(self):
        return None

    def film_delete(self):
        return None

    ###################
    # People operations
    ###################
    def people_create(self):
        return None

    def people_get(self):
        return None

    def people_list(self):
        return None

    def people_edit(self):
        return None

    def people_delete(self):
        return None

    ##############################
    # Operations with relationships
    ##############################

    def film_add_locations(self):
       return None

    def film_add_characters(self):
        return None
    
    def film_remove_locations(self):
        return None

    def film_remove_characters(self):
        return None
