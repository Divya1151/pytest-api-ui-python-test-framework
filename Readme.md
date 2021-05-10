# About the project

This is an automation project to automate Todoist which is a popular task tracking tool and a todolist.
Below are the scenarios which are automated:
- As a user, I can create a new todo item with a due date and a content (name)
- As a user, I can rename my todo item
- As a user, I can mark my todo item as completed to remove it from my list of todos

For above scenarios:
- API tests have been created [here](./tests/api_testcases)
  
 API Documention link: https://developer.todoist.com/sync/v8/#items

- UI tests have been created [here](./tests/ui_testcases)

Todoist Web app link: https://chrome.todoist.com/

## Tools and Technologies used

- Programming Language - Python
- Pytest
- Seleniumsour
- Requests
- PyHamcrest

# Setup & installation
If you run into any issues with the steps below, please let me know at `er.divya.singla@gmail.com`

## Python and VirtualEnv

- **Install Python 3.6 or higher**, Instructions https://www.python.org/downloads/mac-osx/,

  Alternatively you can run below command to install python

  > brew install python3

  pip3 get installed with python3

- **Install virtualenv** -  Virtualenv allows you to create an isolated Python environment, with full control over which Python version to use and which Python packages to install. To install virtualenv via pip run:
  - If you have only Python 3 installed:
    
    > pip install --user virtualenv.
  - If you have Python 2 and Python 3 installed (likely if you use mac or linux), run
    > pip3 install --user virtualenv instead.
  - If you need to figure out what you have installed, you can run
    > python --version and/or python3 --version from the command line.

## Setup a virtual environment

We will be using this virtual environment for our project
  
- **Create a virtual python environment**
  - Note that this will create the virtual environment in the current directory, so pick a convenient location.
  - If you have only Python 3 installed:
    
    > python -m virtualenv venv.
  - If you have both Python 2.7 and Python 3 installed:
    
    > python3 -m virtualenv -p python3 venv.
- **Activate the virtualenv**
  - Note that once the virtual environment is active, `python` and `pip` will be the Python 3 versions, since that is how we set up the virtual environment. So for the rest of the instructions it doesn't matter if you also have Python 2 installed, since we run everything in our virtual Python 3 environment.

    > source venv/bin/activate

- Once you're done with the virtual environment (i.e. no longer want to play around with the code), type `deactivate` to deactivate it.



## Open the project and install dependencies

Important: perform the steps below with your virtual activated environment.

  - Clone this repository or download the project and open in IDE(Pycharm...)
  - Install requirements.txt
    
    > pip install -r requirements.txt


## Download chrome browser

Important: Make sure that chrome browser is installed.

# Running the project
Since we are using pytest so we need to execute below commands to run the tests
  
  - In order to execute all the tests in the project

    > pytest tests/ -s -v
    
  - In order to execute all API test cases

    > pytest tests/api_testcases -s -v
    
  - In order to execute all UI test cases

    > pytest tests/ui_testcases -s -v
    
 - In order to execute specific module

    > pytest tests/api_testcases/test_ui_add_new_task.py -s -v
   
- In order to execute specific test case from a specific module

    > pytest tests/ui_testcases/test_ui_add_new_task.py::test_ui_add_new_task  -s -v
  



# Further reading

## More Pytest
- Pytest reference https://docs.pytest.org/en/latest/reference.html
- Pytest Quick Start Guide - Bruno Oliveira https://www.packtpub.com/web-development/pytest-quick-start-guide
- Python Testing with pytest: Simple, Rapid, Effective, and Scalable - Brian Okken https://pragprog.com/book/bopytest/python-testing-with-pytest

## More Python
- Python https://docs.python.org/3/


# Acknowledgements




