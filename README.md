El presente repositorio contiene una API REST desarrollada utilizando Flask y SQLite 3.

El repositorio tiene cuatro archivos principales:

1. **empresa.db**
   La base de datos. Contiene dos tablas: "abonados" y "servicios".

2. **db.py**
   Se encarga de establecer la conexión con la base de datos y de crear las tablas "abonados" y "servicios" en caso de que no hayan sido creadas. Las tablas quedan conformadas de la siguiente manera:

   | abonados    |
   | ----------- |
   | id          |
   | nombre      |
   | servicio_id |

   | servicios |
   | --------- |
   | id        |
   | tipo      |
   | precio    |

3. **db_controller.py**
   Implementa las operaciones CRUD (Create, Update, Read y Delete).

4. **app.py**
   Es la API propiamente dicha. Los endpoints quedan configurados de la siguiente manera:

   | Endpoint                           | Método HTTP | Descripción                                             |
   | ---------------------------------- | ----------- | ------------------------------------------------------- |
   | https://localhost:8000/abonados    | GET         | Obtiene una lista de todos los abonados                 |
   | https://localhost:8000/servicios   | GET         | Obtiene una lista de todos los servicios                |
   | https://localhost:8000/abonado     | POST        | Crea un nuevo abonado                                   |
   | https://localhost:8000/servicio    | POST        | Crea un nuevo servicio                                  |
   | https://localhost:8000/abonados    | PUT         | Actualiza abonado                                       |
   | https://localhost:8000/servicios   | PUT         | Actualiza servicio                                      |
   | https://localhost:8000/abonado/id  | DELETE      | Elimina abonado particular (el que coincide con el ID)  |
   | https://localhost:8000/servicio/id | DELETE      | Elimina servicio particular (el que coincide con el ID) |
   | https://localhost:8000/abonado/id  | GET         | Obtiene abonado particular (el que coincide con el ID)  |
   | https://localhost:8000/servicio/id | GET         | Obtiene servicio particular (el que coincide con el ID) |
