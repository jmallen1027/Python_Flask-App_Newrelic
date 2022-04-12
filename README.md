**Overview**

This project is for learning Microservices Technologies by using Observability Tools such as New Relic, Jaeger, and others. The application is an online book store where a user can create an account, log in, and purchase a book. The book store admin is responsible for the inventory and pricing. This project is still in development.

**Run the app**

The app includes four services consisting of a Frontend, User service, Product(Book Service), and order service. The application can be spun up with individual Dockerfiles, Docker Compose, and individually in a Python virtual environment.

**Databases**

The application includes configurations for both Sqlite and Mysql in the services app.py files. The User, Order, and Book (Product) services share a MySQL server in Docker Compose. 

Testing Services. While building the application I used Postman to test the APIs and later used JMeter. I utilized JMeter for testing purposes.

**Notes**

Please be aware this app is still in development. You may see multiple lines commented out and nonrelevant python packages. I instrumented this application with multiple monitoring tools and left some older python packages in the requirments.txt file. The application requires additional steps after starting it up. But it functions. I'll list the commands and instructions below.

**Running the app with Docker Compose**

Run these commands after building and running the docker compose file. The app will spin up with some errors with the database. Just docker exec into the DB and Python Services and run these commands.

Please update the apps.py and Dockerfiles of each service with the DB password or New Relic Licesnse Keys. There are backup Dockerfiles in the each service directory if you choose not to use New Relic and want to spin it up normally. 

Below are the commands for running the App with Docker Compose. There is a backup Docker Compose File is you want to run the app without MySql named docker-compose.yaml.bk in the frontend directory. Just skip the MYSQL Steps and continue with the migrations. 

I used Post Man to create the books. Send a Post Request to the Book Service API and use form data. There is a screenshot in the the book Details. 

docker-compose build (in the user directory)

docker-compose up

docker exec -it mysql_db_1 /bin/bash

mysql -uroot -p

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PASSWORD;

CREATE USER 'newrelic'@'localhost' IDENTIFIED WITH mysql_native_password BY 'PASSWORD';

FLUSH PRIVILEGES;

CREATE DATABASE book; ## Create user and order Databases to. Put order inbetween `` or change the name.

docker exec -it book_app /bin/bash ## Do this for the user and order service as well.

flask db upgrade

**API Url Changes**

If running locally and not in docker you will need to change the URL settings in the code. Please see below for running locally.

/order/routes.py

USER_API_URL = 'http://127.0.0.1:5001/api/user

#USER_API_URL = 'http://user-app:5001/api/user' ## user-app is the container name. If yours is something else then change it ##

/frontend/api/init.py

USER_API_URL = 'http://127.0.0.1:5001'

BOOK_API_URL = 'http://127.0.0.1:5002'

ORDER_API_URL = 'http://127.0.0.1:5003'

**New Relic Setup**

Go to Newrelic.com and create a free account. No credit card or payment information is required. Go to guided setup to quickly install the agent on your host.

APM Setup - The Dockerfiles are set up with the Newrelic Python Agent. Just change the licenses keys. The keys can be obtained in the newrelic.ini file or the account settings.

**Useful Links for New Relic**

Sign up for Free New Relic Account - https://newrelic.com/

NRQL Lessons for learning the New Relic Query Language - https://opensource.newrelic.com/projects/newrelic/nr1-learn-nrql

New Relic Docs - https://docs.newrelic.com/

New Relic Python Agent for Docker - https://docs.newrelic.com/docs/apm/agents/python-agent/installation/install-python-agent-docker

New Relic IM Agent - https://docs.newrelic.com/docs/infrastructure/install-infrastructure-agent/get-started/install-infrastructure-agent
