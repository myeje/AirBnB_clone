# AirBnB Clone - The Console

  
![AirBnB clone](https://miro.medium.com/v2/resize:fit:828/format:webp/1*87ce_sVbWHSHpDhCMBwKtA.png)


## Background Context

**First step: Write a command interpreter to manage your AirBnB objects.**

This is the first step towards building your first full web application:

the AirBnB clone. Each task is linked and will help you to:



- Put in place a parent class (called BaseModel) to take care of the initialize

- Create a simple flow of serialization/deserialization

- Create all classes used for AirBnB that inherit from BaseModel

- Create the first abstracted storage engine of the project: File storage.

- Create all unittests to validate all our classes and storage engine


**What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. 

In our case, we want to be able to manage the objects of our project:


- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object


### Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, 

without the help of Google:


##General

- How to create a Python package

- How to create a command interpreter in Python using the cmd module

- What is Unit testing and how to implement it in a large project

- How to serialize and deserialize a Class

- How to write and read a JSON file

- How to manage datetime

- What is an UUID

- What is "*args" *and how to use it

- What is **kwargs **and how to use it

- How to handle named arguments in a function



## Execution

  
Your shell should work like this in interactive mode:

  
```
$ ./console.py
:) help

Documented commands (type help <topic>):
========================================
EOF help quit

:)
:)
:) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

:)

Documented commands (type help <topic>):
========================================

EOF help quit
:)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
:)


Documented commands (type help <topic>):
========================================
EOF help quit
:)
$
