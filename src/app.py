from sqlalchemy import create_engine
from models import db
from db_operations import Database_Operations

ops=Database_Operations(db)

#ops.planet_create(name="Tatooine",diameter="10465",gravity="1",population="120000")
#alderaan=ops.planet_create(name="Aldera",diameter="12500",gravity="1 standard",population="2000000000")
earth=ops.planet_create(name="Earth",diameter="12742",gravity="1 standard",population="8100000000")

# Fix alderan Typo
alderaan=ops.planet_edit(id=19, name="Alderaan")

# List all planets
planets=ops.planet_list()
if(planets is not None):
  # you can choose to serialize the entire object instead of just mapping the name
  #mapped_planets = list(map(lambda x: x.serialize(), planets))
  mapped_planets = list(map(lambda x: x.name, planets))
  print(mapped_planets)

#Delete planet earth witch is not on Star Wars
if(ops.planet_delete(planet=earth)): print("Planet earth deleted")

# Look for a planet by specific id
first_planet=ops.planet_get(id=1)
print(first_planet.serialize())