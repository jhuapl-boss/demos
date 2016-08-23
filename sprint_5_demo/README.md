## Sprint 5 Demo

### Setup to Run the Demo

- Create a user account and download an API token:
    - Go to [the token page](https://api.theboss.io/token)
    - This will redirect you to the Single Sign On server. Create an account.
    - Once complete you'll be redirected to the current token page.  This will be replaced in the future by the Boss Managment Console.
    - Generate a token and enter it into demo.cfg
- Request "resource_manager" role
    - Roles are not automatically assigned to all users.  Send an email to iarpamicrons (at) jhuapl.edu to request access
- Install required python packages
    
    ```
    pip install -r requirements.txt
    ```
    
- Download ndio

    ```
    cd PATH_TO_THIS_DIR
    git clone https://github.com/jhuapl-boss/ndio.git
    ```

- Launch jupyter notebook while setting up your PYTHONPATH

```
export PYTHONPATH="$PYTHONPATH:PATH_TO_THIS_DIR/ndio:PATH_TO_THIS_DIR/JSAnimation/"

cd PATH_TO_THIS_DIR
jupyter notebook
````