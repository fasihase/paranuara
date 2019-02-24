# Paranuara Challange
Paranuara is a class-m planet. Those types of planets can support human life, for that reason the president of the Checktoporov decides to send some people to colonise this new planet and reduce the number of people in their own country. After 10 years, the new president wants to know how the new colony is growing, and wants some information about his citizens. Hence he hired you to build a rest API to provide the desired information.

## Getting Started
   This Paranuara API Code is developed and verified on **Windows OS** using **Python** and **Django**.

### Installation

This program requires **Python 3.5** or above to run.

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

 2. Install Paranuara in already created virtualenv.

    #### Download the project

    ```commandline
    Download(and Unzip) or Clone the project from https://github.com/fasihase/paranuara.git into paranuara-hivery folder.
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

* To run tests, Run below command:

  ```commandline
  python manage.py test
  ```

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

## REST API Endpoints:

1. http://localhost:8000/api/employees/1/
                    OR   
   http://127.0.0.1:8000/api/employees/?company=PERMADYNE

    Given a company (**_index_** or **_name_**), returns all its employees.
    Where `1` is index of the company as specified in source data.
    ```json
    {
    "index": 1,
    "company": "PERMADYNE",
    "employees": [
        {
            "index": 289,
            "name": "Frost Foley",
            "age": 22,
            "address": "824 Clark Street, Utting, New Mexico, 3994",
            "phone": "+1 (987) 436-3916"
        },
        {
            "index": 580,
            "name": "Luna Rodgers",
            "age": 56,
            "address": "430 Frank Court, Camino, American Samoa, 2134",
            "phone": "+1 (889) 544-3275"
        },
        {
            "index": 670,
            "name": "Boyer Raymond",
            "age": 20,
            "address": "326 Times Placez, Cumminsville, Montana, 2703",
            "phone": "+1 (867) 458-3241"
        },
        {
            "index": 714,
            "name": "Solomon Cooke",
            "age": 51,
            "address": "340 Granite Street, Cazadero, Colorado, 1597",
            "phone": "+1 (844) 460-3877"
        },
        {
            "index": 828,
            "name": "Walter Avery",
            "age": 35,
            "address": "797 Vandervoort Place, Wheaton, Kentucky, 1051",
            "phone": "+1 (992) 532-3748"
        },
        {
            "index": 928,
            "name": "Hester Malone",
            "age": 38,
            "address": "928 Seaview Court, Jacksonburg, American Samoa, 4161",
            "phone": "+1 (847) 435-3662"
        },
        {
            "index": 985,
            "name": "Arlene Erickson",
            "age": 46,
            "address": "821 Coventry Road, Manchester, New Mexico, 2751",
            "phone": "+1 (878) 521-3781"
        }
      ]
    }
    ```

2. http://localhost:8000/api/twopeople/10/15/

    Given 2 people, provides their information (Name, Age, Address, phone) and
    the list of their friends in common which have brown eyes and are still alive.
    Where `10` and `15` are indexes of people as specified in source data.
    ```Json
    {
    "person1": {
        "index": 10,
        "name": "Kathleen Clarke",
        "age": 30,
        "address": "195 Ovington Avenue, Bonanza, Indiana, 7131",
        "phone": "+1 (888) 523-3982"
    },
    "person2": {
        "index": 15,
        "name": "Morris Logan",
        "age": 25,
        "address": "776 Thatford Avenue, Wattsville, New York, 8981",
        "phone": "+1 (830) 441-2767"
    },
    "common_friends": [
        {
            "index": 0,
            "name": "Carmella Lambert",
            "age": 61,
            "address": "628 Sumner Place, Sperryville, American Samoa, 9819",
            "phone": "+1 (910) 567-3630"
        },
        {
            "index": 1,
            "name": "Decker Mckenzie",
            "age": 60,
            "address": "492 Stockton Street, Lawrence, Guam, 4854",
            "phone": "+1 (893) 587-3311"
        },
        {
            "index": 2,
            "name": "Bonnie Bass",
            "age": 54,
            "address": "455 Dictum Court, Nadine, Mississippi, 6499",
            "phone": "+1 (823) 428-3710"
        },
        {
            "index": 3,
            "name": "Rosemary Hayes",
            "age": 30,
            "address": "130 Bay Parkway, Marshall, Virgin Islands, 298",
            "phone": "+1 (984) 437-3226"
        },
        {
            "index": 4,
            "name": "Mindy Beasley",
            "age": 62,
            "address": "628 Brevoort Place, Bellamy, Kansas, 2696",
            "phone": "+1 (862) 503-2197"
        },
        {
            "index": 5,
            "name": "Grace Kelly",
            "age": 24,
            "address": "762 Tabor Court, Ola, Idaho, 4329",
            "phone": "+1 (923) 600-2868"
        },
        {
            "index": 6,
            "name": "Cote Booth",
            "age": 26,
            "address": "394 Loring Avenue, Salvo, Maryland, 9396",
            "phone": "+1 (842) 598-3525"
        }
      ]
    }
    ```

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
