import pandas as pd
import random
from csv import writer


def choosefirstname(rand, fnm, fnf):
    if rand % 2 == 0:
        randfirstname = firstnamemale
        index = fnm
    else:
        randfirstname = firstnamefemal
        index = fnf
    return randfirstname, index


def chooserandommale():
    fnm = random.randint(0, 2065)
    return fnm


def chooserandomfemal():
    fnf = random.randint(0, 2244)
    return fnf


def append_row(filename, dict_of_elem):
    with open(filename, 'a+', newline='') as write_obj:
        dict_writer = writer(write_obj)
        dict_writer.writerow(dict_of_elem)


firstnamemale = pd.read_csv("Arabic_English_Names_male.csv")
firstnamefemal = pd.read_csv("Arabic_English_Names_female.csv")
secondnamemale = pd.read_csv("Arabic_English_Names_male.csv")
surenamemale = pd.read_csv("Arabic_English_Names_male.csv")

for i in range(0, 5000):
    fnm = chooserandommale()
    fnf = chooserandomfemal()
    rand = random.randint(0, 100)
    firstnamedata, index = choosefirstname(rand, fnm, fnf)
    firstname = firstnamedata['Arabic_Name'][index]
    secondindex = chooserandommale()
    secondname = firstnamemale['Arabic_Name'][secondindex]
    thirdindex = chooserandommale()
    surename = firstnamemale['Arabic_Name'][thirdindex]
    fullname = "- [{} {} {}](name)".format(firstname, secondname, surename)
    name = [fullname]
    append_row('Arabic_English_full_name.csv', name)
