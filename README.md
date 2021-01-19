# Python API application 

## Initial setup (run once per workstation)
There's two options:

### Manage venv via IntelliJ
* Select `File` > `Project Structure`
* In the `Project` tab, specify a `New` Project SDK (as you won't have one), and click on `Python SDK`
* Change `Location` to point to a `./api/venv` folder; it will create an empty directory for your virtualenv
* Assuming python is already installed and you don't have an existing environment, select `/usr/local/bin/python3.7`
* Click Apply and Ok after the virtualenv is created (the default name is `venv`, but it can be whatever you want it to be)
* Make sure you add it to `.gitignore` if it's a new name so it doesn't get pushed to the repo

### Manage venv via terminal
* Navigate to `./api`
* Create virtual environment with any name, `DEV` is used as an example
    * `python3 -m venv DEV`

* Activate virtual environment `DEV`
	* `source DEV/bin/activate`
	
* When no longer in use, deactivate current active virtual environment
    * `deactivate`

### After initial set up:
* Stay up to date with modules by installing all dependencies from requirements.txt
	* `pip install -r requirements.txt`

## Run the application

1. Activate virtual environment `DEV`:   

    `source DEV/bin/activate`

1. Run all API tests: 
* Make sure you have a database running i.e. `docker-compose up db` or an instance of postgres running
* `pytest`
	
1. Run Flask app: 

	`flask run`
### Manage packages
1. Make sure local packages are up to date (potentially after each `git pull`)
    
    `pip install -r requirements.txt`
1. Add new package in ripple-app api:

   1. `pip install package_name`
   
   1. `pip freeze > requirements.txt`
   
   `requirements.txt` will contain changes, which need to be pushed into repository 
	
### Database management commands
1. Creates a new migration repository(creates a folder `migrations` with 4 files)
    
   `flask db init`
1. To read help: 

    `flask db --help`
1. Two steps to update database   
    1. Generate new revision:
    
    `flask db migrate`
  
    1. Upgrade database to latest revision:
    
    `flask db upgrade`
    
    
 ### Notes:
 For .flaskenv and .env, docker-compose currently has a bug where it doesn't parse `export` properly. `export` has been 
 removed until [1.26.0](https://github.com/docker/compose/issues/6511)