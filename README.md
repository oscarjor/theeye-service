
# The Eye Service

Web service that collect application events.

## Conclusions:
1. Added Applications, Sessions and EventCategories Models to support some of the constrains and future requirements.
2. The API will require an API to create sessions for the different applications.
3. The API will require some basic authentication, i used DRF TokenAuthentication.
4. The Session will require some optional metadata to send informations for the session like browser information, hashed user id and ip address information.
5. The events API will need to use Asynchronous Tasks to avoid issues and bottle necks. 
6. The events serializer will require specific validations depending on the selected category 

## Project set up:

Set up the containers:

```sh
$ docker-compose build
```

Run the app:

```sh
$ docker-compose up
```
Run migrations:

```sh
$ docker-compose run --rm app python manage.py migrate
```
Create a super user:

```sh
$ docker-compose run --rm app python manage.py createsuperuser
```

Create basic objects, use the superuser user and password:
1. Browse to http://localhost:3003/admin/auth/user/ and create a new user for the api ex: 'test_app_user'
2. Browse to http://localhost:3003/admin/events/application/ and create a new app ex slug: 'test_app'  
3. Browse to http://localhost:3003/admin/authtoken/tokenproxy/ and create a new user token select the user you created before.
4. Save the created token, it will be used for the api authentication.
5. Browse to http://localhost:3003/admin/events/eventcategory/ and create the categories for the events ex slug: 'page interaction'  


## API 

Browse to http://localhost:3003/swagger/ and click on Authorize type in the token field the following string: Token <<created_token>>, then close (please use the token you created before). Now you will be able to use the api, select the endpoint and click on Tryout and then on Execute.

Example payload:

```sh
{
  "session": "4d33de25-5535-4b2c-bc49-a88ed07175e7",
  "category": "page interaction",
  "name": "pageview",
  "data": {
    "host": "www.consumeraffairs.com",
    "path": "/"
  },
  "timestamp": "2021-01-01 09:15:27.243860"
}
```

## API Documentation

Browse to http://localhost:3003/redoc/ to see the API documentation or download the contract or browse to http://localhost:3003/swagger/ to see the API swagger doc.

Note: Use the sessions endpoint to create a session usign the application slug.

## Tests

Run:

```sh
$ docker-compose run --rm app python manage.py test
```

## Shell

Run:

```sh
$ docker-compose run --rm app python manage.py shell
```
