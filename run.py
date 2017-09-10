#!/usr/bin/env python

import os
from api import app
import config

if __name__ == '__main__':
    app.run(debug=config.DEBUG)