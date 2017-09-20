#!/usr/bin/env python

from app import app
import logging
import sys

class RunApp():

    DEBUG="--debug"
    HOST="--host"
    PORT="--port"

    def __init__(self):
            
        logging.getLogger().setLevel(logging.INFO)
        
        self.args_dic={
            self.DEBUG: False,
            self.HOST: '0.0.0.0',
            self.PORT: 5007
        }

    def run(self,args):
        
        d=self.args_dic
               
        for i, arg in enumerate(args):
            if(arg in d):
                d[arg] = args[i + 1]

        logging.info(" Debug: " + str(d[self.DEBUG]))
        logging.info(" Host: " + str(d[self.HOST]))
        logging.info(" Port: " + str(d[self.PORT]))
        
        app.run(
            debug=d[self.DEBUG],
            host=d[self.HOST],
            port=int(d[self.PORT])
        )

if __name__ == '__main__':
    RunApp().run(sys.argv)
   