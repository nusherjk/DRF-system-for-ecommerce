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
   - still authenticated users can  do product create. they shouldnt. 
3. create user roles.
   - ~~added Provider Role~~
4. search endpoints.
5. ~~test out why images are not getting uploaded.~~
   ~~1. test in the staging server.~~
   ~~2. check the slugs.~~
    
6. plan the whole api endpoints.
7. ~~Order still needs to send an fake user id but it should not~~
8. ~~User creation is not working need better solution~~
9. ~~Order get method only show the list of orders by that perticular user~~
10. features 


### Explanations

1. 3 types of users can consists in this system.
2. Admin, Provider, Customer
   - an additional alluser
3. Customer can add reviews, order everything
4. alluser will have readonly view of everything
5. Provider can add products, numbers and all
6. admin can add categories and remove products