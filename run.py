#!/usr/bin/env python

from app import app
import logging
import sys

host='0.0.0.0'
port=5000
debug=False

if __name__ == '__main__':
    
    args = sys.argv
    
    for i, arg in enumerate(args):
        if (arg == "--host"):
            host = args[i + 1] 
        elif (arg == "--port"):
            port = args[i + 1]
        elif (arg == "--debug"):
            debug = args[i + 1]
    
    app.run(debug=debug,host=host,port=port)