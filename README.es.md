---
title: "Construye una base de datos de Star Wars con SQLAlchemy"
subtitle: "Construye una base de datos de películas de Star Wars, creando modelos e implementando relaciones. Aprende a realizar operaciones CRUD con SQLAlchemy."
tags: ["python","json","postgresql","data-structures","sql","sqlalchemy"]
---

<!--hide-->
# Construye una base de datos de Star Wars con SQLAlchemy
<!--endhide-->

## Base de datos de Star Wars
El universo de Star Wars necesita una base de datos para almacenar la información de todos los planetas y sus habitantes, asi como tambien los datos de las peliculas, los personajes que las integran y los planetas donde transcurren... La fuerza es intensa en este proyecto!

## 🌱 ¿Cómo comenzar este proyecto?

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

1. Ejecuta el comando `pipenv run migrate` para generar una nueva migración.

2. Ejecuta el comando `pipenv run upgrade` para migración aplicar las migraciones a tu base de datos.

> Es necesario seguir estos pasos la primera vez que inicias tu repo y de luego cada vez que hagas cambios a la estructura del modelo

<!-- ## ✅ Autoevaluación

+ Evalúa tu código con el comando `$ pipenv run test` -->

## 📝 Instrucciones

### En el archivo `models.py`

1. Utiliza python para representar en SQLAlchemy el modelo que se muestra en la imagen:

