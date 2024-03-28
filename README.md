# Intro to Flask - Hotels Lab

## Learning Goals

- Build and run a Flask application on your computer.
- Manipulate and test the structure of a request object.

***

## Key Vocab

- **Web Framework**: software that is designed to support the development of
  web applications. Web frameworks provide built-in tools for generating web
  servers, turning Python objects into HTML, and more.
- **Extension**: a package or module that adds functionality to a Flask
  application that it does not have by default.
- **Request**: an attempt by one machine to contact another over the internet.
- **Client**: an application or machine that accesses services being provided
  by a server through the internet.
- **Web Server**: a combination of software and hardware that uses Hypertext
  Transfer Protocol (HTTP) and other protocols to respond to requests made
  over the internet.
- **Web Server Gateway Interface (WSGI)**: an interface between web servers
  and applications.
- **Template Engine**: software that takes in strings with tokenized
  values, replacing the tokens with their values as output in a web browser.

***

## Instructions

This lab will give you more practice with Routing and Views in Flask. This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then enter the
`server` directory and run `pytest -x` to run your tests. Write your code in the `app.py` file in the `server` directory. Use these
instructions and `pytest`'s error messages to complete your work in the `app.py` file. If you prefer working in a Flask environment to running
your application as a script, remember to configure it with the following
commands from the `server` directory:

```console
$ export FLASK_APP=app.py
$ export FLASK_RUN_PORT=5555
```

In `app.py`, there is a `hotels` variable that contains a list that contains dictionaries with information about various hotels. You will need to retrieve information from this list while working on the deliverables.

## Deliverables

1. Create an `index()` view that has the route `/`. The `index()` view should return an `<h1>` element that contains text in the following format: `Welcome to the Hotels website! We have {number_of_hotels} hotels available`, where `number_of_hotels` should be replaced with the number of hotels in the `hotels` list.

Hint: The number of hotels in the `hotels` list means that you should get the length of the list. You can use the `len()` function the get the length of a list.

2. Create an `all_hotels()` view that has the route `/hotels`. The `all_hotels()` view should return a `<ul>` element that contains `<li>` elements for each of the hotels from the `hotels` list in `app.py`. The `<li>` elements should contain the information for each of the hotels from the `hotels` list in the following format: `Hotel # {id}: {name}`.

3. Create a `hotel_by_id()` view that takes one parameter, an integer. Its route should be of the format `/hotels/<id>`. The `hotel_by_id()` view should return an `<h1>` element that contains the information for a hotel found by its `id` from the `hotels` list in the following format: `Hotel # {id}: {name}`. If no hotel is found, the view should return an `<h1>` element that contains the following error message `Error: Hotel Not Found!`

Hint: `try` and `except` are useful to handle `IndexError`s that occur when the list index is out of range.

***

## Resources

- [A Minimal Application - Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#a-minimal-application)
- [Routing - Flask](https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing)
- [Chapter 2. Basic Application Structure - Flask Web Development, 2nd Edition](https://learning.oreilly.com/library/view/flask-web-development/9781491991725/ch02.html#idm140583868985008)
