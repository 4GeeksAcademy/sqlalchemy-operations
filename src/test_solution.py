from models import Base, People, Planets, Films, Locations, Character
from db_operations import Database_Operations
from datetime import date
import pytest
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, create_engine,func

engine = create_engine('sqlite:///:memory:')


@pytest.fixture
def session():
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    yield session()
    # Drop tables after each test
    Base.metadata.drop_all(engine)


def test_planet_create(session):
    ops = Database_Operations(session=session)
    ops.planet_create(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    query = select(Planets).filter_by(name="Tatooine")
    output = session.scalars(query).first()
    assert isinstance(output, Planets)


def test_planet_get(session):
    ops = Database_Operations(session=session)
    tatooine = Planets(name="Tatooine", diameter="10465",
                       gravity="1", population="120000")
    session.add(tatooine)
    session.commit()
    test = ops.planet_get(tatooine.id)
    assert isinstance(test, Planets)


def test_planet_find_by_name(session):
    ops = Database_Operations(session=session)
    tatooine = Planets(name="Tatooine", diameter="10465",
                       gravity="1", population="120000")
    session.add(tatooine)
    session.commit()
    tatooine = ops.planet_find_by_name(name="Tatooine")
    assert isinstance(tatooine, Planets)


def test_planet_list(session):
    ops = Database_Operations(session=session)
    planet1 = Planets(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    planet2 = Planets(name="Alderaan", diameter="12500",
                      gravity="1 standard", population="2000000000")
    planet3 = Planets(name="Earth", diameter="12742",
                      gravity="1 standard", population="8100000000")
    session.add(planet1)
    session.add(planet2)
    session.add(planet3)
    session.commit()
    planets = ops.planet_list()
    assert len(planets) == 3 and all(isinstance(planet, Planets) for planet in planets)


def test_planet_edit(session):
    ops = Database_Operations(session=session)
    planet1 = Planets(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    session.add(planet1)
    session.commit()
    test = ops.planet_edit(planet1.id, name="Alderaan", diameter="12500",
                           gravity="1 standard", population="2000000000")
    assert test.name == "Alderaan" and test.diameter == "12500" and test.gravity == "1 standard" and test.population == "2000000000"


""" def test_planet_delete_by_entity(session):
    ops = Database_Operations(session=session)
    planet1 = Planets(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    ops.planet_delete(planet=planet1)
    count=session.query(func.count(Planets.id)).scalar()
    assert count == 0 """


def test_planet_delete_by_id(session):
    ops = Database_Operations(session=session)
    planet1 = Planets(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    ops.planet_delete(id=planet1.id)
    count=session.query(func.count(Planets.id)).scalar()
    assert count == 0


def test_film_create(session):
    ops = Database_Operations(session=session)
    ops.film_create(title="A new hope", episode_id=4, director="George Lucas",
                    producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    query = select(Films).filter_by(title="A new hope")
    output = session.scalars(query).first()
    assert isinstance(output, Films)


def test_film_get(session):
    ops = Database_Operations(session=session)
    new_film = Films(title="A new hope", episode_id=4, director="George Lucas",
                     producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(new_film)
    session.commit()
    test = ops.film_get(id=new_film.id)
    assert isinstance(test, Films)


def test_film_get_episode(session):
    ops = Database_Operations(session=session)
    new_film = Films(title="A new hope", episode_id=4, director="George Lucas",
                     producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(new_film)
    session.commit()
    test = ops.film_get_episode(4)
    assert isinstance(test, Films)


def test_film_list(session):
    ops = Database_Operations(session=session)
    new_hope = Films(title="A new hope", episode_id=4, director="George Lucas",
                     producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    empire = Films(title="The Empire Strikes Back", episode_id=5, director="Irvin Kershner",
                   producer="Gary Kurtz, Rick McCallum", release_date=date(year=1980, month=5, day=17))
    jedi = Films(title="Return of the Jedi", episode_id=6, director="Richard Marquand",
                 producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date=date(year=1983, month=5, day=25))
    session.add(new_hope)
    session.add(empire)
    session.add(jedi)
    session.commit()
    films = ops.film_list()
    assert len(films) == 3 and all(isinstance(film, Films) for film in films)


def test_film_edit(session):
    ops = Database_Operations(session=session)
    jedi = Films(title="A new hope", episode_id=4, director="George Lucas",
                 producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(jedi)
    session.commit()
    test = ops.film_edit(id=jedi.id, title="Return of the Jedi", episode_id=6, director="Richard Marquand",
                         producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date=date(year=1983, month=5, day=25))
    assert test.title == "Return of the Jedi" and test.episode_id == 6 and test.director == "Richard Marquand" and test.producer == "Howard G. Kazanjian, George Lucas, Rick McCallum" and test.release_date == date(
        year=1983, month=5, day=25)


""" def test_film_delete_by_entity(session):
    ops = Database_Operations(session=session)
    new_film = Films(title="A new hope", episode_id=4, director="George Lucas",
                     producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(new_film)
    session.commit()
    ops.film_delete(film=new_film)
    count=session.query(func.count(Films.id)).scalar()
    assert count == 0 """

def test_film_delete_by_id(session):
    ops = Database_Operations(session=session)
    new_film = Films(title="A new hope", episode_id=4, director="George Lucas",
                     producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(new_film)
    session.commit()
    ops.film_delete(id=new_film.id)
    count=session.query(func.count(Films.id)).scalar()
    assert count == 0

def test_people_create(session):
    ops = Database_Operations(session=session)
    ops.people_create(name="Leia Organa", height=150, mass=49,
                      birth_year="19BBY", gender="female", homeworld_id=1)
    query = select(People).filter_by(name="Leia Organa")
    output = session.scalars(query).first()
    print(output is None)
    assert isinstance(output, People)


def test_people_get(session):
    ops = Database_Operations(session=session)
    luke = ops.people_create(name="Luke Skywalker", height=172,
                             mass=77, birth_year="19BBY", gender="male", homeworld_id=1)
    query = select(People).filter_by(name="Luke Skywalker")
    test = session.scalar(query)
    assert isinstance(test, People)


def test_people_list(session):
    ops = Database_Operations(session=session)
    leia = People(name="Leia Organa", height=150, mass=49,
                  birth_year="19BBY", gender="female", homeworld_id=1)
    anakin = People(name="Anakin Skywalker", height=188, mass=84,
                    birth_year="41.9BBY", gender="male", homeworld_id=1)
    luke = People(name="Leia Organa", height=150, mass=49,
                  birth_year="19BBY", gender="female", homeworld_id=1)
    session.add(leia)
    session.add(luke)
    session.add(anakin)
    session.commit()
    output = ops.people_list()
    assert len(output)==3 and all(isinstance(people, People) for people in output)


def test_people_edit(session):
    ops = Database_Operations(session=session)
    luke = People(name="Leia Organa", height=150, mass=49,
                  birth_year="19BBY", gender="female", homeworld_id=1)
    session.add(luke)
    session.commit()
    test = ops.people_edit(id=luke.id, name="Luke Skywalker", height=172,
                           mass=77, birth_year="19BBY", gender="male", homeworld_id=1)
    assert test.name == "Luke Skywalker" and test.height == 172 and test.mass == 77 and test.birth_year == "19BBY" and test.gender == "male" and test.homeworld_id == 1

""" def test_people_delete_by_entity(session):
    ops = Database_Operations(session=session)
    luke = People(name="Leia Organa", height=150, mass=49,
                  birth_year="19BBY", gender="female", homeworld_id=1)
    session.add(luke)
    session.commit()
    ops.people_delete(people=luke)
    count=session.query(func.count(People.id)).scalar()
    assert count==0 """

def test_people_delete_by_id(session):
    ops = Database_Operations(session=session)
    luke = People(name="Leia Organa", height=150, mass=49,
                  birth_year="19BBY", gender="female", homeworld_id=1)
    session.add(luke)
    session.commit()
    ops.people_delete(id=luke.id)
    count=session.query(func.count(People.id)).scalar()
    assert count==0


def test_film_add_locations(session):
    ops = Database_Operations(session=session)
    tatooine=ops.planet_create(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    hope=ops.film_create(title="A new hope", episode_id=4, director="George Lucas",
                    producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(tatooine)
    session.add(hope)
    session.commit()
    ops.film_add_locations(planet_id=tatooine.id,film_id=hope.id)
    query=select(Locations)
    location=session.scalars(query).first()
    assert isinstance(location.film, Films) and isinstance(location.planet,Planets)


def test_film_add_characters(session):
    ops = Database_Operations(session=session)
    hope=ops.film_create(title="A new hope", episode_id=4, director="George Lucas",
                    producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    luke = ops.people_create(name="Luke Skywalker", height=172,
                             mass=77, birth_year="19BBY", gender="male", homeworld_id=1)        
    session.add(hope)
    session.add(luke)
    session.commit()
    ops.film_add_characters(people_id=luke.id,film_id=hope.id)
    query=select(Character)
    character=session.scalars(query).first()
    assert isinstance(character.film,Films) and isinstance(character.people,People)


def test_film_remove_locations(session):
    ops = Database_Operations(session=session)
    tatooine=ops.planet_create(name="Tatooine", diameter="10465",
                      gravity="1", population="120000")
    hope=ops.film_create(title="A new hope", episode_id=4, director="George Lucas",
                    producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    session.add(tatooine)
    session.add(hope)
    session.flush()
    location=Locations(film_id=hope.id,planet_id=tatooine.id)
    session.add(location)
    session.commit()
    ops.film_remove_locations(planet_id=tatooine.id,film_id=hope.id)
    count=session.query(func.count(Locations.id)).scalar()
    assert count==0


def test_film_remove_characters(session):
    ops = Database_Operations(session=session)
    hope=ops.film_create(title="A new hope", episode_id=4, director="George Lucas",
                    producer="Gary Kurtz, Rick McCallum", release_date=date(year=1977, month=5, day=25))
    luke = ops.people_create(name="Luke Skywalker", height=172,
                             mass=77, birth_year="19BBY", gender="male", homeworld_id=1)        
    session.add(hope)
    session.add(luke)
    session.flush()
    character=Character(film_id=hope.id,people_id=luke.id)
    session.add(character)
    session.commit()
    ops.film_remove_characters(people_id=luke.id,film_id=hope.id)
    count=session.query(func.count(Character.id)).scalar()
    assert count==0
