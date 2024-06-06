<!--hide-->
# Base de datos de Star Wars
<!--endhide-->

El universo de Star Wars necesita una base de datos para almacenar la información de todos los planetas y sus habitantes, asi como tambien los datos de las peliculas, los personajes que las integran y los planetas donde transcurren... La fuerza es intensa en este proyecto!

## 🌱 Cómo comenzar este proyecto

Este proyecto viene con los archivos necesarios para comenzar a trabajar de inmediato.

Recomendamos abrir este mismo repositorio usando un entorno de desarrollo como [Codespaces](https://4geeks.com/es/lesson/tutorial-de-github-codespaces) (recomendado) o [Gitpod](https://4geeks.com/es/lesson/como-utilizar-gitpod). Alternativamente, puedes clonarlo en tu computadora local usando el comando `git clone`.

Este es el repositorio que necesitas abrir:

```txt
https://github.com/4GeeksAcademy/sqlalchemy-operations
```

## 💻 Instalación

1. Instala las dependencias del proyecto `$ pipenv install`.

2. Entra dentro del *virtual environment* `$ pipenv shell`

## 🌐 Migración de tu base de datos

1. Ejecuta el comando `pipenv run db_update` para generar una nueva migración.

2. Ejecuta el comando `pipenv run db_upgrade` para migración aplicar las migraciones a tu base de datos.

> Es necesario seguir estos pasos la primera vez que inicias tu repo y de luego cada vez que hagas cambios a la estructura del modelo

<!-- ## ✅ Autoevaluación

+ Evalúa tu código con el comando `$ pipenv run test` -->

## 📝 Instrucciones

### En el archivo `models.py`

1. Crea el código crear en la base de datos, el modelo que se presenta en la imagen:

![Modelo de base de datos de Star Wars](https://raw.githubusercontent.com/4GeeksAcademy/sqlalchemy-operations/master/docs/assets/model.png)

2. Las tablas deben tener los mismos datos que se reflejan en el modelo

3. Debes implementar las llaves foráneas en los casos en que haya relaciones.

4. Implementa el uso de propiedades de tipo `relationship` para acceder a los datos que estén relacionados.

5. (Opcional) Puedes escribir funciones para seralizar los objetos de SQLAlchemy en diccionarios; asi como tambien una funcion `__repr__` para especificar como aparecerán los objetos mostrados en consola. Esto puede ayudarte a facilitar la experiencia de desarrollo del proyecto.

Solo edita las clases para completar los columnas y las relaciones que se reflejan en el modelo

### En el archivo `db_operations.py`

En este archivo encontrarás las operaciones que deben realizarse para manejar la informacíon en la base de datos

1. Escribe el código que realice la tarea que indica el nombre de la funcion, estas son:

```python
# Planetas
def planet_create(): # Crear
def planet_get(): # Buscar por llave primaria
def planet_find_by_name(): # Buscar por nombre
def planet_list(): # Traer lista
def planet_edit(): # Editar los datos especificando por el id
def planet_delete(): # Eliminar especificando por el id
# Peliculas
def film_create(): # Crear
def film_get(): # Buscar por llave primaria
def film_get_episode(): # Buscar por numero de episodio
def film_list(): # Traer lista
def film_edit(): # Editar los datos especificando por el id
def film_delete(): # Eliminar especificando por el id
# Personas
def people_create(): # Crear
def people_get(): # Buscar por llave primaria
def people_list():# Traer lista
def people_edit(): # Editar los datos especificando por el id
def people_delete(): # Eliminar especificando por el id
# Operaciones con relaciones
def film_add_locations(): # Agregar un registro dado el id de la pelicula y el id del planeta
def film_add_characters():# Agregar un registro dado el id de la pelicula y el id de la persona
def film_remove_locations(): # Eliminar un registro dado el id de la pelicula y el id del planeta
def film_remove_characters(): # Eliminar un registro dado el id de la pelicula y el id de la persona
```

### En el archivo `app.py`

En este archivo puedes hacer uso de las operaciones a medida que las vayas desarrollando para observar como funcionan y asegurarte que cumplan con los requisitos. Se recomienda utilizar la consola como salida para con el comando `print()` para mostrar informacion en la terminal, parecido a como funciona `console.log()` en javascript.

> Recuerda que puedes ejecutar el codigo de este archivo con el comando `pipenv run start`

<!-- hide -->

## Colaboradores

Gracias a estas personas maravillosas ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Arnaldo Perez (arnaloperez)](https://github.com/arnaloperez) cotribución: (build-tutorial) ✅, (documentación) 📖
  
2. [Alejandro Sanchez (alesanchezr)](https://github.com/alesanchezr),  contribución: (detector bugs) 🐛


Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). ¡Todas las contribuciones son bienvenidas!

Este y otros ejercicios son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por parte de los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) realizado por [Alejandro Sánchez](https://twitter.com/alesanchezr) y muchos otros contribuyentes. Conoce más sobre nuestros [Cursos de Programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero?lang=es) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack/?lang=es), o nuestro [Data Science Bootcamp](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).Tambien puedes adentrarte al mundo de ciberseguridad con nuestro [Bootcamp de ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad).
<!-- endhide -->