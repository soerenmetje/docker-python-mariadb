# This is a sample Python script.

import os
import sys

if __name__ == '__main__':

    print(f'Hi, PyCharm')

    try:
        print(os.environ["PORT"])
        print(os.environ["MYSQL_HOST"])
        print(os.environ["MYSQL_DATABASE"])
        print(os.environ["MYSQL_PORT"])
        print(os.environ["MYSQL_USER"])
        print(os.environ["MYSQL_PASSWORD"])
    except KeyError as e:
        print("Some needed environment variable is not set: ", e, file=sys.stderr)

    # TODO do stuff with Flask or so
