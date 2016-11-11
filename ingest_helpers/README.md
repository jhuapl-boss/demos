## Ingest Helpers
Examples to get started ingesting data and reading data from the Boss

## Installation
- `mkdir` and `cd` to a directory of your choice

- Clone the demos repository
	
	```
	git clone https://github.com/jhuapl-boss/demos.git
	cd ingest_helpers
	```
- Use virtualenv to isolate the ingest client from your system Python installation

	- Using [virtualenv](https://virtualenv.pypa.io/en/stable/):
	
	```
	virtualenv ingest-env
	. ingest-env/bin/activate
	```
	
	- Using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):
	
	```
	mkvirtualenv ingest-env
	```
	
- Install Python dependencies
	
	```
	pip install -r requirements.txt
	```
	
## Setting up `intern`
You must configure [intern](https://github.com/jhuapl-boss/intern) with your secret API token:

- Go to [the token page](https://api.theboss.io/token). This will redirect you to the Single Sign On server.
-  Create an account by clicking the "Register" button or log in.
- Once complete you'll be redirected back to the current token page.  (This will be replaced in the future by the Boss Managment Console)
- Generate a token and copy it.
- Copy `boss.cfg.example` to `boss.cfg` and paste your token in

## Preparing For An Ingest Job
To ingest your dataset you must have already completed the following:

- Have setup `boss.cfg` as described above
- Have been granted the "resource_manager" role
- Have developed ingest-client plugins for your data, or your data is compatible with existing plugins

The script `setup_channel_for_ingest.py` will create a collection, coordinate frame, experiment, and channel for you based on a configuration file located in `./db_configs`. It will also automatically update an ingest job configuration file located in `./ingest_configs` for you.  Examples are provided, but you will need to customize these configuration files for your needs. 

Once the script completes, it will print the command to run the ingest-client.  Simply `cd` to your ingest-client directory and copy/paste the provided commands. 

## Visualizing Data in Jupyter
A jupyter notebook `visualize_cutout.ipynb` is provided to give an example of how to access and visualize data in the Boss with jupyter. Make sure you are in the `ingest_helpers` directory and simply run jupyter:

```
cd ./ingest_helpers
jupyter notebook
``` 