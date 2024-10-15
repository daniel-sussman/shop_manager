# Database Project Starter

This is a starter project for you to use to start your Python database projects.

There are two videos to support:

* [A demonstration of setting up the project](https://www.youtube.com/watch?v=KMEt4GgWJXc)
* [A walkthrough of the project codebase](https://youtu.be/KMEt4GgWJXc?t=460)

## Setup

```shell
# Clone the repository to your local machine
; git clone git@github.com:makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Or, if you don't have SSH keys set up
; git clone https://github.com/makersacademy/databases-in-python-project-starter.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv databases-starter-venv

# Activate the virtual environment
; source databases-starter-venv/bin/activate 

# Install dependencies
(databases-starter-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Create the database
(databases-starter-venv); createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(databases-starter-venv); open lib/database_connection.py

# Run the tests - see below if you have any issues
(databases-starter-venv); pytest

# Run the app
(databases-starter-venv); python app.py
```

<br>
<details>
  <summary>I get a <code>ModuleNotFoundError: No module named 'psycopg'</code></summary>
  <br>
If, after activating your <code>venv</code> and installing dependencies, you see this error when running <code>pytest</code>, please deactivate and reactivate your <code>venv</code>. This should solve the problem - if not, contact your coach.
</details>
