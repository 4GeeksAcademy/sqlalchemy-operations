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

    def __repr__(self):
        return "<Films {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }

class Planets(Base):
    __tablename__ = "planets"
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return "<Planets {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }


class People(Base):
    __tablename__ = "people"
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return "<People {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }


class Locations(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return "<Location {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }


class Character(Base):
    __tablename__ = "charaters"
    id: Mapped[int] = mapped_column(primary_key=True)

    def __repr__(self):
        return "<Character {}>".format(self.id)

    def serialize(self):
        return {
            "id": self.id
        }

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
