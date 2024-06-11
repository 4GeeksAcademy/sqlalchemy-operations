from datetime import date
import os
from typing import List
from sqlalchemy import create_engine, String, Integer, Date, ForeignKey
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


class Films(Base):
    __tablename__ = "films"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    episode_id: Mapped[int] = mapped_column(Integer, unique=True)
    director: Mapped[str] = mapped_column(String(100))
    producer: Mapped[str] = mapped_column(String(100))
    release_date: Mapped[date] = mapped_column(Date)
    locations: Mapped[List["Locations"]] = relationship(back_populates="film")
    characters: Mapped[List["Character"]] = relationship(back_populates="film")

    def __repr__(self):
        return "<Film {}: {}>".format(self.id, self.title)

class Planets(Base):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    diameter: Mapped[str] = mapped_column(String(50))
    gravity: Mapped[str] = mapped_column(String(50))
    population: Mapped[str] = mapped_column(String(50))
    residents: Mapped[List["People"]] = relationship(
        back_populates="homeworld")
    movies: Mapped[List["Locations"]] = relationship(back_populates="planet")

    def __repr__(self):
        return "<Planets {}: {}>".format(self.id, self.name)
 
class People(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    height: Mapped[int] = mapped_column(Integer)
    mass: Mapped[int] = mapped_column(Integer)
    birth_year: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(50))
    homeworld_id = mapped_column(ForeignKey("planets.id"), nullable=True)
    homeworld: Mapped["Planets"] = relationship(back_populates="residents")
    movies: Mapped[List["Character"]] = relationship(back_populates="people")

    def __repr__(self):
        return "<People {}: {}>".format(self.id, self.name)

class Locations(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    planet_id = mapped_column(ForeignKey("planets.id"))
    planet: Mapped["Planets"] = relationship(back_populates="movies")
    film_id = mapped_column(ForeignKey("films.id"))
    film: Mapped["Films"] = relationship(back_populates="locations")

    def __repr__(self):
        return "<Location of {}: Planet: {}>".format(self.film.title, self.planet.name)

class Character(Base):
    __tablename__ = "characters"
    id: Mapped[int] = mapped_column(primary_key=True)
    people_id = mapped_column(ForeignKey("people.id"))
    people: Mapped["People"] = relationship(back_populates="movies")
    film_id = mapped_column(ForeignKey("films.id"))
    film: Mapped["Films"] = relationship(back_populates="characters")

    def __repr__(self):
        return "<Character of {}: {}>".format( self.film.title, self.people.name)


#--------------------------------------------------------------------
# Don't edit the lines bellow here - No edite la lineas abajo de aquí
#--------------------------------------------------------------------
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    db_url = db_url.replace("postgres://", "postgresql://")
else:
    db_url = "sqlite:////tmp/test.db"


# You can add 'echo=True' as param to the next line and see the sql under the hood
# You can add 'echo=True' as param to the next line and see the sql under the hood
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
db = Session()
