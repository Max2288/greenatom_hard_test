# How install
_$ sudo apt-get update_

_$ sudo apt-get install docker-ce docker-ce-cli 
containerd.io docker-compose-plugin_

_$ git clone https://github.com/Max2288/greenatom_hard_test_

# How run
Add .env file with your data

Go to folder with project and run commands:

- _$ chmod +x init.sh_

- _$ chmod +x start.sh_

- _$ ./init.sh_

- _$ ./start.sh_

# After start
Project runs up three docker containers: database, greenatom, grafana.
## Graphql

Python container which makes request on GraphQL service
and receives data in json format from there. 

Example of data:

    {
        launches {
        mission_id
        mission_name
        rocket {
            rocket_name
            rocket_type
            rocket {
                country
                cost_per_launch
            }
        }
        }
    }

Then this data will be written into database.

# Postgres
Postgres database container which stores saved data received from a GraphQL 
service. It contains three tables: rockets, missions, launches with 
relevant information for each table.

Example table(rockets):

     id |     name     |  type  |             country              | cost_per_launch 
    ----+--------------+--------+----------------------------------+-----------------
      1 | Falcon 1     | rocket | Republic of the Marshall Islands |         6700000
      2 | Falcon 9     | rocket | United States                    |        50000000
      3 | Falcon Heavy | rocket | United States                    |        90000000

Example table(missions):

                id            |                      name                      
    --------------------------+------------------------------------------------
     5eb87cd9ffd86e000604b32a | FalconSat
     5eb87cdaffd86e000604b32b | DemoSat
     5eb87cdbffd86e000604b32c | Trailblazer
     5eb87cdbffd86e000604b32d | RatSat
     5eb87cdcffd86e000604b32e | RazakSat
     5eb87cddffd86e000604b32f | Falcon 9 Test Flight


# Grafana
Grafana is the service that can visualize your data. 


To run grafana on device:

    Go to localhost:3000

    Login: admin

    Password: admin

    Find the dashboards icon and click it

    Open Greenatom in folder General

# .env
## Below should be your data to postgres
    DATABASE - name of database
    DB_USER - database user _(recommended name - postgres)_
    DB_PASSWORD - user password
    DB_HOST - database host
    DB_PORT - database port

# Recommended
## Don't start project twice without deliting volumes _(grafana container depends on main file)_
## If you want to do it run commands:
- _$ docker compose down --volumes_
- _$ ./start.sh_
