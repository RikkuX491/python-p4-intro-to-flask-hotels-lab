#!/usr/bin/env python3

from flask import Flask

hotels = [
    {
        "id": 1,
        "name": "Marriott"
    },
    {
        "id": 2,
        "name": "Hampton Inn"
    },
    {
        "id": 3,
        "name": "Flatiron Resort"
    }
]

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
