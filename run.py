#!/usr/bin/env python

from app import app
import config
import logging
import os

if __name__ == '__main__':
    app.run(debug=config.DEBUG, host='0.0.0.0', port=os.environ.get("UM_PORT", 5000))