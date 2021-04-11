# DRF-system-for-ecommerce

A Django Rest framework Based API for E-commerce system . build on docker image


## Dependancy

- Django Rest Framework
- Postgres
- Docker


## Installation

- clone the repository
- open terminal/cmd in the root directory of the repository
- run ``` docker-compose up ```


## Additional

- for migration 
`docker-compose run web manage.py migrate`


##  staging

- https://doogdoogi.herokuapp.com/


### TODO

1. ~~Add product has bugs .. have to fix them~~
2. create category and product,  other individual features should have different permission classes.
3. create user roles.
4. search endpoints.