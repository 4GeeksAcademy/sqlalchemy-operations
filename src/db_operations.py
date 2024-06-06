from sqlalchemy import select
from models import People, Planets, Films


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
        except:
            self.session.rollback()
        else:
            self.session.commit()
            return new_planet

    def planet_get(self, id):
        try:
            query = select(Planets).filter_by(id=id)
            planet = self.session.scalars(query).first()
            return planet
        except Exception as e:
            print(f"Error occurred during transaction: {e}")
            return None

    def planet_list(self, limit=None, offset=None):
        try:
            query = select(Planets)
            if (limit):
                query.limit(limit)
            if (offset):
                query.offset(offset)
            results = self.session.scalars(query).all()
            return results
        except Exception as e:
            print(f"Error occurred during transaction: {e}")
            return None

    def planet_edit(self, id, name=None, diameter=None, gravity=None, population=None):
        try:
            query = select(Planets).filter_by(id=id)
            planet = self.session.scalars(query).first()
            if (planet is None):
                print("Planet not found")
                return None

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
        except:
            self.session.rollback()
        else:
            self.session.commit()
            return new_film

    def film_get(self):
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
        people = People()
        try:
            self.session.add(people)
        except:
            self.session.rollback()
        else:
            self.session.commit()
            return people

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

    def people_get_homeworld(self):
        return None

    def planet_residents(self):
        return None

    def film_locations(self):
        return None

    def film_characters(self):
        return None
