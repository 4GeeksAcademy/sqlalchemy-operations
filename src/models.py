import os
from sqlalchemy import create_engine,String
from sqlalchemy.orm import mapped_column, DeclarativeBase, Mapped, sessionmaker


class Base(DeclarativeBase):
  pass

class People(Base):
  __tablename__="people"
  id:Mapped[int]=mapped_column(primary_key=True)
  name:Mapped[str]=mapped_column(String(30))
  
  def __repr__(self):
    return '<People %r>' % self.id



class Films(Base):
  __tablename__="films"
  id:Mapped[int]=mapped_column(primary_key=True)
  
  def __repr__(self):
    return '<Films %r>' % self.id


class Planets(Base):
  __tablename__="planets"
  id:Mapped[int]=mapped_column(primary_key=True)
  
  def __repr__(self):
    return '<Planets %r>' % self.id


class Locations(Base):
  __tablename__="locations"
  id:Mapped[int]=mapped_column(primary_key=True)
  
  def __repr__(self):
    return '<Locations %r>' % self.id


# Don't edit the lines bellow here - No edite la lineas abajo de aquí

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    db_url = db_url.replace("postgres://", "postgresql://")
else:
    db_url = "sqlite:////tmp/test.db"
    
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
db = Session()