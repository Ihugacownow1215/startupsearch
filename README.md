# startupsearch

## Routes

admin/ for crud operations in admin console
mvpapp/avg-funding-by-person/<str:person_id>
mvpapp/companies-by-person/<str:person_id>
mvpapp/investors-by-company/<str:company_name>

## Setup

```
pip install django
pip install pandas

python3 -m venv env
source env/bin/activate

python3 manage.py runserver
```
