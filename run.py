#!/usr/bin/env python

from app import app
import logging
import sys

host='0.0.0.0'
port=5007
debug=True

if __name__ == '__main__':

    logging.getLogger().setLevel(logging.INFO)
    
    args = sys.argv
    
    for i, arg in enumerate(args):
        if (arg == "--host"):
            host = args[i + 1] 
        elif (arg == "--port"):
            port = args[i + 1]
        elif (arg == "--debug"):
            debug = args[i + 1]

    logging.info(" Host: " + str(host))
    logging.info(" Port: " + str(port))
    logging.info(" Debug: " + str(debug))
    
    app.run(debug=debug,host=host,port=int(port))