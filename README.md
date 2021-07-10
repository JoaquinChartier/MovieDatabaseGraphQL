**MovieDatabaseGraphQL**

This project is developed in Django, a Python framework, using a GraphQL implementation.

The purpose of this system is develop a fast, mainteinable, open source API with GraphQL.

Made it using a public movie´s dataset. See more here: [*https://data.world/jamesgaskin/movies.*](https://data.world/jamesgaskin/movies)

**Instructions**

The system come with a preloaded version of the dataset, however you can manually load it by yourself.

- Delete *db.sqlite3* file in root folder

- Run in the root folder

  ```
  python manage.py migrate
  ```

- After that, run

  ```
  python manage.py runserver
  ```

- And run this, positioned in "Tools" folder

  ```
  python load_movies.py
  ```

Database is loaded!

To execute query´s you can go to: http://127.0.0.1:8000/movies and execute it with Postman or something like that.

**SignUp**

```
POST http://127.0.0.1:8000/signup/

(body)
{
    "username":"my_user",
    "password":"p4ssw0rd"
}
```

**Login**

```
POST http://127.0.0.1:8000/login/

(body)
{
    "username":"my_user",
    "password":"p4ssw0rd"
}
```

**Example querys**

- Query all movies

```
GET http://127.0.0.1:8000/movies

(GraphQL body)
query {
    allMovies {
        id
        title
    }
}
```

- Query actors who´s name is or contains "John"

```
GET http://127.0.0.1:8000/movies

(GraphQL body)
query {
    actorsBy(name:"John") {
        id
        name
        gender
    }
}
```

- Query characters who´s name is or contains "Mary" and order in ascending by "credit_order"

```
GET http://127.0.0.1:8000/movies

(GraphQL body)
query {
    charactersBy(characterName:"Mary", orderByAsc:"credit_order") {
        id
        characterName
        creditOrder
    }
}
```

