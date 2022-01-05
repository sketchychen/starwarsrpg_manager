# Star Wars RPG (FFG) Manager
an unofficial character and campaign manager for Star Wars RPG (FFG)


```
brew services start mongodb-community
flask run
```


## User stories:
- As a _User_, I want to look up items, vehicles, species, and classes.
- As a _User_, I want to manage my owned characters and owned campaigns.

- As a _Player_, I want to access my involved campaigns.

- As a _GM_, I want to manage my owned campaigns.
- As a _GM_, I want to provide timeline updates to my campaigns.
- As a _GM_, I want to create characters for _Players_ to claim.
- As a _GM_, I want to create custom items for characters to use in my campaigns.




## Running the server locally via docker
### Pre-reqs
- the feature utilizes docker and docker-compose to run.
- download docker to your local machine

### running
- `virtualenv venv` - setup your virtual environment (venv)
- `source venv/bin/activate` - turns on the venv
- `deactivate` - turn off the venv
- RUN `docker-compose build server-local; docker-compose up -d`
  - this action:
    - reads from the specified dockerfile to build an image
    - then deploys that image as specified in the docker-compose file, under `server-local`
    - `-d` flag specifies to run the the docker container in the background
      - run `docker ps` to see running containers
      - run `docker-compose down` to shutdown any running containers
  - NOTES
    - this has live-reloading built in
    - if you want to have the logs run to your terminal, remove the `-d` flag
- RUN `http://localhost:2424/api/lifecheck/` to confirm you get a response

### other docker notes
  - if you're building a lot of images, they hang around.
  - `docker ps` - see all your docker images
  - `docker rm <IMAGE_ID>` - to remove them one by one
  - `docker image prune -f` - cleans up those images
