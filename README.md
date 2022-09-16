# Rendom_project


# Setup project
~~~
git clone https://github.com/vikashkumarsaini9815/Rendom_project
~~~
# installation
~~~
cd rendom
pip install -r requairments.txt
~~~~
# Setup DB migration
~~~
create a models Users

run commands
python manage.py makemigrations
python manage.py migrate
~~~
# Runserver
~~~
python manage.py runserver
~~~
# Rest api for employe
~~~
http://127.0.0.1:8000/employe/
Request Body :
  {
	"id": 4936,
	"uid": "25646c6a-b3f2-4c3a-8757-b212f7a4f038",
	"password": "YMuwv7VWhm",
	"first_name": "Weldon",
	"last_name": "Quigley",
	"username": "weldon.quigley",
	"email": "weldon.quigley@email.com",
	"avatar": "https://robohash.org/debitisquisomnis.png?size=300x300\u0026set=set1",
	"gender": "Non-binary",
	"phone_number": "+972 916.339.1137",
	"social_insurance_number": "707806063",
	"date_of_birth": "1993-08-21"
}
Response Body :
  {
	"id": 4936,
	"uid": "25646c6a-b3f2-4c3a-8757-b212f7a4f038",
	"password": "YMuwv7VWhm",
	"first_name": "Weldon",
	"last_name": "Quigley",
	"username": "weldon.quigley",
	"email": "weldon.quigley@email.com",
	"avatar": "https://robohash.org/debitisquisomnis.png?size=300x300\u0026set=set1",
	"gender": "Non-binary",
	"phone_number": "+972 916.339.1137",
	"social_insurance_number": "707806063",
	"date_of_birth": "1993-08-21"
}
~~~
