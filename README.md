# Welcome to the AirBnB clone project!
<img src="https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png" />


## Language
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

- Name of the project : ``0x00. AirBnB clone - The console``
- Authors : <br>
[Valentin Repetto](https://github.com/valerepetto14) <br>
[Santiago Neira](https://github.com/sanei1509)

# We create a shell to manage our AirBnB objects.

This is the first step in creating our first full web application: the ``AirBnB clone``

## What’s a command interpreter (shell)?

It is a program that receives commands from a user,
our console has the following functions:

``create``  ``update`` ``Destroy``  ``store`` ``persists``  -> Objects

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Starting

Steps:
### 1 - Install python

````
sudo apt install python3.8
````

### 2 - Clone the repo on your computer
````
git clone https://github.com/sanei1509/holbertonschool-AirBnB_clone.git
````

### 3 - Execute the console
````
./console.py
(hbnb)
````
you should see the following prompt waiting for your commands

## Non interactive mode

````c
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
````


## Interactive Mode
````c
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
````

## Learning Objectives

General
- How to create a ``Python package``
- How to create a command interpreter in Python using the ``cmd module``
- What is ``Unit testing`` and how to implement it in a ``large project``
- How to ``serialize`` and ``deserialize`` a Class
- How to ``write`` and ``read`` a JSON file
- How to manage ``datetime``
- What is an ``UUID``
- What is ``*args`` and how to use it
- What is `` **kwargs `` and how to use it
- How to handle ``named arguments`` in a function



# Testing
we must run the tests in interactive and non-interactive mode

| Non interactive mode
````c
echo "python3 -m unittest discover tests" | bash
````

| Interactive mode
````c
python3 -m unittest discover tests"
````

# Ejemplos de uso de **Comandos**

## 1 - Create
````c
(hbnb) create <[class]>

========================Output======================================

(hbnb) create User
38f22813-2753-4d42-b37c-57a17f1e4f88
(hbnb)
````

## 2 - all

### Usage 1
````c
all <class>
````

### Usage 2

````
<nombre de clase>.all()
````

### Output
````c

(hbnb) User.all()
["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'John', 'age': '89'}"]
(hbnb) 

````

## 3 Show a class instances
muestra una instancia especifica


````c
================ Usage 1 ==============
(hbnb) show City 07062be7-fd57-4791-88a6-6a78806398c9

================ Usage 2 ==============

City.show(07062be7-fd57-4791-88a6-6a78806398c9)

========================Output======================================
[City] (07062be7-fd57-4791-88a6-6a78806398c9) {'id': '07062be7-fd57-4791-88a6-6a78806398c9', 'created_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356353), 'updated_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356365)}
(hbnb) 

````

## 4 Destroy a instance of the storage( file.json )

````c

==================== Usage 1 ==================
destroy User 38f22813-2753-4d42-b37c-57a17f1e4f88

==================== Usage 2 ===================
destroy.User("38f22813-2753-4d42-b37c-57a17f1e4f88")

========================Output======================================

(hbnb) User.all()
["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'John', 'age': '89'}"]
(hbnb) 

````

## 5 Update attribute, of instance to the storage

````c

(hbnb) User.all()

["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'John', 'age': '89'}"]
(hbnb)

================= Usage 1 ======================
update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Naruto"

================= Usage 2 =======================
update.User(49faff9a-6318-451f-87b6-910505c55907, first_name, "Naruto")

========================Output======================================
["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'Naruto', 'age': '89'}"]
(hbnb)

````


# Unittest for classes and console

## run unittest

````c
python3 -m unittest discover tests


=============Output================
.............................................................
----------------------------------------------------------------------
Ran 61 tests in 0.531s

OK
````


## Test the console capturing the output

````c
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
````

## Structure of files

````c
console.py
models/
    __init__.py
    amenity.py
    base_model.py
    city.py
    place.py
    review.py
    state.py
    user.py
    engine/
        __init__.py
        file_storage.py
tests/
    __init__.py
    test_console.py
    test_models/
        __init__.py
        test_amenity.py
        test_base_model.py
        test_city.py
        test_place.py
        test_review.py
        test_state.py
        test_user.py
````


# Authors contact

[Valentin Repetto - linkedin](https://www.linkedin.com/in/valentin-repetto-6aa6711a0/) <br>
[Santiago Neira - linkedin](https://www.linkedin.com/in/santiago-neira-4479501b7/)

