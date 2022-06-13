# Install
Clone the repository and open the project directory:
```
$ git clone git@github.com:VKasaraba/project4_library.git
$ cd library
```

Download Python3 from official source https://www.python.org/downloads/

Check that python was installed successfully by checking its version:
```
$ python --version
```

Create and activate python virtual environment and install the requirements:
```
$ python3 -m venv .venv/
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

Get ```.env``` file from developers and connedct it to ```settings.py```:
```
$ source .env
```

# Start the project
Apply migrations to your database (database configs are specified in ```.env``` secrets):
```
$ python manage.py migrate
```

Run the test server on localhost:
```
$ python manage.py runserver
```

The application will running on http://127.0.0.1:8000
To stop the web server press CTRL+C.