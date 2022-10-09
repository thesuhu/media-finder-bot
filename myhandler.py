import logging
import random
import os
from datetime import date
today = str(date.today())


class myFileHandler(logging.FileHandler):
    def __init__(self, path, fileName, mode):
        fileName = path+"/"+today+".txt"
        super(myFileHandler, self).__init__(fileName, mode) # mode: a=merge, w=overwrite
