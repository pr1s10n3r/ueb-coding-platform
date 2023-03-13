# Backend

This is the backend application layer of the _UEB Cofing Platform_.

## Setup Local Development Environment

You will need [Python 3](https://www.python.org/) and [Pipenv](https://pipenv-es.readthedocs.io/es/latest/)

1. Clone the project to your computer using git.
2. Move inside the `backend` directory.
3. Update project to your current version of Python using `pipenv update`.
4. Install dependencies using `pipenv install`.
5. Enter Python virtual environment using `pipenv shell`.
6. Run the project using `python uebcodingplatform_app/manage.py runserver`.

## Response

```json
{
  "time": {
    "actual": 1,
    "expected": 2
  },
  "complexity": {
    "actual": "linear",
    "expected": "cuadratic"
  },
  "output": {
    "actual": "1 2 3 4 5",
    "expected": "1 2 3 4 5"
  }
}
```
