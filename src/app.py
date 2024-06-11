from sqlalchemy import create_engine
from models import db
from db_operations import Database_Operations

ops = Database_Operations(db)

# Looking for a planet named "Tatooine"
tatooine = ops.planet_find_by_name("Alderaan")
# If it is not found add it
if (tatooine is None):
    tatooine = ops.planet_create(
        name="Tatooine", diameter="10465", gravity="1", population="120000")

# Looking for a planet named "Alderaan"
alderaan = ops.planet_find_by_name("Alderaan")
if (alderaan is None):
    alderaan = ops.planet_create(
        name="Aldera", diameter="12500", gravity="1 standard", population="2000000000")

# Let's add the earth just for fun
earth = ops.planet_create(name="Earth", diameter="12742",
                          gravity="1 standard", population="8100000000")

# Fix Alderan name Typo
alderaan = ops.planet_edit(id=alderaan.id, name="Alderaan")

# List all planets
planets = ops.planet_list()
if (planets is not None):
    mapped_planets = list(map(lambda x: x.name, planets))
    print("List of planets:")
    print(mapped_planets)

# Look for a planet by specific id
first_planet = ops.planet_get(id=1)
print("First planet:")
print(first_planet)

# Register princess Leia, refering Alderaan as her homeworld
leia = ops.people_create(name="Leia Organa", height=150, mass=49,
                         birth_year="19BBY", gender="female", homeworld_id=alderaan.id)

# Now we can see her among Alderaan residents
print("Alderaan residents:")
print(alderaan.residents)

# Now let's register Luke and Anakin
# But first we need to find tatooine in order to use it as homeworld
tatooine = ops.planet_find_by_name(name="Tatooine")
luke = ops.people_create(name="Luke Skywalker", height=172, mass=77,birth_year="19BBY", gender="male", homeworld_id=tatooine.id)
anakin = ops.people_create(name="Anakin Skywalker", height=188, mass=84,birth_year="41.9BBY", gender="male", homeworld_id=tatooine.id)
print("Tatooine residents:")
print(tatooine.residents)

# let's look for the original trilogy
new_hope = ops.film_get_episode(episode_id=4)
empire = ops.film_get_episode(episode_id=5)
jedi = ops.film_get_episode(episode_id=6)
# If the movies are not found, add them
if (new_hope is None):
    new_hope = ops.film_create(title="A new hope", episode_id=4, director="George Lucas",
                               producer="Gary Kurtz, Rick McCallum", release_date="1977-05-25")

if (empire is None):
    empire = ops.film_create(title="The Empire Strikes Back", episode_id=5, director="Irvin Kershner",
                             producer="Gary Kurtz, Rick McCallum", release_date="1980-05-17")

if (jedi is None):
    jedi = ops.film_create(title="Return of the Jedi", episode_id=6, director="Richard Marquand",
                           producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date="1983-05-25")


# Now let's add the planets as films locations to a A new hope
ops.film_add_locations(planet_id=alderaan.id, film_id=new_hope.id)
ops.film_add_locations(planet_id=tatooine.id, film_id=new_hope.id)
ops.film_add_locations(planet_id=earth.id, film_id=new_hope.id)
print("A new hope planets")
print(new_hope.locations)

# Delete planet earth witch is not on Star Wars (at least in the movies)
ops.film_remove_locations(planet_id=earth.id, film_id=new_hope.id)
if (ops.planet_delete(planet=earth)):
    print("Planet earth deleted")


# Next let's add the people as characters of A new hope
ops.film_add_characters(people_id=luke.id,film_id=new_hope.id)
ops.film_add_characters(people_id=anakin.id,film_id=new_hope.id)
ops.film_add_characters(people_id=leia.id,film_id=new_hope.id)
print("A new hope characters")
print(new_hope.charaters)

# But wait, Anakin is not in "A new hope"
ops.film_remove_characters(people_id=anakin.id, film_id=new_hope.id)
print("Now these are the correct characters")
print(new_hope.charaters)

# Now we have a Star Wars database