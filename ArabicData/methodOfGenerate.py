import pandas as pd
import random
from csv import writer

def choosefirstname(filemale,filefemal,rand, fnm, fnf):
        if rand % 2 == 0:
            randfirstname = filemale
            index = fnm
        else:
            randfirstname = filefemal
            index = fnf
        return randfirstname, index


def chooserandommale():
        fnm = random.randint(0, 853)
        return fnm


def chooserandomfemal():
        fnf = random.randint(0, 552)
        return fnf


def append_row(filename, dict_of_elem):
        with open(filename, 'a+', newline='') as write_obj:
            dict_writer = writer(write_obj)
            dict_writer.writerow(dict_of_elem)





