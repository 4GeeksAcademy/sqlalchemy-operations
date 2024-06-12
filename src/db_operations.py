from sqlalchemy import select, Column
from models import People, Planets, Films, Locations,Character


class Database_Operations:
    # Constructor to initialize the object
    def __init__(self, session):
        self.session = session

    #####################
    # Planets operations
    #####################
    def planet_create(self, name, diameter, gravity, population):
        new_planet = Planets(
            name=name,
            diameter=diameter,
            gravity=gravity,
            population=population
        )
        try:
            self.session.add(new_planet)
        except Exception as e:
            print(e)
            self.session.rollback()
            return None
        else:
            self.session.commit()
            return new_planet

    def planet_get(self, id):
        try:
            query = select(Planets).filter_by(id=id)
            planet = self.session.scalars(query).first()
            return planet
        except Exception as e:
            print(e)
            print(f"Error occurred during transaction: {e}")
            return None

    def planet_find_by_name(self,name):
      try:
          query = select(Planets).filter_by(name=name)
          planet = self.session.scalars(query).first()
          return planet
      except Exception as e:
          print(e)
          print(f"Error occurred during transaction: {e}")
          return None

    def planet_list(self, limit=None, offset=None):
        try:
            query = select(Planets)
            if (limit):
                query=query.limit(limit)
            if (offset):
                query=query.offset(offset)
            results = self.session.scalars(query).all()
            return results
        except Exception as e:
            print(e)
            print(f"Error occurred during transaction: {e}")
            return None

    def planet_edit(self, id, name=None, diameter=None, gravity=None, population=None):
        try:
            query = select(Planets).filter_by(id=id)
            planet = self.session.scalars(query).first()
            if (planet is None):
                print("Planet not found")
                return None
            # Validate if the values are there to be updated
            if (name is not None):
                planet.name = name
            if (diameter is not None):
                planet.diameter = diameter
            if (gravity is not None):
                planet.gravity = gravity
            if (population is not None):
                planet.population = population
            self.session.add(planet)
            self.session.commit()
            return planet
        except Exception as e:
            print(e)
            self.session.rollback()
            print(f"Error occurred during transaction: {e}")
            return None

    def planet_delete(self, id=None, planet=None):
        try:
            if (planet is not None):
                self.session.delete(planet)
                self.session.commit()
                return True
            elif (id is not None):
                planet = self.session.get(Planets, id)
                self.session.delete(planet)
                self.session.commit()
                return True
        except Exception as e:
            print(e)
            return False

    ###################
    # Films operations
    ###################
    def film_create(self, title, episode_id, director, producer, release_date):
        new_film = Films(
            title=title,
            episode_id=episode_id,
            director=director,
            producer=producer,
            release_date=release_date,
        )
        try:
            self.session.add(new_film)
        except Exception as e:
            print(e)
            self.session.rollback()
            return None
        else:
            self.session.commit()
            return new_film

    def film_get(self, id):
        try:
            query = select(Films).filter_by(id=id)
            film = self.session.scalars(query).first()
            return film
        except Exception as e:
            print(e)
            print(f"Error occurred during transaction: {e}")
            return None
        
    def film_get_episode(self, episode_id):
      try:
          query = select(Films).filter_by(episode_id=episode_id)
          film = self.session.scalars(query).first()
          return film
      except Exception as e:
          print(e)
          print(f"Error occurred during transaction: {e}")
          return None

    def film_list(self, limit=None, offset=None):
        try:
            query = select(Films)
            if (limit):
                query=query.limit(limit)
            if (offset):
                query=query.offset(offset)
            results = self.session.scalars(query).all()
            return results
        except Exception as e:
            print(e)
            print(f"Error occurred during transaction: {e}")
            return None

    def film_edit(self,id,title,episode_id, director, producer, release_date):
        try:
            query = select(Films).filter_by(id=id)
            film = self.session.scalars(query).first()
            if (film is None):
                print("Film not found")
                return None
            if(title):
              film.title=title
            if(episode_id):
              film.episode_id=episode_id
            if(director):
              film.director=director
            if(producer):
              film.producer=producer
            if(release_date):
              film.release_date=release_date
            self.session.add(film)
            self.session.commit()
            return film
        except Exception as e:
            print(e)
            self.session.rollback()
            print(f"Error occurred during transaction: {e}")
            return None

    def film_delete(self,id=None, film=None):
        try:
            if (film is not None):
                self.session.delete(film)
                self.session.commit()
                return True
            elif (id is not None):
                film = self.session.get(Films, id)
                self.session.delete(film)
                self.session.commit()
                return True
        except Exception as e:
            print(e)
            return False

    ###################
    # People operations
    ###################
    def people_create(self,name,height,mass,birth_year,gender,homeworld_id):
        people = People(
            name=name,
            height=height,
            mass=mass,
            birth_year=birth_year,
            gender=gender,
            homeworld_id=homeworld_id
        )
        try:
            self.session.add(people)
        except Exception as e:
            print(e)
            self.session.rollback()
            return None
        else:
            self.session.commit()
            return people

    def people_get(self,id):
        try:
            query = select(People).filter_by(id=id)
            people = self.session.scalars(query).first()
            return people
        except Exception as e:
            print(e)
            print(f"Error occurred during transaction: {e}")
            return None

    def people_list(self, limit=None, offset=None):
        try:
            query = select(People)
            if (limit):
                query=query.limit(limit)
            if (offset):
                query=query.offset(offset)
            results = self.session.scalars(query).all()
            return results
        except Exception as e:
            print(e)
            print(f"Error occurred during transaction: {e}")
            return None

    def people_edit(self,id,name,height,mass,birth_year,gender,homeworld_id):
        try:
          query = select(People).filter_by(id=id)
          people = self.session.scalar(query)
          if (people is None):
              print("People not found")
              return None
          if(name):
            people.name=name
          if(height):
            people.height=height
          if(mass):
            people.mass=mass
          if(birth_year):
            people.birth_year=birth_year
          if(gender):
            people.gender=gender
          if(homeworld_id):
            people.homeworld_id=homeworld_id
          self.session.add(people)
          self.session.commit()
          return people
        except Exception as e:
            print(e)
            self.session.rollback()
            print(f"Error occurred during transaction: {e}")
            return None

    def people_delete(self, id=None, people=None):
        try:
            if (people is not None):
                self.session.delete(people)
                self.session.commit()
                return True
            elif (id is not None):
                film = self.session.get(People, id)
                self.session.delete(film)
                self.session.commit()
                return True
        except Exception as e:
            print(e)
            return False

    ##############################
    # Operations with relationships
    ##############################

    def film_add_locations(self,planet_id,film_id):
        # Find if this location is already registered in that movie
        query = select(Locations).filter_by(planet_id=planet_id).filter_by(film_id=film_id)
        location = self.session.scalars(query).first()
        # If that location is registered returns false
        if(location): return False

        location=Locations(planet_id=planet_id,film_id=film_id)
        try:
            self.session.add(location)
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
        else:
            return True

    def film_add_characters(self,people_id,film_id):
        # Find if this character is already registered in that movie
        query = select(Character).filter_by(people_id=people_id).filter_by(film_id=film_id)
        character = self.session.scalars(query).first()
        # If that character is registered returns false
        if(character is not None): return False

        character=Character(people_id=people_id,film_id=film_id)
        try:
            self.session.add(character)
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()
            return False
        else:
            return True
    
    def film_remove_locations(self,planet_id,film_id):
        query = select(Locations).filter_by(planet_id=planet_id).filter_by(film_id=film_id)
        location = self.session.scalars(query).first()
        # If that location is registered returns false
        if(location is None): return False
        try:
            self.session.delete(location)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def film_remove_characters(self,people_id,film_id):
        query = select(Character).filter_by(people_id=people_id).filter_by(film_id=film_id)
        character = self.session.scalars(query).first()
        # If that character is registered returns false
        if(character is None): return False
        try:
            self.session.delete(character)
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
