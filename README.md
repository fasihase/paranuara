# Paranuara Challange
Paranuara is a class-m planet. Those types of planets can support human life, for that reason the president of the Checktoporov decides to send some people to colonise this new planet and reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

## Getting Started
   This Paranuara API Code is developed and verified on Windows OS using Python and Django.
   
### Installation

This program requires Python 3.5 or above to run.

1. Some requirements:
    
    #### Install Python, If you don't already have: 
    
    ```commandline
    Download and execute the latest Python installation package from Python.org.
    ```
    
    #### Install pip, if you don't already have:
    
      1. Download get-pip.py to a folder on your computer.
      2. Open a command prompt and navigate to the folder containing get-pip.py.
      3. Run the following command:
        
          ```commandline
          python get-pip.py
          ```
      4. Pip is now installed!

    #### Install virtualenv if you don't already have
    
    ```commandline
    pip install virtualenv
    pip install virtualenvwrapper-win
    ```
    
    #### Create virtual environment if it does not exist
    
    ```commandline
    mkvirtualenv paranuara-hivery
    ```
 
 2. Choose a folder to install Paranuara. Create and activate new virtualenv.
    
    #### Download the project

    ```commandline
    Download or Clone the project from *****GIT LOCATION****** into paranuara-hivery folder 
    ```
    
    #### Activate Virtual Environment, if not activated:
    
    ```commandline
    workon paranuara-hivery
    ```
    
 3. Install dependencies
    
    ```commandline
    cd paranuara-hivery/paranuara
    pip install -r requirements.txt
    ```

 4. Run these commands to instantiate new paranuara application:

    ```commandline
    python manage migrate
    python manage runserver
    ```
Then navigate to http://127.0.0.1:8000/ 

### Usage

* Eager to use different companies.json or people.json files:
    
    1. Copy companies.json and/or people.json file to resource folder availabe under project folder
    2. Run below command:
    
        ```commandline
        python manage.py flush
        ```
    3. Activate the virtual environemnt 
    4. Navigate to the project folder containing load_companies.py and load_people.py
    5. Run below command
    
        ```commandline
        python load_companies.py
        python load_people.py
        ```
      
* To run tests, Run below command:

  ```commandline
  python manage.py test
  ``` 

## REST API Endpoints:

1. http://localhost:8000/api/employees/1/
    
    Given a company (index), returns all its employees.
    Where `1` is index of the company as specified in source data.
    
2. http://localhost:8000/api/twopeople/10/11/
    
    Given 2 people, provides their information (Name, Age, Address, phone) and 
    the list of their friends in common which have brown eyes and are still alive.
    Where `10` and `11` are indexes of people as specified in source data.
    
3. http://localhost:8000/api/fruits_and_vegetables/5/
    
    Given 1 person, provides a list of fruits and vegetables they like. This endpoint
    respects this interface for the output:
    ```json
    {
      "username": "Grace Kelly",
      "age": 24,
      "fruits": [
          "strawberry"
      ],
      "vegetables": [
          "cucumber",
          "beetroot",
          "carrot"
      ]
    }
    ```

