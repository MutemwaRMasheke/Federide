#!/usr/bin/env python

#-----------------------------------------------------------------------
# runserver.py
# Author: Mutemwa Masheke, Ian Jaccojwang
#-----------------------------------------------------------------------

from sys import exit, stderr
import argparse
from reg import app

FILE_NAME = "runserver: "

def main():
    try:
        # Parse command line args
        parser = argparse.ArgumentParser(description='The registrar \
            application', allow_abbrev=False)
        parser.add_argument('port', type=int, help='the port at which\
             the server should listen')
        args = parser.parse_args()

        try:
            app.run(host='0.0.0.0', port=args.port, debug=True)
        except Exception as ex:
            print(ex, file=stderr)
            exit(1)

    except Exception as ex:
        print(str(ex), file=stderr)
        exit(1)

if __name__ == '__main__':
    main()
