# SOVELLUKSEN PÄÄOHJELMA

# Kirjastojen ja modulien lataus
from calendar import c
import datetime
from inspect

# Luokka-määritykset

class Person():
    """dostring for Classname"""
    def __init__(self, firstname, lastname):
        self.firstname = firstname