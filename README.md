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
- RUN `docker-compose build; docker-compose up`
  - this action reads from the specified dockerfile to build an image
  - this action then deploys that image as specified in the docker-compose file, under `server-local`
- RUN `http://localhost:2424/api/lifecheck/` to confirm you get a response
