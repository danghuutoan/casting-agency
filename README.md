# Casting Agency API Backend
Casting Agency helps simplify the casting process
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

-   [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

-   [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

-   [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Running the server

From within the project root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_ENV=development
python3 run.py
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

Deploy server using gunicorn

```
    gunicorn -b :8080 run:app
```

Deploy server to heroku

# DB migration

```
heroku run python manage.py db init --app casting-service

```
# Remote Heroku psql 

```
heroku pg:psql --app casting-service
```

# Push data from local database to remote database 

```
heroku pg:push casting_agency DATABASE_URL --app casting-service
```
## Auth0 Authorize Link
the app is not shipped with front end so please use the link below for login
https://dev-to9u3yj6.auth0.com/authorize?audience=casting_service&response_type=token&client_id=gLQbqpEH5ribwnbZJiGRwW4C4RW4puvS&redirect_uri=http://localhost:8100/tabs/user-page&prompt=login
## Testing

To run the tests, run

```
dropdb casting_agency
createdb casting_agency
psql casting_agency < casting_agency.psql
python test_movie.py
python test_actor.py
```

## Error handling

Errors are returned as JSON objects in the following format

```
{
    "success": False,
    "error": 404,
    "message": "Not found"
}
```

The API will return three types of error when requests fail

-   404 : Not found
-   422 : Unprocessable
-   400 : Bad request

## Endpoints
url : https://casting-service.herokuapp.com/
### GET /actors

-   General:
    -   get all the available actors
    -   Curl command
        ```bash
        curl http://127.0.0.1:8080/actors/
        ```
    -   Return: An object similar to the on below
        ```json
        {
        "actors": [
            {
            "age": 5, 
            "gender": 1, 
            "id": 1, 
            "movies": [
                {
                "id": 1, 
                "title": "The Movie 1"
                }, 
                {
                "id": 3, 
                "title": "The Movie 3"
                }
            ], 
            "name": "The Actor 1"
            }, 
            {
            "age": 10, 
            "gender": 2, 
            "id": 2, 
            "movies": [
                {
                "id": 3, 
                "title": "The Movie 3"
                }, 
                {
                "id": 4, 
                "title": "The Movie 4"
                }
            ], 
            "name": "The Actor 2"
            }, 
            {
            "age": 20, 
            "gender": 2, 
            "id": 3, 
            "movies": [
                {
                "id": 2, 
                "title": "The Movie 2"
                }, 
                {
                "id": 4, 
                "title": "The Movie 4"
                }
            ], 
            "name": "The Actor 3"
            }, 
            {
            "age": 35, 
            "gender": 2, 
            "id": 4, 
            "movies": [], 
            "name": "The Actor 4"
            }, 
            {
            "age": 40, 
            "gender": 1, 
            "id": 5, 
            "movies": [], 
            "name": "The Actor 5"
            }, 
            {
            "age": 50, 
            "gender": 2, 
            "id": 6, 
            "movies": [], 
            "name": "The Actor 6"
            }, 
            {
            "age": 6, 
            "gender": 1, 
            "id": 7, 
            "movies": [], 
            "name": "The Actor 7"
            }
        ], 
        "success": true
        }        
        ```

### GET /movies

-   General:
    -   get all the available movies
    -   Curl command
        ```bash
        curl http://127.0.0.1:8080/movies/
        ```
    -   Return: An object similar to the on below
        ```json
        {
        "movies": [
            {
            "actors": [
                {
                "id": 1, 
                "name": "The Actor 1"
                }
            ], 
            "id": 1, 
            "title": "The Movie 1"
            }, 
            {
            "actors": [
                {
                "id": 3, 
                "name": "The Actor 3"
                }
            ], 
            "id": 2, 
            "title": "The Movie 2"
            }, 
            {
            "actors": [
                {
                "id": 1, 
                "name": "The Actor 1"
                }, 
                {
                "id": 2, 
                "name": "The Actor 2"
                }
            ], 
            "id": 3, 
            "title": "The Movie 3"
            }, 
            {
            "actors": [
                {
                "id": 2, 
                "name": "The Actor 2"
                }, 
                {
                "id": 3, 
                "name": "The Actor 3"
                }
            ], 
            "id": 4, 
            "title": "The Movie 4"
            }
        ], 
        "success": true
        }
        ```
### GET /movies/<int:id>

-   General:
    - Get an movie by the given id
    - curl command 
    ```bash
    curl http://127.0.0.1:8080/movies/1
    ```
- Sample response:
    ```json
    {
    "movies": {
        "actors": [
        {
            "id": 1, 
            "name": "The Actor 1"
        }
        ], 
        "id": 1, 
        "title": "The Movie 1"
    }, 
    "success": true
    }
    ```

### GET /actors/<int:id>

-   General:
    - Get an actor by the given id
    - curl command 
    ```bash
    curl http://127.0.0.1:8080/actors/1
    ```
- Sample response:
    ```json
    {
    "actors": {
        "age": 5, 
        "gender": 1, 
        "id": 1, 
        "movies": [
        {
            "id": 1, 
            "title": "The Movie 1"
        }, 
        {
            "id": 3, 
            "title": "The Movie 3"
        }
        ], 
        "name": "The Actor 1"
    }, 
    "success": true
    }
    ```

### POST /actors

-   General:   
    -   create a new actor with the given attribute in json body
    - curl command :
    ```bash
    curl http://127.0.0.1:8080/actors -X POST -H "Content-Type: application/json" -d '{
    "name": "Actor 2",
    "gender": 2,
    "age": 25,
    "movies": [1]
    }'
    ```
-   Sample response:
    ```json
    {
    "actors": [
        {
        "age": 25, 
        "gender": 2, 
        "id": 12, 
        "movies": [
            {
            "id": 1, 
            "title": "a title"
            }
        ], 
        "name": "Actor 2"
        }
    ], 
    "success": true
    }
    ```

### POST /movies

-   General:   
    -   create a new movie with the given attribute in json body
    - curl command :
    ```bash
    curl http://127.0.0.1:8080/movies -X POST -H "Content-Type: application/json" -d '{
    "title": "movie 4",
    "release_date": "2020-02-02 12:03:03"
    }'
    ```
-   Sample response:
    ```json
    {
    "movies": [
        {
        "actors": [], 
        "id": 5, 
        "release_date": "Sun, 02 Feb 2020 05:03:03 GMT", 
        "title": "movie 4"
        }
    ], 
    "success": true
    }
    ```

### DELETE /actors/<int:id>

-   General:   
    -   delete an actor with the given attribute in json body
    - curl command :
    ```bash
    curl http://127.0.0.1:8080/actors/9 -X DELETE
    ```
-   Sample response:
    ```json
    {
    "delete":9,
    "success": true
    }
    ```

### DELETE /movies/<int:id>

-   General:   
    -   delete a movie with the given attribute in json body
    - curl command :
    ```bash
    curl http://127.0.0.1:8080/movies/9 -X DELETE
    ```
-   Sample response:
    ```json
    {
    "delete":9,
    "success": true
    }
    ```

### PATCH /actors/<int:id>

-   General:   
    -   update an actor with the given attribute in json body
    - curl command :
    ```bash
    curl http://127.0.0.1:8080/actors/9 -X patch -d '{"name":"toan"}'
    ```
-   Sample response:
    ```json
    {
    "success": true,
    "update": {
        "age": 2,
        "gender": 1,
        "id": 2,
        "movies": [
        {
            "id": 1,
            "title": "a title"
        },
        {
            "id": 3,
            "title": "movie 3"
        },
        {
            "id": 4,
            "title": "movie 4"
        }
        ],
        "name": "toan"
    }
    }
    ```