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
    episode_id: Mapped[int] = mapped_column(Integer)
    director: Mapped[str] = mapped_column(String(100))
    producer: Mapped[str] = mapped_column(String(100))
    release_date: Mapped[date] = mapped_column(Date)

    def __repr__(self):
        return "<Films %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "episode_id": self.episode_id,
            "director": self.director,
            "producer": self.producer,
            "release_date": self.release_date
        }

class Planets(Base):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    diameter: Mapped[str] = mapped_column(String(50))
    gravity: Mapped[str] = mapped_column(String(50))
    population: Mapped[str] = mapped_column(String(50))
    residents:Mapped[List["People"]]=relationship(back_populates="homeworld")

    def __repr__(self):
        return "<Planets %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "population": self.population
        }

class People(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    height: Mapped[int] = mapped_column(Integer)
    mass: Mapped[int] = mapped_column(Integer)
    birth_year: Mapped[str] = mapped_column(String(50))
    gender: Mapped[str] = mapped_column(String(50))
    homeworld_id = mapped_column(ForeignKey("planets.id"))
    homeworld:Mapped["Planets"]=relationship(back_populates="residents")

    def __repr__(self):
        return "<People %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "homeworld": self.homeworld
        }

class Locations(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)
    planetId = mapped_column(ForeignKey("planets.id"))
    filmId = mapped_column(ForeignKey("films.id"))

    def __repr__(self):
        return "<Locations %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "planetId": self.planetId,
            "filmId": self.filmId
        }

class Cast(Base):
    __tablename__ = "cast"
    id: Mapped[int] = mapped_column(primary_key=True)
    people = mapped_column(ForeignKey("people.id"))
    film = mapped_column(ForeignKey("films.id"))

    def __repr__(self):
        return "<Cast %r>" % self.id

    def serialize(self):
        return {
            "id": self.id,
            "people": self.people,
            "film": self.film
        }


# Don't edit the lines bellow here - No edite la lineas abajo de aquí
db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    db_url = db_url.replace("postgres://", "postgresql://")
else:
    db_url = "sqlite:////tmp/test.db"


# You can add 'echo=True' as param to the next line and see the sql under the hood
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
db = Session()
