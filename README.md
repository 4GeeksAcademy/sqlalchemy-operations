<!--hide-->
# Build a Star Wars database with SQLAlchemy
<!--endhide-->

## Star Wars Database
The Star Wars universe needs a database to store the information of all the planets and their inhabitants, as well as the data of the movies, the characters that integrate them and the planets where they take place... The force is intense in this project!

## 🌱 Cómo comenzar este proyecto

This project comes with the necessary files to start working immediately.

We recommend opening this same repository using a development environment such as [Codespaces](https://4geeks.com/lesson/what-is-github-codespaces) (recomended) or [Gitpod](https://4geeks.com/lesson/how-to-use-gitpod).  `git clone`.

This is the repository you need to open:

```txt
https://github.com/4GeeksAcademy/sqlalchemy-operations
```

## 💻 Installation

1. Install the project dependencies `$ pipenv install`.

2. Enter inside the *virtual environment* `$ pipenv shell`.

## 🌐 Migration of your database

1. Run the `pipenv run migrate` command to generate a new migration.

2. Run the `pipenv run upgrade` command to apply the migrations to your database.

> It is necessary to follow these steps the first time you start your repo and then every time you make changes to the model structure.

## ✅ Self-evaluation

+ Evaluate your code with the command `pipenv run test`

## 📝 Instructions

### On the `models.py` file

1. Use python to represent in SQLAlchemy the model shown in the image:

![Star Wars database model](https://raw.githubusercontent.com/4GeeksAcademy/sqlalchemy-operations/master/docs/assets/model.png)

2. The tables must have the same attributes or columns that are reflected in the model.

3. You must implement foreign keys in cases where there are relationships.

4. Implement the use of `relationship` type properties to access data that are related.

5. For each model write a `__repr__` function to specify how the objects displayed in the console are **represented**. This helps you to improve the development experience of the project.

Just edit the classes to complete the columns and relationships that are reflected in the model.
*** Translated with www.DeepL.com/Translator (free version) ***



### On the `db_operations.py` file

In this file you will find the operations that must be performed to manage the information in the database, usually the CRUD methods (**C**reate, **R**ead, **U**pdate,**D**elete) are developed, along with others that meet the requirements of the project.

#### Write the code that performs the task indicated by the function name

```python
# Planets
def planet_create(): # Create
def planet_get(): # Search by id
def planet_find_by_name(): # Search by name
def planet_list(): # List all planets
def planet_edit(): # Edit data by specifying the id
def planet_delete(): # Delete by id

# Movies
def film_create(): # Create
def film_get(): # Search by id
def film_get_episode(): # Search by episode number
def film_list(): # List of all movies
def film_edit(): # Edit data by id
def film_delete(): # Delete by id

# People
def people_create(): # Create
def people_get(): # Search by id
def people_list():# Get list
def people_edit(): # Edit data specifying by id
def people_delete(): # Delete by id

# Operations with relations
def film_add_locations(): # Add a record given the id of the movie and the id of the planet
def film_add_characters():# Add a record given the id of the movie and the id of the person
def film_remove_locations(): # Delete a record given the id of the movie and the id of the planet
def film_remove_characters(): # Delete a record given the id of the movie and the id of the person
```

#### Input and output data types

As part of the challenge you must specify the types of data to be received by each of the functions, as well as use a specific data type as output. To do this you must take into consideration the following aspects

- The `create` functions must receive all the data that the table needs, except the id that is generated automatically. These functions must return the created object.

- The `get` or `find` functions must return a single entity. It can be the first result that matches the search.

- The `edit` functions also receive all the entity data as a parameters, with the `id` being mandatory and the rest optional so that only the specified data is modified and the rest is preserved as is. These functions must also return the edited object.

- The `delete` functions must return `True` if the deletion was successful.

- The pivot table functions `locations` and `characters` do all the operations with foreign keys so they only need the `id` of the elements they are going to relate to.
- Remember to use the [snake_case](https://wikipedia.org/wiki/Snake_case) convention for variable names, for example: `people_id`.

### On the `app.py` file

In this file you can make use of the operations as you develop them to observe how they work and make sure they meet the requirements. It is recommended to use the console as output with the `print()` command to display information in the terminal, similar to how `console.log()` works in javascript.

> Remember that you can run the code in this file with the `pipenv run start` command.


## 🧪 How to satisfy unit tests?

This project includes unit tests to validate if the operations meet the requirements, similar to how it would be in a Test Driven Development (TDD) environment. To satisfy the tests it is important to adhere to the variable names and input data types, as well as the output data type.

Are all the attributes of your models exactly the same as shown in the picture? For example: If the picture shows `homeworld_id` in the `People` model, related to the `id` of the `Planets` model, it should be represented in the SQLAlchemy classes using the same names, respecting the use of capital letters.

## 🔥 Feeling confident?

Here are some additional challenges for you to delve deeper into the use of SQLAlchemy

1. Implement the use of paging by using `limit` and `offset` in the `list` functions.

2. Use `try / except` blocks to make your code handle errors without breaking the application.

3. Implement entity-based deletion in `delete` functions. Allow you to specify whether you want to delete based on `id` or by passing the object.

<!-- hide -->

## 🫂 Contributors

Thanks to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Arnaldo Perez (arnaloperez)](https://github.com/arnaloperez) contribution: (build-tutorial) ✅, (documentation) 📖.
  
2. [Alejandro Sanchez (alesanchezr)](https://github.com/alesanchezr),  contribution: (bug detector) 🐛


This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. All contributions are welcome!

This and many other exercises are built by students as part of the 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) by [Alejandro Sánchez](https://twitter.com/alesanchezr) and many other contributors. Find out more about our [Full Stack Developer Course](https://4geeksacademy.com/us/coding-bootcamps/part-time-full-stack-developer), and  [Data Science Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/datascience-machine-learning).You can alse deepdive in the world of cybersecurity with our [Cybersecurity Bootcamp](https://4geeksacademy.com/us/coding-bootcamps/cybersecurity)
<!-- endhide -->