![Modelo de base de datos de Star Wars](https://raw.githubusercontent.com/4GeeksAcademy/sqlalchemy-operations/master/docs/assets/model.png)

2. Las tablas deben tener los mismos atributos o columnas que se reflejan en el modelo

3. Debes implementar las llaves foráneas en los casos en que haya relaciones.

4. Implementa el uso de propiedades de tipo `relationship` para acceder a los datos que estén relacionados.

5. Para cada modelo escribe una funcion `__repr__` para especificar como se **representan** los objetos mostrados en consola. Esto te ayuda a mejorar la experiencia de desarrollo del proyecto.

Solo edita las clases para completar los columnas y las relaciones que se reflejan en el modelo

### En el archivo `db_operations.py`

En este archivo encontrarás las operaciones que deben realizarse para administrar la informacíon en la base de datos, usualmente se desarrollan los métodos CRUD(**C**reate, **R**ead, **U**pdate,**D**elete), junto con otros que respondan a los requerimientos del proyecto.

#### Escribe el código que realice la tarea que indica el nombre de la función

```python
# Planetas
def planet_create(): # Crear
def planet_get(): # Buscar por id
def planet_find_by_name(): # Busca uno por nombre
def planet_list(): # Lista de todos los planetas
def planet_edit(): # Editar los datos especificando el id
def planet_delete(): # Eliminar especificando el id

# Peliculas
def film_create(): # Crear
def film_get(): # Buscar por id
def film_get_episode(): # Buscar por numero de episodio
def film_list(): # Lista de todas las películas
def film_edit(): # Editar los datos especificando por el id
def film_delete(): # Eliminar especificando por el id

# Personas
def people_create(): # Crear
def people_get(): # Buscar por id
def people_list():# Traer lista
def people_edit(): # Editar los datos especificando por el id
def people_delete(): # Eliminar especificando por el id

# Operaciones con relaciones
def film_add_locations(): # Agregar un registro dado el id de la pelicula y el id del planeta
def film_add_characters():# Agregar un registro dado el id de la pelicula y el id de la persona
def film_remove_locations(): # Eliminar un registro dado el id de la pelicula y el id del planeta
def film_remove_characters(): # Eliminar un registro dado el id de la pelicula y el id de la persona
```

#### Tipos de dato de las entradas y las salidas

Como parte del reto debes especificar los tipos de datos que van a recibir cada una de las funciones, asi como utilizar un tipo de dato específico como salida. Para ello debes tener en consideración los siguientes aspectos

- Las funciones `create` deben recibir todos los datos que necesite la tabla, excepto el id que se genera automáticamente. Estas funciones deben retornar el objeto creado.

- Las funciones `get` o ` find` deben retornar una sola entidad. Puede ser el primer resultado que coincida con la búsqueda.

- Las funciones `edit` tambien reciben todos los datos de la entidad como parámetros, siendo el `id` obligatorio y el resto opcionales de manera que solo se modifiquen los datos especificados y el resto se preserve como está. Estas funciones tambien deben retornar el objeto editado.

- Las funciones `delete` deben retornar `True` si la eliminación se realizó con exito

- Las funciones de las tablas pivote `locations` y `characters` hacen todas las operaciones con las llaves foráneas (foreign keys) por lo que solo necesitan el `id` de los elementos con los que se van a relacionar.

- Recuerda utilizar la convención [snake_case](https://es.wikipedia.org/wiki/Snake_case) para el nombre de las variables, por ejemplo: `people_id`.

### En el archivo `app.py`

En este archivo puedes hacer uso de las operaciones a medida que las vayas desarrollando para observar como funcionan y asegurarte que cumplan con los requisitos. Se recomienda utilizar la consola como salida con el comando `print()` para mostrar informacion en la terminal, parecido a como funciona `console.log()` en javascript.

> Recuerda que puedes ejecutar el codigo de este archivo con el comando `pipenv run start`


## 🧪 ¿Cómo satisfacer las pruebas unitarias?

Este proyecto incluye pruebas unitarias para validar si las operaciones cumplen con los requisitos planteados, similar a como sería en un entorno de desarrollo orientado a pruebas (TDD). Para satisfacer las pruebas es importante apegarse a  los de nombres de variables y tipos de datos de entrada, asi como tambien el tipo de dato de salida.

¿Todos los atributos de tus modelos son exactamente iguales a como se muestran en la foto? Por ejemplo: Si en la foto aparece `homeworld_id` en el modelo `People`, relacionado con el `id` del modelo `Planets`, asi mismo de representarse en las clases de SQLAlchemy utilizando los mismos nombres, respetando el uso de las mayúsculas.

## 🔥 ¿Te sientes confiado?

Aquí hay unos desafíos adicionales para que profundices mas en el uso de SQLAlchemy

1. Implementa el uso de paginación utilizando `limit` y `offset` en las funciones `list`.

2. Usa bloques `try / except` para hacer que tu código maneje los errores sin romper la aplicación.

3. Implementa la eliminación en base a entidades en las funciones `delete`. Permite que se especifique si se desea eliminar en base al `id` o pasando el objeto.

<!-- hide -->

## 🫂 Colaboradores

Gracias a estas personas maravillosas ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

1. [Arnaldo Perez (arnaloperez)](https://github.com/arnaloperez) cotribución: (build-tutorial) ✅, (documentación) 📖
  
2. [Alejandro Sanchez (alesanchezr)](https://github.com/alesanchezr),  contribución: (detector bugs) 🐛


Este proyecto sigue la especificación [all-contributors](https://github.com/kentcdodds/all-contributors). ¡Todas las contribuciones son bienvenidas!

Este y otros ejercicios son usados para [aprender a programar](https://4geeksacademy.com/es/aprender-a-programar/aprender-a-programar-desde-cero) por parte de los alumnos de 4Geeks Academy [Coding Bootcamp](https://4geeksacademy.com/us/coding-bootcamp) realizado por [Alejandro Sánchez](https://twitter.com/alesanchezr) y muchos otros contribuyentes. Conoce más sobre nuestros [Cursos de Programación](https://4geeksacademy.com/es/curso-de-programacion-desde-cero?lang=es) para convertirte en [Full Stack Developer](https://4geeksacademy.com/es/coding-bootcamps/desarrollador-full-stack/?lang=es), o nuestro [Data Science Bootcamp](https://4geeksacademy.com/es/coding-bootcamps/curso-datascience-machine-learning).Tambien puedes adentrarte al mundo de ciberseguridad con nuestro [Bootcamp de ciberseguridad](https://4geeksacademy.com/es/coding-bootcamps/curso-ciberseguridad).
<!-- endhide -->