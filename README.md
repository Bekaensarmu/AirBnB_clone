# 0x00. AirBnB clone - The console

![Logo AirBnb](https://github.com/JuanSebastianGB/AirBnB_clone/blob/main/images/65f4a1dd9c51265f49d0.png?raw=true)

## Description of the project
This is the first step towards building your first full web application: the **AirBnB clone**. The aim of the project is to deploy a replica of the [Airbnb Website](https://www.airbnb.com/) using my server. The final version of this project will have:
- ```A command interpreter to manipulate data without a visual interface, like a shell (for development and debugging)```
- ```A website (front-end) with static and dynamic functionalities```
- ```A comprehensive database to manage the backend functionalities```
- ```An API that provides a communication interface between the front and backend of the system.```

## Main Resources 

-   [cmd module](https://docs.python.org/3.8/library/cmd.html "cmd module")
-   [cmd module in depth](http://pymotw.com/2/cmd/ "cmd module in depth")
-   [uuid module](https://docs.python.org/3.8/library/uuid.html "uuid module")
-   [datetime](https://docs.python.org/3.8/library/datetime.html "datetime")
-   [unittest module](https://docs.python.org/3.8/library/unittest.html#module-unittest "unittest module")
-   [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/ "args/kwargs")
-   [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html "Python test cheatsheet")
-   [cmd module wiki page](https://wiki.python.org/moin/CmdModule "cmd module wiki page")
-   [python unittest](https://realpython.com/python-testing/ "python unittest")

### Storage

All the classes are handled by the `Storage` engine in the `FileStorage` Class.

## Installation


```bash
git clone https://github.com/aysuarex/AirBnB_clone.git
```
change to the `AirBnb` directory and run the command:
```bash
 ./console.py
```

### Execution
In interactive mode
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
in Non-interactive mode
```bash
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
```

## Testing
All the test are defined in the `tests` folder.
### Documentation
* Modules:
```python
python3 -c 'print(__import__("my_module").__doc__)'
```
* Classes:
```python
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
```
* Functions (inside and outside a class):
```python
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
and
```python
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
```
### Python Unit Tests
* unittest module
* File extension ``` .py ```
* Files and folders star with ```test_```
* Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
* Execution command: ```python3 -m unittest discover tests```
* or: ```python3 -m unittest tests/test_models/test_base.py```
### run test in interactive mode
```bash
echo "python3 -m unittest discover tests" | bash
```
### run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:
```bash
python3 -m unittest discover tests
```
## Usage
* Start the console in interactive mode:
```bash
$ ./console.py
(hbnb)
```
* Use help to see the available commands:
```bash
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
```
* Quit the console:
```bash
(hbnb) quit
$
```
### Commands
> The commands are displayed in the following format *Command / usage / example with output*
* Create
> *Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.*
```bash
create <class>
```
```bash
(hbnb) create BaseModel
6cfb47c4-a434-4da7-ac03-2122624c3762
(hbnb)
```
* Show
```bash
show <class> <id>
```
```bash
(hbnb) show BaseModel 6cfb47c4-a434-4da7-ac03-2122624c3762
[BaseModel] (a) [BaseModel] (6cfb47c4-a434-4da7-ac03-2122624c3762) {'id': '6cfb47c4-a434-4da7-ac03-2122624c3762', 'created_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571360), 'updated_at': datetime.datetime(2021, 11, 14, 3, 28, 45, 571389)}
(hbnb)
```
* Destroy
> *Deletes an instance of a given class with a given ID.*
> *Update the file.json*
```bash
(hbnb) create User
0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) destroy User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
(hbnb) show User 0c98d2b8-7ffa-42b7-8009-d9d54b69a472
** no instance found **
(hbnb)
```
* all
> *Prints all string representation of all instances of a given class.*
> *If no class is passed, all classes are printed.*

```bash
(hbnb) create BaseModel
e45ddda9-eb80-4858-99a9-226d4f08a629
(hbnb) all BaseModel
["[BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) [BaseModel] (4c8f7ebc-257f-4ed1-b26b-e7aace459897) {'id': '4c8f7ebc-257f-4ed1-b26b-e7aace459897', 'created_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447155), 'updated_at': datetime.datetime(2021, 11, 13, 22, 19, 19, 447257), 'name': 'My First Model', 'my_number': 89}"]
["[BaseMode
```
* count
> *Prints the number of instances of a given class.*
```bash
(hbnb) create City
4e01c33e-2564-42c2-b61c-17e512898bad
(hbnb) create City
e952b772-80a5-41e9-b728-6bc4dc5c21b4
(hbnb) count City
2
(hbnb)
```
* update
> *Updates an instance based on the class name, id, and kwargs passed.*
> *Update the file.json*
```bash
(hbnb) create User
1afa163d-486e-467a-8d38-3040afeaa1a1
(hbnb) update User 1afa163d-486e-467a-8d38-3040afeaa1a1 email "aysuarex@gmail.com"
(hbnb) show User 1afa163d-486e-467a-8d38-3040afeaa1a1
[User] (s) [User] (1afa163d-486e-467a-8d38-3040afeaa1a1) {'id': '1afa163d-486e-467a-8d38-3040afeaa1a1', 'created_at': datetime.datetime(2021, 11, 14, 23, 42, 10, 502157), 'updated_at': datetime.datetime(2021, 11, 14, 23, 42, 10, 502186), 'email': 'aysuarex@gmail.com'}
(hbnb)
```
## Authors
<details>
    <summary>Beka Gerbaba</summary>
    <ul>
    <li><a href="https://www.github.com/Bekaensarmu">Github</a></li>
    <li><a href="mailto:beekanensarmu@gmail.com">e-mail</a></li>
    </ul>
</details>
<details>
    <summary>Lencho Ajema</summary>
    <ul>
    <li><a href="https://www.github.com/lenchoajema">Github</a></li>
    <li><a href="mailto:lenchoajema@gmail.com">e-mail</a></li>
    </ul>
</details>
