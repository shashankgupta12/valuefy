About the project
----------------------
This project encapsulates a Django REST TO-DO API which has the following specifics:
* REST API built using Django Rest Framework (DRF)
* Includes CRUD operations over the endpoints **/todos** (for POST) and **/todos/\<id>** (for GET, PUT, DELETE)
* Follows a Test Driven Development (TDD) approach and includes a test suite for each CRUD operation
* Code is documented using doc strings and follows PEP8 coding style

### How to run the project
Below is the sequential set of commands to be executed for successfully running the project in this repository.
* Clone the repository:
  * $ git clone https://github.com/shashankgupta12/valuefy.git
* Change directory:
  * $ cd valuefy/REST
* Create and activate a python3.6 virtual environment:
  * $ virtualenv -p /usr/your-path-to-python/python3.6 venv
  * $ source venv/bin/activate
* Install requirements:
  * $ pip install -r requirements.txt
* Finally make migrations and run:
  * $ python3 server/manage.py makemigrations
  * $ python3 server/manage.py migrate
  * $ python3 server/manage.py runserver

Finally, visit http://127.0.0.1:8000/ in your browser and check out the various API endpoints viz. http://127.0.0.1:8000/todos and http://127.0.0.1:8000/todos/\<id>.
