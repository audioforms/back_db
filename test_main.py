from flask import Flask
from flask_testing import TestCase
from main import *

class MyTest(TestCase):
    def create_app(self):
        return main.app
