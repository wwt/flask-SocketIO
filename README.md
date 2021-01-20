# Prerequisites

- Download and Install python3 from the following link

  - `https://www.python.org/downloads/`

- Download and Install Node.js from the following link
  - `https://nodejs.org/en/download/`

# Launch the app

## Python API

- Launch terminal

- Navigate to ./api under your project repository

- Stay up to date with modules by installing all dependencies from requirements.txt

  - `pip3 install -r requirements.txt`

- Run the following command to create database. This will end up creating 'database.db' file under `./api` folder.
  - `python3 createDatabase.py`
- Run the following command to bring up the API
  - `python3 app.py`

## React Client

- Launch another terminal

- Navigate to `./client` under your project repository

- Stay up to date with modules by installing all dependencies from package.json

  - `npm install`

- Run the following command to bring up the API

  - `npm start`

- Launch a browser access the followign link
  - `http://localhost:3000/`
