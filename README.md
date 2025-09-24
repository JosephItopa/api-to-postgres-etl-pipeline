### CONTAINERIZED ETL PIPELINE
#### INTRODUCTION
##### The ricky and morty API contains several data on the movie, characters, and adventure of ricky and morty. 
##### This ETL pipeline will extract the records from the API, and carry out some transformation, then load on to postgres database which is hosted on docker.

#### HOW TO RUN THE PROJECT
##### Step 1: Clone the repo using:- git clone https://github.com/JosephItopa/api-to-postgres-etl-pipeline.git

##### Step 2: Run the script with this command: bash run_pipeline.sh

##### Step 3: To connect to the database while docker is running, use this command:- 
###### i) docker exec -it postgres-image bash
###### ii) psql -U myuser -d rickandmortyapi

##### Step 4: IF you are having problem ingesting the data to the database, then use the SQL code below to create a table named, 'rickyandmorty'
#### CREATE TABLE
##### CREATE TABLE rickyandmorty (
#####   id SERIAL PRIMARY KEY,
#####   name VARCHAR(50) NOT NULL,
#####   species VARCHAR(100) UNIQUE NOT NULL,
#####   type VARCHAR(100) UNIQUE NOT NULL,
#####   gender VARCHAR(100) UNIQUE NOT NULL,
#####   email VARCHAR(100) UNIQUE NOT NULL,
#####   created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#####   origins VARCHAR(100) UNIQUE NOT NULL,
#####   locations VARCHAR(100) UNIQUE NOT NULL,
#####   episode VARCHAR(100) UNIQUE NOT NULL,
#####   url VARCHAR(100) UNIQUE NOT NULL
#####   );

##### Step 5: After that, restart the docker service by the docker service again. 